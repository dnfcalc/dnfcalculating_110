from fastapi import APIRouter
from utils.apiTools import response

appRouter = APIRouter()


@appRouter.get(path="/heartbeat")
async def heartbeat():
    return response(data=None)
