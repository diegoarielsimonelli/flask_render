from flask_sqlalchemy import SQLAlchemy

bd = SQLAlchemy()

class Estudiante(bd.Model):
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(100), nullable=False)
    email = bd.Column(bd.String(120), unique=True, nullable=False)
    edad = bd.Column(bd.Integer, nullable=False)

    def __init__(self, nombre, email, edad):
        self.nombre = nombre
        self.email = email
        self.edad = edad

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'edad': self.edad
        }
