

# distributed hash table
- https://en.wikipedia.org/wiki/Kademlia  
- https://medium.com/coinmonks/a-brief-overview-of-kademlia-and-its-use-in-various-decentralized-platforms-da08a7f72b8f
- https://en.wikipedia.org/wiki/Distributed_hash_table

# nodes
- nodes communicate among themselves using UDP  
- each node is identified by a **node ID** (160bit hash - SHA-1)  
    - The 160-bucket array routing table layout is a simplified approached for the proof of the paper, later revisions introduce a more sophisticated tree-based table  
- libp2p uses the base58btc encoding to encode the multiaddre into a node ID hash
- node ID provides a direct map to file hashes  
- each node in the network is a leaf in a binary-tree, placed according to the binary representation of their node ID.  
    - tree leaves are **k-buckets**  
        - they are a list of routing addresses of other nodes in the network  
        - contain the IP address, port, and node ID  
        - they prefer the longest-lived nodes  
        - *k* is the max number of nodes represented in a bucket  
- node position is determined by the shortest unique prefix of its ID  
- Each Kademlia node keeps a list of n *k*-buckets, where *n* is the number of bits in a key/node ID  

# k/v store  
- each value is stored at the k nodes whose node IDs are closest to the key ID  

# scaling
- Kademlia contacts only *O(log(n))* nodes during the search out of a total of *n* nodes in the system  
- distance is expressed as log2(n) of nodes number  
- for a netwrok of 10M nodes only about 20 hops are needed at most to communicate with any subset of nodes.  

# routing table  
- its distributed  
- each node keeps a mapping (its own routing table) for a subset of nodes in the network  
- if a loss of a group of nodes the algo/network routes around the unavailable nodes  
- peers can join by discovering just one other peer  
    - peer broadcasts its appearance  
    - peer then collects the node ID from each response and adds it to its peer-table.  
- nodes maintain detailed knowledge of address space close to them; exponentially decreasing knowledge of more distant address space.  
- asymptotically bounded by O(log2(n/k))  
    - *n* - actual number of nodes in the network  
    - *k* - bucket size  
        - larger bucket implementations slightly reduce the total number of buckets in the routing table.  
        - does the bucket size have to be consistent accross the whole network?
            - does the network have to reach consensus on the k-bucket dynamically or is it set at network boot?


# XOR metric  
- how distance is defined between points in the key-space  
- given two 160bit node IDs the distance between them is defined as the XOR of those 2 IDs.  


# long-lived nodes  
- network prefers them over short-lived nodes (new entrants)  
- algo assumes that the longer the nodes have been alive the more likely they are to remain online in the future.  
- concept of node churn leads to the desire to minimize network repair cost.  
- one cannot overtake a ndoes routing state by flooding the network with new nodes.  


# RPC protocol  
- message types  
    - PING - probes the node to see if its online  
    - STORE - instructs the node to store a k/v pair  
    - FIND_NODE  
        - takes a 160-bit key as an argument  
        - recipient of the FIND_NODE RPC returns an (IP address, UDP port, Node ID) tuple for each of the k nodes closest to the target id  
    - FIND_VALUE  
        - returns the k nodes closest to the target identifier  
        - if the RPC recipient has received a STORE for the given key, it returns the stored value  

# S/Kademlina
- secure key-based routing protocol based on Kademlia
    - using parallel lookups over multiple disjoint paths
    - limiting free nodeld generation with crypto puzzles
    - introducing a reliable **sibling broadcast**
- https://git.gnunet.org/bibliography.git/plain/docs/SKademlia2007.pdf

# var  
- nodes issue parallel queries to the network to prevent timeout delays  
- good visualization of Kademlia protocol - https://kelseyc18.github.io/kademlia_vis/basics/1/  
- some sort of network tracing/hop-counting tool should exist (@kevin)
    - to count the number of hops for example in a FIND_NODE network query
    - look into periodically running various FIND_NODE/FIND_VALUE queries for various keys to maybe see how the values change (how often the values change) (for some really common keys or keys that have system/network relevance/importance) or how often they change.
        - cardinality of the set of values of various reserved/system keys
    - run the XOR metric periodiocally on all discover peers (over time) and measure their distance over time to see on average (statisticlly) how those distance are distribute.
        - is it a normal-distribution
        
# used by projects:  
- **Ethereum**  
- **IPFS**  
- StorJ  
- BitTorrent  
- Swarm  

# libp2p implementation
- IpfsDHT is an implementation of Kademlia with **S/Kademlia**, **Coral** and **mainlineDHT** modifications
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
- **Client/Server** mode  
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