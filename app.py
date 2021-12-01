from flask import Flask, request
import logging
import json
import random

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route('/', methods=["POST"])
def standard():
    logging.info(request.json)
    randon_nufro = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    text = request.json.get("request", {}).get("command")
    end = False
    if text == "выход":
        response_text = "Пока!"
        end = True
    elif text:
        response_text = f"Вы сказали {text}"
    else:
        response_text = "Вы таки ничего не сказали"
    response = {
        "response":{
            "text": response_text,
            "end_session": end,
            "buttons":[
                {
                    "title": "Нажми меня!",
                    "hide": True
                },
                {
                    "title": "выход",
                    "hide": True
                },
                {
                    "title": "Рандом цифр",
                    "hide": False,
                    "url": random.choice(randon_nufro)

                },
                {
                    "title": "Нажми на ссылку!",
                    "url": "https://www.youtube.com/watch?v=hiEM5rkx1XA",
                    "hide": True

                }

            ]
        },
        "version": "1.0"
    }

    return response
