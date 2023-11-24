from flask import Flask
from db import init

init()

app = Flask(__name__)

@app.get("/")
def index():
    return "hi"

if __name__ == "__main__":
    app.run(debug=True)
