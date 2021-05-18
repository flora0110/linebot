from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import urllib.request as req
import bs4
import json
import collections
from ..college_project.gossipg import sample_func

app = Flask(__name__)

line_bot_api = LineBotApi('Jc+EHqvTL5jUcUL64J9GLzz8ttcXAjVjs4dCGKvZy8miPrfBEAPKbN6Kj2aCU9wCgS199Pyq7jNO8cvxF0FnAPpJjwY4Yy9XkL7QW6Q0Pofylf38z8i6apcmZIiH5qfaBYSKz9uZkwN9DuTWeA2IRQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('39fc6bc55cf3cc986e23208f683e7140')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print("Request body: " + body, "Signature: " + signature)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #crawl(https://www.ptt.cc/bbs/Gossiping/index.html)
    sample_func()
    #print("Handle: reply_token: " + event.reply_token + ", message: " + event.message.text)
    content = "{}: {}".format(event.source.user_id, event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=content))

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
