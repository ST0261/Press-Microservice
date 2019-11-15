from Informative_Email.info_email_handler import press_router
from Month_Email.month_handler import press_router_month
from flask import Flask


app = Flask(__name__)           #Creating an App instance

app.register_blueprint(press_router)
app.register_blueprint(press_router_month)


@app.route("/")
def hello():
    return "Press server"

if __name__ == "__main__":      #On running python app.py
    app.run('0.0.0.0',debug=True)         #Run the flask App