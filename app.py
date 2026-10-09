import os
from dotenv import load_dotenv

from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "pedrito-clavo-un-clavito")

#conexion a la base de datos
def conectar():
    conexion = sqlite3.connect("usuarios.db")
    conexion.row_factory = sqlite3.Row
    return conexion




def crear_tabla():
    with conectar() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        """)

@app.route("/")
def inicio():
    return redirect(url_for("login"))


#  nuevos usuarios
@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        usuario = request.form["usuario"].strip()
        password = request.form["password"]

    
        if len(usuario) < 3 or len(password) < 9:
            flash("Usuario minimo 3 caracteres y contraseña minimo 9.")
            return redirect(url_for("registro"))


    

        # Aqui es donde empieza hash 


        hash_password = generate_password_hash(password)
        try:
            with conectar() as db:
                db.execute(
                    "INSERT INTO usuarios (usuario, password_hash) VALUES (?, ?)",
                    (usuario, hash_password),
                )
        except sqlite3.IntegrityError:
            flash("Ese usuario ya existe.")
            return redirect(url_for("registro"))

        flash("Cuenta creada. Ya puedes iniciar sesion.")
        return redirect(url_for("login"))


    return render_template("registro.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"].strip()
        password = request.form["password"]

        #bloque para buscar al usuario en la basee datos
        with conectar() as db:
            fila = db.execute(
                "SELECT * FROM usuarios WHERE usuario = ?", (usuario,)
            ).fetchone()
        if fila and check_password_hash(fila["password_hash"], password):
            session["usuario"] = fila["usuario"]
            return redirect(url_for("logueado"))

        flash("Usuario o contraseña incorrectos.")
        return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logueado")
def logueado():
    if "usuario" not in session:
        return redirect(url_for("login"))
    return render_template("logueado.html", usuario=session["usuario"])




@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    crear_tabla()
    app.run(debug=True)