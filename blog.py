from flask import Flask
app = Flask(__name__)

# decorator handles the complicated backend stuff
@app.route("/")
def hello():
    return "<h2>Home Page</h2>"


if __name__ == "__main__":
    app.run(debug=True)