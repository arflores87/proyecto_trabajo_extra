from flask import Flask
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def hello():
    app.logger.info("Request received")
    return "Aplicación DevSecOps funcionando en entorno local"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)