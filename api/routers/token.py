import base64
import hmac
import time
from typing import Optional

from core.baseClass.character import Character, createCharcter
from core.store import store
from fastapi import Body, Header


class AlterState:
    def __init__(self, alter: str, token: str, charcater: Character):
        self.alter = alter
        self.token = token
        self.origin = alter.split('.')[-1]
        self.character = charcater


def createToken(alter: str, expire=86400):
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode("utf-8")
    sha1_tshex_str = hmac.new(alter.encode(
        "utf-8"), ts_byte, 'sha1').hexdigest()
    token = ts_str+':'+sha1_tshex_str
    token = base64.urlsafe_b64encode(token.encode("utf-8")).decode("utf-8")
    character = createCharcter(alter)
    store.set(token, AlterState(alter, token, character))
    return token


def readToken(token) -> AlterState:
    return store.get(token)


def authorize(access_token: Optional[str] = Header(None)):
    if access_token is not None:
        return readToken(access_token)
