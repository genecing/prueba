from flask import Flask, render_template
a = Flask(__name__)

@a.route("/Inicio")
def inicio():
        return render_template("Inicio.html")
    

@a.route("/Login")
def login():
        return render_template("Login.html")

@a.route("/Proyectos")
def proyectos():
        return render_template("Proyectos.html")

if __name__ == "__main__":
    a.run()
