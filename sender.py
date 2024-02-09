from flask import Flask
from logging.config import dictConfig
from flask import request
import multiprocessing

from multicast.sender import send_message

def setup_logging():
    return dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })
  
setup_logging()

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev',
)

@app.route('/health')
def health():
    return {'message':'OK'}

@app.route("/send_mc", methods=["POST"])
def send():
    data = request.get_json()
    call_process = multiprocessing.Process(target=send_message, args=(data,))
    call_process.start()
    return {'message':'OK'}, 200
