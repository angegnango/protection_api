## PROTECTOR API

Webservice in charge of http traffic base of FastAPI , Poetry and Docker

### DEPENDENCIES
  
  - [Python](https://www.python.org/downloads/) 
  - [Poetry](https://python-poetry.org/) 
  - [FastAPI](https://fastapi.tiangolo.com/)
  - [Docker](https://www.docker.com/)

### GETTINGS STARTED

  1 - Clone the repository
  ` git clone `

  2 - Install dependencies using Poetry
  ` poetry install `

  3 - Build docker image
  `  docker build -t datadome/protection_api .  `

  4 - Run the service
  `  docker run -p 8000:8000 datadome/protection_api `

Once thoses step done, your server will run in docker container available
at  ' http://localhost:8000 '

### API DOCUMENTATIONS

Homepage

![API HOMEPAGE](home.png)

---

Endpoints availables

![ENDPOINTS AVAILABLE](endpoints.png)

---
Request from unknow origin

![503 ERROR CODE](error.png)

---

---
> To launch the all stack , cart_api, datadome_module and protector_api dont use the docker commands above. a docker compose will be use to start all service
