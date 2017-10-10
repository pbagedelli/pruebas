# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    mensaje= "hola"
    return render_template("pagina.html", mensaje = mensaje)
if __name__ == '__main__':
    app.run()
