# Setup thing

PAT=$(pass website/github/container_registry)

podman login ghcr.io -u Findarato -p ${PAT}

echo '[]' > podcasts.json

podman build --tag findarato/xandercasts:amd64 .

podman build --tag findarato/xandercasts:next .

podman build --tag findarato/xandercasts:latest .

podman push ghcr.io/findarato/xandercasts:amd64

podman push ghcr.io/findarato/xandercasts:next

podman push ghcr.io/findarato/xandercasts:latest

