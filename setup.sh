#!/usr/bin/env bash

./venv/bin/python -m grpc_tools.protoc -I ./proto --python_out ./ proto/client/client.proto
./venv/bin/python -m grpc_tools.protoc -I ./proto --python_out ./ proto/stream/stream.proto
./venv/bin/python -m grpc_tools.protoc -I ./proto --python_out ./ proto/markets/asset.proto
./venv/bin/python -m grpc_tools.protoc -I ./proto --python_out ./ proto/markets/index.proto
./venv/bin/python -m grpc_tools.protoc -I ./proto --python_out ./ proto/markets/pair.proto
./venv/bin/python -m grpc_tools.protoc -I ./proto --python_out ./ proto/markets/market.proto
