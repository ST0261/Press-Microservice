from flask import Flask
app = Flask(__name__)           #Creating an App instance

@app.route("/")
def hello():
    return "Hello World of mine"


@app.route("/<name>")
def hello_with_name(name):
    return ("Hello " + name)

if __name__ == "__main__":      #On running python app.py
    app.run(debug=True)         #Run the flask App

