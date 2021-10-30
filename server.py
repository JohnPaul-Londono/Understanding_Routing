from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<string:name>")
def names_page(name):
    # print(name)
    return f"Hi {name}!"

@app.route("/repeat/<int:num>/<string:word>")
def repeat_page(num, word):
    # print(num, word)
    output = ''

    for i in range(0,num):
        output += f"<p>{word}</p>"

    return output

if __name__=="__main__":
    app.run(debug=True)