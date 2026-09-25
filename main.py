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
    
def get_board_data(board) -> dict[str, Any]:

    lists_data = []
    for list_index, trellist in enumerate(board.all_lists()):
        cards_data = []
    
        for card_index, card in enumerate(trellist.list_cards()):
            labels_data = []
    
            for label in card.labels:
                labels_data.append(serializers.serialize_label(label))
    
            cards_data.append(serializers.serialize_card_summary(card, card_index, labels_data))
    
        lists_data.append(serializers.serialize_list(trellist, list_index, cards_data))

    
    data = serializers.serialize_board(board, lists_data)

    return data

def get_card_by_id(id) -> dict[str, Any]:
    card = client.get_card(id)

    label_data = []
    comments = []
    
    for label in card.labels:
        label_data.append(serializers.serialize_label(label))
    
    for comment in card.get_comments():
        comments.append(serializers.serialize_comment(comment))

    card_data = serializers.serialize_card_detail(card, label_data, comments)

    return card_data

    
def main() -> int:


    
    # card = get_card_by_id("6ab4c75cd63992f70d839f34")

    # for comment in card.get_comments():
    #     print(json.dumps(comment))
    # print(json.dumps({
    #     "ok": True,
    #     "data": get_board_data(load_board())
    #     }))
    return 0

if __name__ == "__main__":
    sys.exit(main())
