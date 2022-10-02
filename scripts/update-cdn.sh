#!/usr/bin/env bash

set -e

cat > .env << EOF
JSDELIVR_CDN_HASH=$(git rev-parse --verify HEAD)
EOF
