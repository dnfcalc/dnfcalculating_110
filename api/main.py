# encoding:utf-8
# api docs:https://fastapi.tiangolo.com/zh/tutorial/first-steps/
import sys

import uvicorn
from fastapi import FastAPI
from routers.app import appRouter
from routers.calc import calcRouter
from routers.info import infoRouter
from routers.open import openRouter
from utils.apiTools import register_cors, register_exception
from utils.render import Renderer

app = FastAPI(docs_url=None,redoc_url=None)

# 全局的异常处理
register_exception(app)
# 跨域支持
register_cors(app)

# 路由添加注册
app.include_router(infoRouter, prefix="/api", tags=['信息接口'])

app.include_router(calcRouter, prefix="/api", tags=['计算接口'])
app.include_router(appRouter, prefix="/api", tags=['服务接口'])
app.include_router(openRouter, prefix="/api", tags=['三方接口'])


def global_init():
    import json
    import os
    info = []
    if os.path.exists("./dataFiles/set-info.json"):
        with open("./dataFiles/set-info.json", encoding='utf-8') as fp:
            info = json.load(fp)
    detail = [0] * len(info)
    if not os.path.exists('./sets'):
        os.makedirs('./sets')
        with open('./sets/global.json', "w", encoding='utf-8') as fp:
            json.dump(detail, fp, ensure_ascii=False, indent=2)


if __name__ == '__main__':

    global_init()
    try:
        if sys.argv[0].endswith(".py"):
            uvicorn.run(
                # 运行的 py 文件:FastAPI 实例对象
                "main:app",
                # 访问url，默认 127.0.0.1
                # host="0.0.0.0",
                # 访问端口，默认 8080,后续需要做端口检测是否被占用
                port=17173,
                # 热更新，有内容修改自动重启服务器
                reload=True,
                # 同 reload
                debug=True)
        else:
            app.mount(
                "/", Renderer(directory="app/renderer", html=True), name="static")
            uvicorn.run(
                # 运行的 py 文件:FastAPI 实例对象
                app,
                # 访问url，默认 127.0.0.1
                # host="0.0.0.0",
                # 访问端口，默认 8080,后续需要做端口检测是否被占用
                port=17173,
                # 热更新，有内容修改自动重启服务器
                reload=False,
                # 同 reload
                debug=False,
            )
    except Exception as ex:
        print(ex)

    # print(os.getppid())
