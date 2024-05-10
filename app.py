#imports
# from my_model_inf import get_response
from flask import Flask, render_template, request

app = Flask(__name__)

#define app routes
@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get")
#function for the bot response
def get_bot_response():
    messageText = request.args.get('msg')
    print("messageText:",messageText)
    # output = get_response(messageText)
    output = "hello there"
    return output

if __name__ == "__main__":
    app.run(debug=True)
