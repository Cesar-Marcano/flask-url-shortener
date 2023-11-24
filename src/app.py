import secrets

from flask import Flask, request, jsonify, redirect, make_response
from error import MissingFieldError
from db import init, create_url, read_url

init()

app = Flask(__name__)

@app.post("/api/register-route")
def register_route():
    data = request.get_json()
    
    title = data.get('title')
    url = data.get('url')
    if not title or not url:
        raise MissingFieldError("Missing fields. Expected to receive: title: string; url: string;")
    
    slug = secrets.token_hex(6)
    
    create_url(title, url, slug)
    
    return make_response(jsonify({"slug": slug}), 201)


@app.get("/s/<slug>")
def shorten_url(slug):
    data = read_url(slug)
    
    return redirect(data[0], code=301)
    
    
@app.errorhandler(MissingFieldError)
def handle_body_missing_error(e):
    response = jsonify({'error': str(e)})
    response.status_code = 400
    return response


if __name__ == "__main__":
    app.run(debug=True)
