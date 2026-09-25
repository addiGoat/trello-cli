from trello import TrelloClient
from dotenv import load_dotenv
from typing import Any
import serializers
import json
import sys
import os

BOARD_ID = "W1MmHKBG"
load_dotenv()

api_key = os.getenv("API_KEY")
if not api_key:
    raise(RuntimeError("No Api Key Found"))

api_secret = os.getenv("API_SECRET")
if not api_secret:
    raise(RuntimeError("No Api Secret Found"))

app_token = os.getenv("APP_TOKEN")
if not app_token:
    raise(RuntimeError("No App Token Found"))

client = TrelloClient(
    api_key=api_key,
    api_secret=api_secret,
    token=app_token
)

try:
    everything_board = client.get_board(BOARD_ID)
except Exception as e:
    error_data = {
            "ok": False,
            "error": {
                "code": type(e).__name__,
                "message": str(e)
                }
            }
    print(json.dumps(error_data))
    sys.exit(1)



def get_board_data(board) -> dict[str, Any]:
    lists_data = []
    for list_index, trellist in enumerate(board.all_lists()):
        cards_data = []
    
        for card_index, card in enumerate(trellist.list_cards()):
            labels_data = []
    
            for label in card.labels:
                labels_data.append(serializers.serialize_label(label))
    
            cards_data.append(serializers.serialize_card(card, card_index, labels_data))
    
        lists_data.append(serializers.serialize_list(trellist, list_index, cards_data))

    data = {
            "id": board.id,
            "name": board.name,
            "url": board.url,
            "lists": lists_data
            }
    return data


print(get_board_data)


# DONT DELETE ME THIS IS VERY IMPORTANT MAKE SURE YOU KEEP THIS CAUSE IT ACTUALLY WORKS
# lists_data = []
# for list_index, trellist in enumerate(everything_board.all_lists()):
#     cards_data = []
#
#     for card_index, card in enumerate(trellist.list_cards()):
#         labels_data = []
#
#         for label in card.labels:
#             labels_data.append(serializers.serialize_label(label))
#
#         cards_data.append(serializers.serialize_card(card, card_index, labels_data))
#
#     lists_data.append(serializers.serialize_list(trellist, list_index, cards_data))
#
# board_data = serializers.serialize_board(everything_board, lists_data)
#
# board_json = json.dumps(board_data)
# print(board_json)

