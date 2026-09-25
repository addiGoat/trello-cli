from typing import Any

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
