# encoding:utf-8
# api docs:https://fastapi.tiangolo.com/zh/tutorial/first-steps/
import os
from fastapi import FastAPI
import uvicorn
import sys
from routers.info import infoRouter
from routers.calc import calcRouter
from routers.app import appRouter
from utils.apiTools import register_exception, register_cors
from starlette.staticfiles import StaticFiles

app = FastAPI(docs_url=None)

# 全局的异常处理
register_exception(app)
# 跨域支持
register_cors(app)

# 路由添加注册
app.include_router(infoRouter, prefix="/api", tags=['杂项信息接口'])

app.include_router(calcRouter, prefix="/api", tags=['杂项信息接口'])
app.include_router(appRouter, prefix="/api", tags=['杂项信息接口'])

if __name__ == '__main__':
    if sys.argv[0].endswith(".py"):
        uvicorn.run(
            # 运行的 py 文件:FastAPI 实例对象
            app="main:app",
            # 访问url，默认 127.0.0.1
            host="0.0.0.0",
            # 访问端口，默认 8080,后续需要做端口检测是否被占用
            port=17173,
            # 热更新，有内容修改自动重启服务器
            reload=True,
            # 同 reload
            debug=True)
    else:
        app.mount("/web",StaticFiles(directory="app/dist/web/renderer"),name="static")
        uvicorn.run(
            # 运行的 py 文件:FastAPI 实例对象
            app,
            # 访问url，默认 127.0.0.1
            host="0.0.0.0",
            # 访问端口，默认 8080,后续需要做端口检测是否被占用
            port=17173,
            # 热更新，有内容修改自动重启服务器
            reload=False,
            # 同 reload
            debug=False)

    # print(os.getppid())
