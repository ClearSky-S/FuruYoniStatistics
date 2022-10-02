#!/usr/bin/env bash

set -e

export GIT_LATEST_SHA=$(git rev-parse --verify HEAD)
echo $GIT_LATEST_SHA
