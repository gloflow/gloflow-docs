





# IpfsDHT
- implementation of Kademlia with **S/Kademlia**, **Coral** and **mainlineDHT** modifications
    - used to implement the base Routing module
    - BitTorrent DHT spec - https://github.com/libp2p/specs/blob/master/kad-dht/README.md  
- https://github.com/libp2p/go-libp2p-kad-dht
- Distance  
    - XOR(sha256(key1), sha256(key2))  
- Replication Parameter *k*
    - amount of replication is governed by it  
    - recommended value for *k* is 20  
- Concurrency parameter *α*  
    - concurrency of node and value lookups are limited by this param  
    - default value of 3  
    - each lookup process can perform no more than 3 inflight requests, at any given time  
- Node ID  
    - spec - https://github.com/libp2p/specs/blob/master/peer-ids/peer-ids.md  
    - IDs are base58btc encoded (base58-bitcoin) - used to WIF for bitcoin address  

# *Client/Server* mode  
- **Server** mode  
    - unrestricted nodes; Internet, publicly routable nodes, e.g. servers in a datacenter  
    - nodes advertise the libp2p Kademlia protocol identifier via the *identify* protocol  
    - accept incoming streams using the Kademlia protocol identifier  
- **Client** mode 
    - restricted nodes; those with intermittent availability, high latency, low bandwidth, low CPU/RAM/Storage; non-publicly routable nodes, e.g. laptops behind a NAT and firewall.  
    - nodes do not advertise support for the libp2p Kademlia protocol identifier.  
    - nodes do not offer the Kademlia protocol identifier for incoming streams.  
- Nodes add another node to their routing table if and only if that node operates in server mode. 
    - allows restricted nodes to utilize the DHT (query the DHT), without decreasing the quality of the distributed hash table (without polluting the routing tables)  

# *Identify* protocol
- https://github.com/libp2p/specs/tree/master/identify  
- used to exchange basic information with other peers in the network, including addresses, public keys, and capabilities  
- 2 variations of the protocol:  
    - identify  
        - protocol id */ipfs/id/1.0.0*  
        - used to query remote peers for their information  
        - works by opening a stream to the remote peer you want to query, using */ipfs/id/1.0.0* as the protocol id string  
        - peer being identified responds by returning an Identify message and closes the stream   
        ```
        message Identify {
            optional string protocolVersion = 5;
            optional string agentVersion = 6;
            optional bytes publicKey = 1;
            repeated bytes listenAddrs = 2;
            optional bytes observedAddr = 4;
            repeated string protocols = 3;
        }
        ```
    - identify/push
        - protocol id */ipfs/id/push/1.0.0*  
        - used to inform known peers about changes that occur at runtime  
        - When a peer's basic information changes, for example, because they've obtained a new public listen address  

# related repos  
- DHT - github.com/libp2p/go-libp2p-kad-dht  
- KBUCKET - github.com/libp2p/go-libp2p-kbucket  
- MULTIADDRESS - github.com/multiformats/go-multiaddr


# Tools  
- libp2p-lookup
    - Small helper tool  
    - takes as input a peer ID or address and prints the output of the libp2p-identify protocol  
    - https://github.com/mxinden/libp2p-lookup  
- nebula  
    - https://github.com/dennis-tra/nebula  
    - A libp2p DHT crawler, monitor, and measurement tool that exposes timely information about DHT networks.  
    - https://discuss.libp2p.io/t/nebula-libp2p-dht-crawler/950  
    - DHT crawler that also monitors the liveness and availability of peers  
    - crawler connects to the standard DHT bootstrap nodes and then recursively follows all entries in their k-buckets until all peers have been visited  