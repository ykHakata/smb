from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!"

@app.route('/stboard/')
@app.route('/stboard/<name>')
def stboard(name=None):
    return render_template('stboard.html', name=name)

# 開発時のみ
app.run(debug=True)
