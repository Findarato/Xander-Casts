# Setup thing

# PAT=$(pass website/github/container_registry)

# podman login ghcr.io -u Findarato -p ${PAT}

# echo '[]' > podcasts.json

podman build --tag findarato/xandercasts:latest .


podman build  -f "Dockerfile.book" -tag xandercasts-book:latest "." .

podman run --rm --name xandercasts_books \
    -e file='http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4' \
    findarato/xandercasts-book:latest

# podman run --rm --name xandercasts \
#     findarato/xandercasts:latest
# podman push ghcr.io/findarato/xandercasts:amd64

# podman push ghcr.io/findarato/xandercasts:next

# podman push ghcr.io/findarato/xandercasts:latest

