import os

from flask import Flask
from threading import Thread
app = Flask('')

port = os.environ.get('PORT', 10000)

@app.route('/')
def home():
  return "Webserver OK, Discord Bot OK"


def run():
  app.run(host="0.0.0.0", port=port)


def keep_alive():
  t = Thread(target=run)
  t.start()
