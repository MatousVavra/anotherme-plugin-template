from fastapi import APIRouter


class Plugin:
    def on_load(self, ctx):
        router = APIRouter()

        @router.get("")
        async def hello():
            return {"message": "Hello from the AnotherMe plugin template!"}

        ctx.register_router(router)
