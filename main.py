#!/usr/bin/env python
from client import initialize_client
from typing import Any
import serializers
import json
import sys

BOARD_ID = "W1MmHKBG"

def print_error(e: Exception):
    print(json.dumps(
        {
            "ok": False,
            "error": {
                "code": type(e).__name__,
                "message": str(e)
                }
            }
        )
    )

try:
    client = initialize_client()
except Exception as e:
    print_error(e)
    sys.exit(1)


def load_board():
    try:
        board = client.get_board(BOARD_ID)
    except Exception as e:
        print_error(e)
        sys.exit(2)

    return board
    
def get_board_data() -> dict[str, Any]:
    board = load_board()

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


def main() -> int:
    print(json.dumps(get_board_data()))
    return 0

if __name__ == "__main__":
    main()
