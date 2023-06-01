# Setup thing

# PAT=$(pass website/github/container_registry)

# podman login ghcr.io -u Findarato -p ${PAT}

# echo '[]' > podcasts.json

podman build --tag findarato/xandercasts:latest .

podman run --rm --name xandercasts findarato/xandercasts:latest


# podman push ghcr.io/findarato/xandercasts:amd64

# podman push ghcr.io/findarato/xandercasts:next

# podman push ghcr.io/findarato/xandercasts:latest

