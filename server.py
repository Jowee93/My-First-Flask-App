from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    signed_in = False
    return render_template('index.html', signed_in = signed_in)

# @app.route("/another")
# def show():
#     return "Yo"

@app.route('/user/<name>')
def show(name):
    name = name.upper()
    return render_template('index.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)