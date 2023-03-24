# Comwork AI

Comwork AI API based on GPT-2

This API is publicly available here: https://cwai-api.comwork.io

## Git repositories

* Main repo: https://gitlab.comwork.io/oss/cwai/cwai-api.git
* Github mirror: https://github.com/idrissneumann/cwai-api.git
* Gitlab mirror: https://gitlab.com/ineumann/cwai-api.git

## Getting started in local

## Prepare configurations

```shell
cp .env.dist .env # replace your variables in the .env file you just created
```

## Run the containers

```shell
docker-compose -f docker-compose-local.yml up --build --force-recreate
```

Then you can open http://localhost:8000 and test the API via Swagger.

You can also test the prompt API like that:
