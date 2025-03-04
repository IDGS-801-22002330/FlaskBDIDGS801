from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask import g
from config import DevelopmentConfig
import forms

from models import db, Alumnos  # Import db and Alumnos correctly

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)  # Initialize CSRFProtect with the app

@app.route("/", methods=["GET", "POST"])
@app.route("/index")
def index():
    create_forms = forms.UserForm2(request.form)
    alumno=Alumnos.query.all()
    return render_template("index.html", form=create_forms, alumnos=alumno)
    return render_template("index.html")

@app.route("/detalles",methods=["GET", "POST"])
def detalles():
    if request.method=="GET":
        id=request.args.get("id")
        alum=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        id=request.args.get("id")
        nombre=alum.nombre
        apaterno=alum.apaterno
        email=alum.email
    return render_template("detalles.html", id=id, nombre=nombre,apaterno=apaterno,email=email, alum=alum)

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    alumno_form = forms.AlumnosForm(request.form)
    if request.method == "POST" and alumno_form.validate():
        alumno = Alumnos(nombre=alumno_form.nombre.data,
                         apaterno=alumno_form.apaterno.data,
                         amaterno=alumno_form.amaterno.data,
                         email=alumno_form.email.data,
                         date=alumno_form.date.data)
        db.session.add(alumno)
        db.session.commit()
        flash("Alumno registrado correctamente", "success")
        return redirect(url_for("alumnos"))

    alumnos = Alumnos.query.all()
    return render_template("alumnos.html", form=alumno_form, alumnos=alumnos)

@app.route("/eliminar", methods=["GET", "POST"])
def eliminar():
    alumno_form = forms.AlumnosForm(request.form)
    if request.method == "GET":
        id = request.args.get("id")
        alumno = Alumnos.query.get(id)
        alumno_form.id.data = request.args.get("id")
        alumno_form.nombre.data = alumno.nombre
        alumno_form.apaterno.data = alumno.apaterno
        alumno_form.amaterno.data = alumno.amaterno
        alumno_form.date.data = alumno.date
        alumno_form.email.data = alumno.email
        return render_template("eliminar.html", form=alumno_form)
    if request.method == "POST":
        id = alumno_form.id.data
        alumno = Alumnos.query.get(id)
        db.session.delete(alumno)
        db.session.commit()
        return redirect(url_for("alumnos"))

@app.route("/actualizar", methods=["GET", "POST"])
def actualizar():
    alumno_form = forms.AlumnosForm(request.form)
    if request.method == "GET":
        id = request.args.get("id")
        alumno = Alumnos.query.get(id)
        alumno_form.id.data = request.args.get("id")
        alumno_form.nombre.data = alumno.nombre
        alumno_form.apaterno.data = alumno.apaterno
        alumno_form.amaterno.data = alumno.amaterno
        alumno_form.date.data = alumno.date
        alumno_form.email.data = alumno.email
        return render_template("actualizar.html", form=alumno_form)
    if request.method == "POST":
        id = alumno_form.id.data
        alumno = Alumnos.query.get(id)
        alumno.nombre = alumno_form.nombre.data
        alumno.apaterno = alumno_form.apaterno.data
        alumno.amaterno = alumno_form.amaterno.data
        alumno.date = alumno_form.date.data
        alumno.email = alumno_form.email.data
        db.session.add(alumno)
        db.session.commit()
        return redirect(url_for("alumnos"))

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
    app.run()