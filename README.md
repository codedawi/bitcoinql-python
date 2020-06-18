# bitcoinql-python
GraphQL interface on top of `bitcoind` and `lnd` implemented in python.

## `bitcoind`
bitcoind provides a full peer which you can interact with through RPCs to port `8332` (or `18332` for testnet)

[RPC Documentation](https://developer.bitcoin.org/reference/rpc/index.html)

## `lnd`
lnd stands for *Lightning Network Daemon* and serves as the main software component driving the Lightning Network. gRPC is the preferred programmatic way to interact with lnd. It includes simple methods that return a response immediately, as well as response-streaming and bidrectional streaming methods.

[gRPC Documentation](https://api.lightning.community/#lnd-grpc-api-reference)
