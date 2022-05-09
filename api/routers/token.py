import time
import base64
import hmac
from typing import Optional

from fastapi import Header
from core.store import store


class AlterState:
    def __init__(self, alter: str):
        self.alter = alter


def createToken(alter: str, expire=86400):
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode("utf-8")
    sha1_tshex_str = hmac.new(alter.encode(
        "utf-8"), ts_byte, 'sha1').hexdigest()
    token = ts_str+':'+sha1_tshex_str
    token = base64.urlsafe_b64encode(token.encode("utf-8")).decode("utf-8")
    store.set(token, AlterState(alter))
    return token


def readToken(token):
    return store.get(token)


def authorize(access_token: Optional[str] = Header(None)):
    if access_token is not None:
        state = readToken(access_token)
        if state is not None:
            return state.alter
