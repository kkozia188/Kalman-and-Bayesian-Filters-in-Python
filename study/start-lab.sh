#!/usr/bin/env bash
set -euo pipefail

study_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
if [[ ! -x "$study_root/.venv/bin/jupyter" ]]; then
    echo '请先按 study/README.md 中的说明安装学习环境。' >&2
    exit 1
fi

exec "$study_root/.venv/bin/jupyter" lab \
    --no-browser \
    --ip=127.0.0.1 \
    --port="${KALMAN_JUPYTER_PORT:-8888}" \
    --port-retries=0 \
    --ServerApp.root_dir="$study_root" \
    --ServerApp.default_url=/lab/tree/01-g-h-filter.ipynb \
    "$@"
