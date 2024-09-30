import logging
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s, %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_endpoint(endpoint_name):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info(f"{timestamp}, {endpoint_name} endpoint was reached")


@app.route('/status')
def healthcheck():
    log_endpoint('/status')
    return jsonify({"result": "OK - healthy"}), 200


@app.route('/metrics')
def metrics():
    log_endpoint('/metrics')
    return jsonify({
        "status": "success",
        "code": 0,
        "data": {
            "UserCount": 140,
            "UserCountActive": 23
        }
    }), 200


@app.route("/")
def hello():
    log_endpoint('/')
    return "Hello World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')