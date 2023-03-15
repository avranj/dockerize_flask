from flask import Flask


app=Flask(__name__)

@app.route("/") #localhost:portnumber/home_page


def home():
    return "first application"


if __name__=="__main__":
    app.run(debug=True)