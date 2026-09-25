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

def serialize_card_summary(card, index: int, labels: list) -> dict[str, Any]:
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

def serialize_comment(comment) -> dict[str, str]:
    author = comment["memberCreator"]
    data = {
        "id": comment["id"],
        "text": comment["data"]["text"],
        "created_at": comment["date"],
        "author": {
            "id": author["id"],
            "name": author["username"],
            "avatar_url": author["avatarUrl"]
        }
    }

    return data

def serialize_card_detail(card, labels: list, comments: list) -> dict[str, Any]:
    parent_list = card.get_list()

    data = {
        "id": card.id,
        "name": card.name,
        "description": card.description,
        "url": card.url,
        "list": {
            "id": parent_list.id,
            "name": parent_list.name,
            },
        "labels": labels,
        "comments": comments
    }
    return data














