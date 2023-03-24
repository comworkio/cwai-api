#!/usr/bin/env bash

export ENV="prod"
export VERSION="${CI_COMMIT_BRANCH}-${CI_COMMIT_SHORT_SHA}"
export IMAGE_NAME="cwai_api"
