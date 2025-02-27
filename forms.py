from wtforms import Form, validators
from wtforms import StringField, PasswordField, EmailField, BooleanField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired, NumberRange

class UserForm(Form):
    matricula = IntegerField("Matricula", [
        validators.DataRequired(message='El campo es requerido')
    ])
    nombre = StringField("Nombre", [
        validators.DataRequired(message='El campo es requerido')
    ])
    apellido = StringField("Apellido", [
        validators.DataRequired(message='El campo es requerido')
    ])
    correo = EmailField("Correo", [
        validators.Email(message='Correo invalido')
    ])

class ZodiacoForm(Form):
    nombre = StringField("Nombre", [
        DataRequired(message='El campo es requerido')
    ])
    apellido = StringField("Apellido", [
        DataRequired(message='El campo es requerido')
    ])
    dia = IntegerField("Día", [
        DataRequired(message='El campo es requerido'),
        NumberRange(min=1, max=31, message='Día no válido')
    ])
    mes = IntegerField("Mes", [
        DataRequired(message='El campo es requerido'),
        NumberRange(min=1, max=12, message='Mes no válido')
    ])
    anio = IntegerField("Año", [
        DataRequired(message='El campo es requerido'),
        NumberRange(min=1910, max=2025, message='Año no válido')
    ])
    sexo = RadioField("Sexo", choices=[('M', 'Masculino'), ('F', 'Femenino')], 
                      validators=[DataRequired(message='El campo es requerido')])

class UserForm2(Form):
    id=IntegerField('id',
    [validators.number_range(min=1, max=20,message='valor no valido')])
    nombre=StringField('nombre',[
        validators.DataRequired(message='El nombre es requerido'),
        validators.length(min=4,max=20, message='requiere min=4 max=20')
    ])
   
    apaterno=StringField('apaterno',[
        validators.DataRequired(message='El apellido es requerido')
    ])
   
    email=EmailField('correo',[
        validators.DataRequired(message='El apellido es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])