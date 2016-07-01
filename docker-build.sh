#!/usr/bin/env bash
set -e

\cp requirements.txt docker/web/
\cp -r website_technical_exercises/* docker/web/
cd docker
docker-compose up