import requests
print("Leyendo un empleado")
apiUrl = "https://apiejemplos.azurewebsites.net/api/Empleados/7839"
response = requests.get(apiUrl)
#ESTO NOS DEVUELVE UNA RESPUESTA
#QUEREMOS EL JSON
jsonObject = response.json()
#ESTO ES UN OBJETO QUE PODEMOS ACCEDER A SUS PROPIEDADES
print("Apellido: " + jsonObject["apellido"])
print(jsonObject)
print("Fin de programa")

