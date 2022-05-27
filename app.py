from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # ここでindex.htmlを読み込んで表示
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)