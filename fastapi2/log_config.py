# log_config.py

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "fmt": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"],
    },
    "loggers": {
        "fastapi_app": {  # 自定义日志配置
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
        "uvicorn": {  # uvicorn 的主日志
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
        "uvicorn.access": {  # uvicorn 的访问日志
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
    },
}
