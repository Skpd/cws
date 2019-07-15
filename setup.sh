#!/usr/bin/env bash

VENV="./venv"
# init virtual environment. use any python >= 3.6
python3.7 -m venv ${VENV}

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
