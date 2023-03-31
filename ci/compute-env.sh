#!/usr/bin/env bash

export ENV="prod"
export VERSION="${CI_COMMIT_BRANCH}-${CI_COMMIT_SHORT_SHA}"
export IMAGE_NAME="cwai_api"
export DEFAULT_MAX_LENGTH=50
export DEFAULT_NUM_RETURN_SEQUENCES=1
