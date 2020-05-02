echo '[]' > podcasts.json

docker build --tag findarato/xandercasts:pi .

docker push findarato/xandercasts:pi

