echo '[]' > podcasts.json

docker build --tag findarato/xandercasts:amd64 .

docker build --tag findarato/xandercasts:next .

docker push findarato/xandercasts:amd64

docker push findarato/xandercasts:next

