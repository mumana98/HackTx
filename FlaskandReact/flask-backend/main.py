from flask import Flask, request, render_template
app = Flask(__name__)
import json
from pprint import pprint

@app.route("/")
def my_index():
    return render_template("index.html", token="Hello")
    #data = json.load(open('data.json'))
    #pprint(data)

@app.route("/test", methods=["POST"])
def test():
    return "hello"

@app.route("/pageTwo")
def page_two():
    return render_template("index.html", token="this is page 2")


if __name__ == "__main__":
    app.run(debug=True)

