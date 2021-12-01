from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/', methods=["POST"])
def standard():
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
                    "url": random.randrange(1,30,2),
                    "hide": True

                },
                {
                    "title": "Нажми на ссылку!",
                    "url": "https://www.google.by/maps/@54.9495832,26.3622858,13.75z?hl=ru",
                    "hide": True

                }

            ]
        },
        "version": "1.0"
    }
    return response
