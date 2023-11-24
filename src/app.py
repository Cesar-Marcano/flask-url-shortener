from flask import Flask, request, jsonify
from error import MissingFieldError
from db import init

init()

app = Flask(__name__)

@app.post("/api/register-route")
def register_route():
    data = request.get_json()
    
    title = data.get('title')
    url = data.get('url')
    if not title or not url:
        raise MissingFieldError("Missing fields. Expected to receive: title: string; url: string;")
    
    return "hello world"
    
    
@app.errorhandler(MissingFieldError)
def handle_body_missing_error(e):
    response = jsonify({'error': str(e)})
    response.status_code = 400
    return response


if __name__ == "__main__":
    app.run(debug=True)
