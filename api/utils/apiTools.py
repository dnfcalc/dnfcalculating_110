import json
from logging import Logger
import sys
import traceback
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse, Response
from typing import Generic, List, TypeVar, Union
from pydantic.generics import GenericModel
from fastapi.middleware.cors import CORSMiddleware

T = TypeVar('T')


class Return(GenericModel, Generic[T]):
    code: int = 200
    message: str = ""
    data: Union[T, dict, str] = None


def response(*, code=200, data: Union[list, dict, str], message="Success"):
    return Return(code=code, message=message, data=data)


def register_exception(app: FastAPI):
    """
    全局异常捕获
    :param app:
    :return:
    """
    # 捕获全部异常
    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request, ex: Exception):
        # api = str(request.url).split("api/")[1]
        info = traceback.format_exc().replace(
            "  ", "").split("\n")[-4:-1]
        info[0] = info[0].split("\\")[-1].replace("\"",":").replace(",","")
        info = "\n \r".join(info)

        # traceback.print_last(sys.exc_info())
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            # 一定要加
            headers={
                "Access-Control-Allow-Origin": "*"
            },
            content={
                "code": 500,
                "message":info,
                # f"api:{api} \n \r{info}",
                "data": []
            })


def register_cors(app: FastAPI):
    """
    支持跨域
    :param app:
    :return:
    """

    app.add_middleware(
        CORSMiddleware,
        allow_origin_regex='https?://.*',  # 改成用正则就行了
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
