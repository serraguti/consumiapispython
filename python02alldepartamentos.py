import requests
print("Leyendo muchos departamentos")
apiUrl = "https://apiejemplos.azurewebsites.net/api/Departamentos"
response = requests.get(apiUrl)
departamentos = response.json()
#RECORREMOS TODOS LOS DEPARTAMENTOS 
for row in departamentos:
    numero = row["idDepartamento"]
    nombre = row["nombre"]
    localidad = row["localidad"]
    print(f"Numero: {numero}, Nombre: {nombre}, Localidad {localidad}")
print("Fin de programa")

    