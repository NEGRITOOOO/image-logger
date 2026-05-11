from flask import Flask, redirect

app = Flask(__name__)

@app.route('/api/image')
def serve_image():
    return redirect("https://i.im.ge/QMdVbq/token.png")
