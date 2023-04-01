#!/usr/bin/env bash

export ENV="prod"
export VERSION="${CI_COMMIT_BRANCH}-${CI_COMMIT_SHORT_SHA}"
export IMAGE_NAME="cwai_api"
export DEFAULT_MAX_LENGTH=100
export DEFAULT_NUM_RETURN_SEQUENCES=1
export DEFAULT_NO_REPEAT_NGRAM_SIZE=2
export DEFAULT_TOP_K=50
export DEFAULT_TOP_P="0.95"
export DEFAULT_TEMPERATURE="0.8"
