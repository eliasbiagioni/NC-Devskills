
# NC-Devskills - Django

  

La aplicacion esta desarrollada utilizando Docker y Docker-compose.

Para levantar la aplicacion, primero se debe crear un archivo de variables de entorno *.env* y setear las variables necesarias (basarse en el archivo *.env.example*) . Luego, ejecutar los siguientes comandos:

- Despliegue de la aplicacion: `docker-compose up -d` . Esta, por defecto corre en el puerto 8000. En el caso de querer modificarlo, ingresar al archivo *docker-comopse.yml* y, en la seccion ***ports***, modificar el puerto de la izquierda. La base de datos utilizada es PostgreSQL y corre en el puerto 5432.
- Ejecucion de migraciones: `docker exec -i nc-devskills-web python3 manage.py migrate`
- Ejecucion de seed para inicializar la base de datos con datos de: 
	- Tipos de servicios y estados de pagos de una boleta de pago: `docker exec -i nc-devskills-web python3 manage.py shell < payables/seeder.py`
	- Metodos de pagos disponibles: `docker exec -i nc-devskills-web python3 manage.py shell < transactions/seeder.py` 

Para la prueba de los endpoints, dejo una coleccion de postman (*Devskills - Elias Biagioni.postman_collection.json*) en la que se encuentran las requests con ejemplos.