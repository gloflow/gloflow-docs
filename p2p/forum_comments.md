











https://github.com/libp2p/go-libp2p-kad-dht/issues/147





# libp2p DHT modes
- Well, it really query-only mode (mostly) versus full mode. The active side is actually the "client" (making requests), the "server" just responds to requests.  
- Given enough bad nodes, a DHT becomes unusable.  
- we have a ton of nodes behind NATs  
    1. Make outbound connections to insert themselves into the DHT.
    2. Cannot accept inbound connections, making it hard to actually traverse the DHT.
- nodes behind NATs won't be pingable (so they'll be dropped from routing tables pretty quickly).  
- clients are "passive" nodes, this is how it's done in BitTorrent.  
- DHT nodes that have just started may not provide particularly useful responses to some queries  

- https://github.com/libp2p/go-libp2p-kad-dht/issues/349
    - The DHT needs the ability to switch between server and client mode.  
        - If a peer becomes undialable for some reason, they should move to being only a client, but if a peer becomes dialable and suitable for being a full dht node, they should be able to without rebooting.


# libp2p functions to use:

> // returns the diversity stats for the Routing Table.  
> IpfsDHT.GetRoutingTableDiversityStats()  

> // allows introspection of the operation mode of the DHT  
> // Client & Server modes; Server mode allows for answering queries  
> IpfsDHT.Mode()  

> // looks for a peer with a given ID connected to this dht and returns the peer and the table it was found in  
> IpfsDHT.FindLocal(id peer.ID) peer.AddrInfo  

> host.Peerstore().Peers()

# AutoNAT



# libp2p RPC
- github.com/libp2p/go-libp2p-gorpc
- provides RPC support on top of libp2p in the same way that net/rpc does on HTTP


# Third-party tutorials
- https://ldej.nl/post/building-an-echo-application-with-libp2p/


# libp2p concepts
- Host
    - contains all the core functionalities you require connecting one peer to another  
    - contains *ID*, which is an identity of the peer  

- Stream
    - communication channel between two peers  
- Peerstore