from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("exercise_home.html")

@app.route("/api/v1/<word>")
def about(word):
    temperature=23
    return {'definition' : word.upper(),
            'word' : word}

if __name__=="__main__":
    app.run(debug=True,port=5001)