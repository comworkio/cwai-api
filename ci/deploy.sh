#!/usr/bin/env bash

source ./ci/compute-env.sh

ENV_FILE=".env.${ENV}"

echo "VERSION=${VERSION}" > "${ENV_FILE}"
echo "MAX_LENGTH=${MAX_LENGTH}" >> "${ENV_FILE}"
echo "NUM_RETURN_SEQUENCES=${NUM_RETURN_SEQUENCES}" >> "${ENV_FILE}"

docker login "${CI_REGISTRY}" --username "${CI_REGISTRY_USER}" --password "${CI_REGISTRY_PASSWORD}"
docker-compose -f "docker-compose-${ENV}.yml" up -d --force-recreate
