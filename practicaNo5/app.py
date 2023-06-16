
from flask import Flask

#inicializacion del servidor Flask
app= Flask(__name__)

#configuraciones para la conexion a BD
app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= ""
app.config['MYSQL_DB']= "bdflask"




#Declaracion de rutas


# ruta se compone de nombre y funcion

# ruta Index http://localhost:5000
@app.route('/')
def index():
    return "Hola Mundo"

@app.route('/guardar')
def guardar():
    return "Se guardo el album en la BD"

@app.route('/eliminar')
def eliminar():
    return "Se Elimino"




# Ejecucion de servidor
if __name__== '__main__':
    app.run(port= 5000,debug=True)