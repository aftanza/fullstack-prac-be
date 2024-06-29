pushd %~dp0
docker compose down
docker compose build
docker compose up
popd