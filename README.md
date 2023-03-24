# Comwork AI

Comwork AI API based on GPT-2

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
