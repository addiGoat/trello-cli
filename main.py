import enum

from trello import TrelloClient
from dotenv import load_dotenv
from typing import Any
import os
import json

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

BOARD_ID = "W1MmHKBG"
everything_board = client.get_board("W1MmHKBG")


def serialize_board(board, lists: list) -> dict[str, Any]:
    data = {
        "id": board.id,
        "name": board.name,
        "url": board.url,
        "lists": lists
    }
    return data

def serialize_list(list_object, index: int, cards: list) -> dict[str, Any]:
    data = {
        "id": list_object.id,
        "name": list_object.name,
        "position": index,
        "cards": cards
    }
    return data

def serialize_card(card, index: int, labels: list) -> dict[str, Any]:
    data = {
        "id": card.id,
        "name": card.name,
        "url": card.url,
        "position": index,
        "labels": labels 
    }
    return data

def serialize_label(label) -> dict[str, Any]:
    data = {
        "id": label.id,
        "name": label.name,
        "color": label.color
    }
    return data






lists_data = []
# im really sorry for this variable name
for index, trellist in enumerate(everything_board.all_lists()):
    cards_data = []

    for index, card in enumerate(trellist.list_cards()):
        labels_data = []

        for label in card.labels:
            labels_data.append(serialize_label(label))

        cards_data.append(serialize_card(card, index, labels_data))

    lists_data.append(serialize_list(trellist, index, cards_data))


board_data = serialize_board(everything_board, lists_data)

board_json = json.dumps(board_data)
print(board_json)

