#!/bin/env python

import json
import csv

def sanitize(value):
    return value.replace("\u201c", '"').replace("\u201d", '"').strip()

def to_json(value):
    return json.loads(value)

def sanitize_to_json(value):
    return to_json(sanitize(value))

cards = open("./RolplayCards.csv", encoding="utf8")
cards = csv.DictReader(cards, delimiter=";", quotechar="'")

items = []

for card in cards:
    id =  sanitize_to_json(card["id"])
    items.append({
        "id": id,
        "images": {
            "normal": f"{id}.jpg",
            "horizontal": f"{id}_h.jpg",
            "small": f"{id}_s.jpg"
        },
        "name": {
            "spanish": sanitize(card["name_es"]),
            "english": sanitize(card["name_en"])
        },

        "level": sanitize_to_json(card["level"]),
        "max_per_deck": sanitize_to_json(card["max_per_deck"]),
        "rarity": {
            "percent": sanitize_to_json(card["rarity_percent"]),
            "value": sanitize(card["rarity"])
        },
        "casting_cost": sanitize_to_json(card["casting_cost"]),
        "attack": sanitize_to_json(card["attack"]),
        "defense": sanitize_to_json(card["defense"]),
        "badges": {
            "left": sanitize(card["badge_left"]),
            "right": sanitize(card["badge_right"])
        },
        "class": sanitize(card["class"]),
        "kind": sanitize_to_json(card["kind"]),
        "type": sanitize(card["type"]),
        "subtype": sanitize(card["subtype"]),
        "abilities": {
            "main": sanitize_to_json(card["ability"]),
            "special": sanitize_to_json(card["special"]),
            "on_before_cast": sanitize_to_json(card["on_before_cast"]),
            "on_activate": sanitize_to_json(card["on_activate"]),
            "on_before_attack": sanitize_to_json(card["on_before_attack"])
        },
        "settings": sanitize_to_json(card["settings"])
    })


with open("./cards.json", "w") as file:
    file.write(json.dumps(items))