#!~/myenv/bin/python3

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn, logging
import json
from datetime import datetime

# 配置日志
logging.basicConfig(
            level=logging.INFO,
                format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                )

app=FastAPI()

logger = logging.getLogger("fastapi_app")


# 获取日志对象
logger = logging.getLogger("fastapi_app")


@app.on_event("startup")
async def startup_event():
    logger.info("Application startup: Custom logger is ready!")

@app.get('/')
def get_msg():
    logger.info("Root endpoint accessed!")

    return json.dumps({"message":"t1"}) + '\n'

@app.get('/msg')
def get_msg():
    logger.info('q:')
    return json.dumps({"message":"t1", "date": str(datetime.now())}) + '\n'

@app.get('/get/{item_id}')
async def get_item_info(item_id: str):
    return {"time": str(datetime.now()), "itemId": item_id}

@app.get('/get1/query')
async def get_query_info(item_id: int | None=12, q: str | None=None): 
    logger.info("datetime:{}, q:{}, item_id:{}".format(datetime.now(), q, item_id))
    if q:
        return {"datetime": str(datetime.now()), "q": q, "item_id": item_id}
    return {"datetime": datetime.now(), "item_id": item_id}

# cros
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)



if __name__=='__main__':
    # run
    logger.info("Root endpoint accessed!")
    logger.info("Root endpoint accessed")  # 打印日志
    logger.info("Root endpoint accessed")  # 打印日志

    uvicorn.run('example01:app', host='0.0.0.0', port=8000, reload=False, log_level="info",  workers=1)
