from trello import TrelloClient
from dotenv import load_dotenv
import os

class MissingConfig(Exception):
    pass

load_dotenv()

def initialize_client():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise(MissingConfig("Missing trello api key"))
    
    api_secret = os.getenv("API_SECRET")
    if not api_secret:
        raise(MissingConfig("Missing trello api secret"))
    
    app_token = os.getenv("APP_TOKEN")
    if not app_token:
        raise(MissingConfig("Missing trello app token"))

    return TrelloClient(
        api_key=api_key,
        api_secret=api_secret,
        token=app_token
    )
