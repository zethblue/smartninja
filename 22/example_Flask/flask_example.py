from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/Superhero")
def superhero():
    return "Hello Superhero!"

if __name__ == "__main__":
    app.run()