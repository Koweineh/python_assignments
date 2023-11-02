from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('check.html')

@app.route('/<x>/<y>')
def index1(x,y):
    return render_template('check.html',x=int(x),y=int(y))

if __name__ == "__main__":
    app.run(debug=True)
           