from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

# @app.route("/another")
# def show():
#     return "Yo"

@app.route('/user/<username>')
def show(username):
    return f"Hi {username[2]}"


if __name__ == "__main__":
    app.run(debug=True)