

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

# p2p libp2p attacks
**Sybil Attacks**
- https://docs.libp2p.io/concepts/security-considerations/#sybil-attacks  
- one operator spins up a large number of DHT peers with distinct identities to flood the network  
- By controlling a large number of Sybil nodes (in proportion to the size of the network), a bad actor increases the probability of being in the lookup path for queries. 
    - routing table posining
- To target a specific key, they could improve their chances of being in the lookup path further by generating IDs that are “close” to the target key according the DHT’s distance metric  
- Applications can guard against modification of data by:  
    - detect if the data has been tampered with  
        - signing values that are stored in the DHT  
        - using content addressing, where a cryptographic hash of the stored value is used as the key, as in IPFS  
       
- investing doing PoW calculation on peer joining the network, just to prevent malicious actors from joning too many of their agents too rapidly. StorJ does this.  
    - S/Kademlia extensions
- encrypting values stored in a peer using that peers prviate key, and then other peers that consume that value decrypt it using that peers node ID. this way constitency of values stored by peers with given node IDs can be assured.


**Eclipse attacks**
- uses a large number of controlled nodes
- targeted at a specific peer with the goal of distorting their “view” of the network