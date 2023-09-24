## PROTECTOR API

Webservice in charge of http traffic base of FastAPI , Poetry and Docker

### DEPENDENCIES
  
  - [Python](https://www.python.org/downloads/) 
  - [Poetry](https://python-poetry.org/) 
  - [FastAPI](https://fastapi.tiangolo.com/)
  - [Docker](https://www.docker.com/)

### GETTINGS STARTED

  1 - Clone the repository
  ` git clone git@github.com:angegnango/protection_api.git`

  2 - Install dependencies using Poetry
  ` poetry install `

  3 - Build docker image
  `  docker build -t datadome-protection-api-image .  `

  4 - Run the service
  `  docker run -p 8000:8000 datadome-protection-api-image `

Once thoses step done, your server will run in docker container available
at  ' http://localhost:8000 '

Once thoses step done, all your webservice will run 

- Protector API homepage available here -> http://localhost:8000
- API Documentation avalaible here -> http://localhost:8000/docs

### TESTS

Homepage

![API HOMEPAGE](home.png)

---

Endpoints availables

![ENDPOINTS AVAILABLE](endpoints.png)

---
Request from unknow origin

![503 ERROR CODE](error.png)

