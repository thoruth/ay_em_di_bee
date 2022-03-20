# Requirements

This demo was made in docker to install automatically the package, and to run a temporal PostgreSQL database.


But to run the notebooks locally, install the requirements.txt

In order to run, 
Docker and docker-compose needed. Install these softwares from
https://www.docker.com/get-started

Docker engine minimum version needed: 18.02.0+


# Boot up

```bash
docker-compose up --build
```
or
```bash
docker compose up --build
``` 
# Stop containers

```bash
docker-compose down --volumes
```
or
```bash
docker compose down --volumes
``` 


# Jupyter

The url for notebook is http://localhost:8888
The password is `password`

# Development

The implementation can be found in the magic_package folder.
To install locally:
```bash
cd magic_package
pip3 install .

# or dynamically
pip3 install -e .
``` 

# Development

To test, the package have to installed before hand

To run the unittest:
```bash
cd magic_package
pytest .
``` 

