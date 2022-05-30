from fastapi import APIRouter
from utils.apiTools import reponse

appRouter = APIRouter()


@appRouter.get(path="/heartbeat")
async def heartbeat():
    return reponse(data=None)
