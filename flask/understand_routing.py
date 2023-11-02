from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/Dojo')
def Dojo():
    return "Dojo"


@app.route('/say/<word>')
def say(word):
    return f"HI +  {word}"

    
    
@app.route('/repeat/<num>/<word>')
def repeat(num,word):
    return f"{word}" * int(num)

if __name__ == '__main__':
    app.run(debug=True)
    
    