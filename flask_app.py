from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "<p>Hello world!</p>"

if __name__ == "main":
    app.run(port=5000,debug=True)
