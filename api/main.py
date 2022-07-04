# encoding:utf-8
# api docs:https://fastapi.tiangolo.com/zh/tutorial/first-steps/
import os
import sys

import uvicorn
from fastapi import FastAPI
from routers.app import appRouter
from routers.calc import calcRouter
from routers.info import infoRouter
from starlette.responses import FileResponse, HTMLResponse
from starlette.staticfiles import StaticFiles
from utils.apiTools import register_cors, register_exception

app = FastAPI(docs_url=None)

# 全局的异常处理
register_exception(app)
# 跨域支持
register_cors(app)

# 路由添加注册
app.include_router(infoRouter, prefix="/api", tags=['杂项信息接口'])

app.include_router(calcRouter, prefix="/api", tags=['杂项信息接口'])
app.include_router(appRouter, prefix="/api", tags=['杂项信息接口'])


def not_found(request, exc):
    with open("app/renderer/index.html", "r", encoding="utf-8") as fp:
        return HTMLResponse(fp.read())


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
        app.mount(
            "/", StaticFiles(directory="app/renderer", html=True), name="static")
        app.add_exception_handler(404, not_found)
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
            debug=False,
        )

    # print(os.getppid())
