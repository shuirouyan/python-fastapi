#!~/myenv/bin/python3
from fastapi import FastAPI
import uvicorn, logging
from log_config import LOGGING_CONFIG

# FastAPI 应用
app = FastAPI()

logger = logging.getLogger("fastapi_app")

@app.on_event("startup")
async def startup_event():
    logger.info("Application startup: Custom logger is ready!")

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed!")
    return {"message": "Hello, FastAPI"}

if __name__ == "__main__":
    uvicorn.run(
        "code:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_config=LOGGING_CONFIG,  # 使用自定义日志配置
    )
