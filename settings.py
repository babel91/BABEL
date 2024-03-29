import os
import logging

from logging.config import dictConfig
from dotenv import load_dotenv

load_dotenv()

DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")
CH_BOTS = os.getenv("CH_BOTS")
CH_DMP = os.getenv("CH_DMP")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

LOGGING_CONFIG = {
    "version": 1,
    "disabled_existing_loggers": False, 
    "formatters":{  
        "verbose":{
            "format": "%(levelname)-7s - %(name)-15s - %(asctime) 23s - %(funcName)s - %(module)-9s - %(message)-s"
        },
        "standard":{
            "format": "%(levelname)-7s - %(name)-15s : %(message)s"
        }
    },
    "handlers":{
        "console":{
            'level':"DEBUG",
            'class':"logging.StreamHandler",
            'formatter': "standard"
        },
        "console2":{
            'level':"WARNING",
            'class':"logging.StreamHandler",
            'formatter': "standard"
        },
        "console3":{
            'level':"ERROR",
            'class':"logging.StreamHandler",
            'formatter': "standard"
        },
        "file":{
            'level': "INFO",
            'class': "logging.FileHandler",
            'filename': "Logs/infos.log",
            'mode': "w",
            'formatter': "verbose"
        },
    },
    "loggers":{
        "bot":{
            'handlers': ['console'],
            "level": "INFO",
            "propagate": False
        },
        "discord":{
            'handlers': ['console2', "file"],
            "level": "INFO",
            "propagate": False
        }
        
    }
    
}


dictConfig(LOGGING_CONFIG)