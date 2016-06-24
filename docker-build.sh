#!/usr/bin/env bash
set -e

\cp requirements.txt docker/web/
\cp -r website-technical-exercises/* docker/web/
cd docker
docker-compose up