# API REST Demo

Demo de una API REST utilizando el framework fastapi

- [API REST Demo](#api-rest-demo)
	- [Ejecutar con Docker](#ejecutar-con-docker)
		- [Crear la imagen](#crear-la-imagen)
		- [Correr la imagen](#correr-la-imagen)
	- [Ejecutar localmente](#ejecutar-localmente)
		- [Acceder a la documentación](#acceder-a-la-documentación)
		- [Instalar bibliotecas](#instalar-bibliotecas)
		- [Iniciar aplicación](#iniciar-aplicación)
		- [Acceder a la documentación](#acceder-a-la-documentación-1)

## Ejecutar con Docker
### Crear la imagen
```sh
$ docker build -t api_demo1 .
```

### Correr la imagen
Puede elegir el puerto que le acomode (en el ejemplo 8084)
```sh
$ docker run -d -p 8084:80 api_demo1
```

## Ejecutar localmente
### Acceder a la documentación
```
http://localhost:8084/docs
```

### Instalar bibliotecas
```sh
$ pip install -r requirements.txt
```

### Iniciar aplicación
```sh
$ python run.py
```

### Acceder a la documentación
```
http://localhost:8000/docs
```
