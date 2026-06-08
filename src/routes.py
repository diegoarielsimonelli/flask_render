from flask import Blueprint, render_template, request, redirect, url_for
from models import bd, Estudiante

estudiantes_bp = Blueprint('estudiantes', __name__,url_prefix='/estudiantes')

# Leer todos (Ver info)
@estudiantes_bp.route('/')
def index():
    estudiantes = Estudiante.query.all()
    return render_template('index.html', estudiantes=estudiantes)

# Crear
@estudiantes_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        edad = request.form['edad']
        
        nuevo_estudiante = Estudiante(nombre=nombre, email=email, edad=edad)
        bd.session.add(nuevo_estudiante)
        bd.session.commit()
        return redirect(url_for('estudiantes.index'))
        
    return render_template('crear.html', estudiante=None)

# Editar / Actualizar
@estudiantes_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    estudiante = Estudiante.query.get_or_404(id)
    if request.method == 'POST':
        estudiante.nombre = request.form['nombre']
        estudiante.email = request.form['email']
        estudiante.edad = request.form['edad']
        
        bd.session.commit()
        return redirect(url_for('estudiantes.index'))
        
    return render_template('crear.html', estudiante=estudiante)

# Eliminar
@estudiantes_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    estudiante = Estudiante.query.get_or_404(id)
    bd.session.delete(estudiante)
    bd.session.commit()
    return redirect(url_for('estudiantes.index'))
