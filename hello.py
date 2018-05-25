from flask import Flask, render_template
app = Flask(__name__)

# トップページ
@app.route("/")
def stboard(name=None):
    return render_template('stboard.html', name=name)

# 伝言板登録画面
@app.route('/create')
def stbcreate():
    return render_template('create.html')

# 開発時のみ
app.run(debug=True)
