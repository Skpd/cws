#!/usr/bin/env bash

BASE="$(dirname "$0")"
VENV="venv"
PYTHON_EX="python3.7"

cd ${BASE}

# init virtual environment. use any python >= 3.6
if [[ ! -d $VENV ]]; then
    ${PYTHON_EX} -m venv ${VENV}
else
    echo "Using already installed venv $VENV"
fi

# install python libraries
${VENV}/bin/pip install -r requirements.txt

# init proto submodule
git submodule init
git submodule update

# install / compile protocols
${VENV}/bin/python -m grpc_tools.protoc -I ./proto --python_out ./ proto/client/client.proto
${VENV}/bin/python -m grpc_tools.protoc -I ./proto --python_out ./ proto/stream/stream.proto
${VENV}/bin/python -m grpc_tools.protoc -I ./proto --python_out ./ proto/markets/asset.proto
${VENV}/bin/python -m grpc_tools.protoc -I ./proto --python_out ./ proto/markets/index.proto
${VENV}/bin/python -m grpc_tools.protoc -I ./proto --python_out ./ proto/markets/pair.proto
${VENV}/bin/python -m grpc_tools.protoc -I ./proto --python_out ./ proto/markets/market.proto
