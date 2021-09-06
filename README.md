# NaNLABS
ejercicio

# Descripción
Ejercicio de entrevista técnica.
- Generar api que reciba un json y cree tarjetas en Trello


## Requisitos

- pip3 
```bash
sudo apt-get install python3-pip
```
- virtualenv 
```bash
pip3 install virtualenv
```


## Instalación
 - crear carpeta del proyecto, ingresar a la misma
 - iniciar git 
```bash
git init
```
 - clonar repositorio
```bash
git clone https://github.com/BraianMilocco/NaNLABS.git
```
 - crear virtual enviroment
```bash
python3 -m venv
```
 - iniciar venv ()
```bash
source venv/bin/activate
``` 
- instalar dependencias (pip3 install -r requirements.txt)
```bash
pip3 install -r requirements.txt
```
- Exportar las variables de Ambiente (se encuentran en archivo enviado por mail)


## Correr
- Correr server
```bash
uvicorn main:app --reload
```

#### urls
 - api: http://127.0.0.1:8000/ (Devuelve informacion para hacer las requests)

 ### Recomendacion 
 - Usar Postman o algun programa similar para las requests

