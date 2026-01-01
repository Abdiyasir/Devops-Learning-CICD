from flask import Flask
import redis


app = Flask(__name__)

# Connect to Redis
client = redis.Redis(host="redis", port=6379)


@app.route("/")
def welcome():
    return "Welcome to my Coderco Docker Project!"


@app.route("/count")
def count():
    visitor_count = client.incr("visitor_count")
    return f"You are Visitor number: {visitor_count}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)