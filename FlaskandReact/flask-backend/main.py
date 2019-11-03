from flask import Flask, request, render_template
app = Flask(__name__)
 
@app.route("/")
def my_index():
    return render_template("index.html", token="Hello")

if __name__ == "__main__":
    app.run(debug=True)

