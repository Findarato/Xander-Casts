
docker build --tag findarato/xandercasts:amd64 .

docker build --tag findarato/xandercasts:next .

docker build --tag findarato/xandercasts:latest .

docker push findarato/xandercasts:amd64

docker push findarato/xandercasts:next

docker push findarato/xandercasts:latest

