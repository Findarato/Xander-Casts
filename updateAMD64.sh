echo '[]' > podcasts.json

docker build --tag findarato/xandercasts:amd64 .

docker push findarato/xandercasts:amd64

