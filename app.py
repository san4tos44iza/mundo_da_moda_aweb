from flask import Flask, render_template, request, redirect
import MySQLdb

app = Flask(__name__)

db = MySQLdb.connect(
    host="127.0.0.1",
    user="root",
    passwd="labinfo",
    db="moda"
)

@app.route("/")
def paginaprincipal():
    return render_template("index.html")


@app.route("/paginaprincipal")
def index():
    return render_template("paginaprincipal.html")


@app.route("/registrar", methods=["POST"])
def registrar():
    nome = request.form["username"]
    email = request.form["email"]
    senha = request.form["password"]

    cursor = db.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
    usuario = cursor.fetchone()

    if usuario:
        return redirect("/paginaprincipal")

    sql = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
    valores = (nome, email, senha)

    cursor.execute(sql, valores)
    db.commit()

    return redirect("/paginaprincipal")


if __name__ == "__main__":
    app.run(debug=True)
