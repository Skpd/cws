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
${VENV}/bin/python -m grpc_tools.protoc -I ./proto --python_out ./cws/ proto/client/client.proto
${VENV}/bin/python -m grpc_tools.protoc -I ./proto --python_out ./cws/ proto/stream/stream.proto
${VENV}/bin/python -m grpc_tools.protoc -I ./proto --python_out ./cws/ proto/markets/asset.proto
${VENV}/bin/python -m grpc_tools.protoc -I ./proto --python_out ./cws/ proto/markets/index.proto
${VENV}/bin/python -m grpc_tools.protoc -I ./proto --python_out ./cws/ proto/markets/pair.proto
${VENV}/bin/python -m grpc_tools.protoc -I ./proto --python_out ./cws/ proto/markets/market.proto

# fix imports. it looks like there is no way to change package name for output proto's externally,
# so we'll do that manually

for file in $(find ./cws -name '*_pb2.py'); do
    # regex code replace isn't a good idea, so we'll use at least full name
    sed -i 's/from client import client_pb2/from cws.client import client_pb2/g' ${file}
    sed -i 's/from markets import market_pb2/from cws.markets import market_pb2/g' ${file}
    sed -i 's/from markets import index_pb2/from cws.markets import index_pb2/g' ${file}
    sed -i 's/from markets import pair_pb2/from cws.markets import pair_pb2/g' ${file}
    sed -i 's/from markets import asset_pb2/from cws.markets import asset_pb2/g' ${file}
    sed -i 's/from stream import stream_pb2/from cws.stream import stream_pb2/g' ${file}
done
