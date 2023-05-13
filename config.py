import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "20960397"))
    API_HASH = os.environ.get("API_HASH", "d68d847d3abb2087bf74f5d0683c2993")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5706154290:AAHCL9yFFwoDNWWo0e03b-3mLSI-NSX5eVc")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "1327973537")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://vpcreatz:VPCREATION@cluster0.6lncjwt.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQAsphg_zN76KWlimM16KSKJM6cpnE-2Gl5doLiLOPVqm8dLgmLtKuQDfzTqWW5lmNoZT9LiHVmJ2XRSCICkgC427_aE8kT2dSLGEmCrn_y8rew4LLxsfnklJiTG2snOttgfC0iH6zFlokbxL8sfwy4XQotmMzaCuyGnAmMoF7ZlM5R3SwLwZsrT7d7zxK-AxhDO9ue93vI3Fo4_xyShvEvyAwnE0nqgA3p-Gkr-NiQE4R6pN87u0EXHgH5XVWwQmtDV9mFxe6tKPq-uy0hgUCjfAvYD2h7yDhytgm3vDsETQST8rFRfA9ybH0XkfmE_pU6JGnBuVzXZLZVmXlk1TyeNAAAAAVs9ne4A")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001290647385"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "autofilterimdbfiles_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
