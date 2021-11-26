import pyodbc
server = 'localhost'

bd = 'Estudiantes'


usuario = 'sa'
contrasena = 'Dayanara1814'

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; Server='+server+';database='+bd+';UID='+usuario+';PWD='+contrasena)
    print('conexion exitosa')


except :
    print('error al intentar conectarse')

#consulta a la base de datos

cursor = conexion.cursor()
cursor.execute("Select * from alumno;")

alumno = cursor.fetchall()

for usuario in alumno:
    print(usuario)

cursor.close()
conexion.close()
