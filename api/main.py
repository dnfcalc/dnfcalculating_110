# encoding:utf-8
# api docs:https://fastapi.tiangolo.com/zh/tutorial/first-steps/
import sys
import uvicorn
from multiprocessing import cpu_count,freeze_support
from app import global_init

if __name__ == '__main__':

    global_init()
    workers = max(cpu_count()-1,1)
    freeze_support()
    uvicorn.run(
        # 运行的 py 文件:FastAPI 实例对象
        "app:app",
        # 访问url，默认 127.0.0.1
        # host="0.0.0.0",
        # 访问端口，默认 8080,后续需要做端口检测是否被占用
        port=17173,
        # 热更新，有内容修改自动重启服务器
        reload=sys.argv[0].endswith(".py"),
        # 同 reload
        debug=sys.argv[0].endswith(".py"),
        workers=workers
        )

    # print(os.getppid())
