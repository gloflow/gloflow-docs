



GloFlow is using the Go-lang **libp2p** implementation.  
https://github.com/libp2p/go-libp2p

 
supported libp2p transports:  
| protocol       | libp2p package    | status      |
| -------------- | ----------------- | ----------- |
| **TCP**        | libp2p-tcp        | (primary)   |
| **WebSockets** | libp2p-websockets | (secondary) |  





supported capabilities:
- NAT traversal
    - libp2p-circuit-relay-v2
    - libp2p-autonat
    - libp2p-hole-punching
- Secure communication
    - libp2p-tls
- Discovery
    - bootstrap
- Protocols
    





Peer identity:  
- **PeerId**:
    - each peer is given a globaly unique name
    - verifiable link between peer and their public key (peer_id is a hash of pub-key)
    - can be used in combination with peer public-keys to verify peer identity (authentication)
    - its a multi-hash
    - each peer controls a private key
        - how are we generating this private key on each peer?
        - how are we storing it on each peer?


Muliaddress
- encoding multiple layers of addressing into a single path structure
- multiaddress includes peerID, public IP of some sort, port number, transport protocol to be used.


Connection encryption
- all connections between peers are encrypted
- peer private-keys are used for encryption, and can be verified to come from that peer via its public-key
- encryption of connections assures among other things that if relay-peers are used (peers that relay data between multiple other peers) they cannot read relayed data.
 
Peer Store
- each peer has this temporary store
- holds a list of known peers that a particular peer is connected to
- should be persisted on peer shutdown to avoid having to rediscover peers on each startup

Authorization
- libp2p does not implement this part of security
- GF will need to implement a authorization mechanism to verify peers are permited to interact with particular data and conduct actions.

Protocols:
- protocol handlers
    - functions that handle data incoming for a particular protocol ID
- protocol negotiation
    - listening peer on the other end will check the incoming protocol id against the registered protocol handlers


