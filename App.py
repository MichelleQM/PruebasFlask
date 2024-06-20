from flask import Flask, request, render_template, url_for, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdflask'

app.secret_key = 'millavesecreta'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('Home.html')

@app.route('/RegistrarMedico')
def RegistrarMedico():
    return render_template('RegistroMedico.html')

@app.route('/guardarMedico', methods=['POST'])
def guardarMedico():
    if request.method == 'POST':
        # Tomamos los datos que vienen por POST
        FNombreMedico = request.form['NombreMedico']
        FCedulaProfesional = request.form['CedulaProfesional']
        FRFC = request.form['RFC']
        FCorreo = request.form['Correo']
        FContra = request.form['Contra']
        FRol = request.form['Rol']
        
        # Enviamos a la BD
        cursor = mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO medicos (NombreMedico, CedulaProfesional, RFC, Correo, Contra, Rol) VALUES (%s, %s, %s, %s, %s, %s)',
            (FNombreMedico, FCedulaProfesional, FRFC, FCorreo, FContra, FRol)
        )
        mysql.connection.commit()
        
        flash('Registro exitoso')
        return redirect(url_for('RegistrarMedico'))

@app.errorhandler(404)
def paginanotfound(e):
    return 'Revisa tu sintaxis: No encontré nada', 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)

