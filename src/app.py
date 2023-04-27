from flask import Flask

print("name", __name__)
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, world!"


if __name__ == "__main__":
    app.run()
