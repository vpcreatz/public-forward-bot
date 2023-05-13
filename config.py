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
    SESSION = os.environ.get("SESSION", "BQDFzD7GiX1djrIzxK5OQ-llnnNrcI-JAIMF1pY0zsLsU0PjzrxF4_RwonH6FK4WUosQoMdL2YYDnXeBIwRxYkWwaPv8VJ9f5qzAAFndSZ7UHafGe2Xt7LJa9nlKqWoZDUmbUTaFPS9uXSqjooBISUAW7ezTxrsX8f6VTx5rVIvhOFZ_dnqkMWcYAP7XZp6262EBSG67v5leUgmvXKU8WCHfbESqM487yE_cac-qz3ozTRTDfLiEa1dkSv03-kPXfwsEgUIlsh8zEa_lEs0eRjuH5UOWJZJ0mBOUt21CkSYDMI6CoGmtIEIUobngqmoyv55kaZdEbRVWpoMSbXXZ9qhTAAAAAVs9ne4A")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001290647385"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "autofilterimdbfiles_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
