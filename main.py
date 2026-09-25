from trello import TrelloClient
from dotenv import load_dotenv
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

board = client.get_board("W1MmHKBG")

board_output = {
        "ok": True,
        "data": {
            "id": board.id,
            "name": board.name,
            "url": board.url,
            "lists": [
                {
                    "id": "list_id",
                    "name": "Active",
                    "position": 2,
                    "cards": [
                        {
                            "id": "card_id",
                            "name": "Build a Trello desktop widget",
                            "url": "https://trello.com/c/...",
                            "position": 1,
                            "labels": [
                                { "id": "label_id", "name": "Quickshell", "color": "blue" }
                                ]
                            }
                        ]
                    }
                ]
            }
        }

# print("<Board name: ", board.name, ">")

lists_data = []
for list in board.all_lists():
    cards_data = []
    for card in list.list_cards():
        labels_data = []
        for label in card.labels:
            labels_data.append({
                "id": label.id,
                "name": label.name,
                "color": label.color
            })
        cards_data.append({
            "id": card.id,
            "name": card.name,
            "url": card.url,
            "position": card.pos,
            "labels": labels_data 
        })
    lists_data.append({
        "id": list.id,
        "name": list.name,
        "position": list.pos,
        "cards": cards_data
    })

board_data = {
        "ok": True,
        "data": {
                "id": board.id,
                "name": board.name,
                "url": board.url,
                "lists": lists_data
            }
        }

board_json = json.dumps(board_data)
print(board_json)

