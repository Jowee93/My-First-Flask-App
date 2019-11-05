from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Why so easy"

@app.route("/another")
def show():
    return "Yo"




if __name__ == "__main__":
    app.run(debug=True)