
from flask import Flask,render_template,request, redirect,url_for,flash
from flask_mysqldb import MySQL

#inicializacion del servidor Flask
app= Flask(__name__)

#configuraciones para la conexion a BD
app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= ""
app.config['MYSQL_DB']= "dbflask"

app.secret_key='mysecretkey'

mysql= MySQL(app)


#Declaracion de rutas


# ruta se compone de nombre y funcion

# ruta Index http://localhost:5000
@app.route('/')
def index():
    curSelect= mysql.connection.cursor()
    curSelect.execute('select * from albums')
    consulta= curSelect.fetchall()
    #print(consulta)
    
    return render_template('index.html',listAlbums=consulta )





@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST':
        
        #guardamos en variables lo escrito en los Input
        Vtitulo= request.form['txtTitulo']
        Vartista= request.form['txtArtista']
        Vanio= request.form['txtAnio']
        
        #Conectamos y ejecutamos el Insert
        CS= mysql.connection.cursor()
        CS.execute('insert into albums(titulo,artista,anio) values(%s,%s,%s)',(Vtitulo,Vartista,Vanio))
        mysql.connection.commit()
    
    flash('Album Agregado Correctamente')    
    return redirect(url_for('index'))





@app.route('/eliminar')
def eliminar():
    return "Se Elimino"




# Ejecucion de servidor
if __name__== '__main__':
    app.run(port= 5000,debug=True)