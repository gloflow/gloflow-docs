
# ALWAYS THINK BACK TO THE USER!!


# General protocol functions
- peers should be able to announce to each other which GF functions they support/have-enabled

# **Flow** Sharing/Discovery
- private flows belonging to a peer should only be discoverable by desired target peers
- public flows belonging to a peer should be broadcasted to the whole network of peers
- have a subset of users 

# **Image sharing** between individual peers
- allow transfer of individual image files between peers that chose to exchange this data
- have flags on peer nodes that turns off this functionality on startup


# Image **Crawling** (Decentralized/Collective)
- should be prioritized since its the fastest way to rapidly expand the size of the image DB
- be able to synchronize between peers crawling of multiple domains
- handle a case where some max number of peers is crawling certain domains
    - avoid situations where too many crawlers crawl certain domains
    - have this max number be variable to account for some domains being very large, and some much smaller (and therefore needing much less crawling to cover in their entirity).
    - some form of algo should be in place to auto-determine the frequency of update of certain domains (speed with which new image content is added to those domains) and that should then influence how frequntly the GF network should be instructed to re-crawl those domains.
- share information between peers to prevent too many crawls of the same URL on some domain
    - possibly some amount of redundant crawling of a particular URL is beneficial to detect possibly fradulant/unfrendly crawlers that report URLs as crawled even though they're not.
- should crawling only fetch/permanently store images of reduced size, and redirect viewing users to full sized images on origin URL's (to remain fair to original content publishers)?
- look into Eth2 data sampling algos where availability of datasets can be verified by only explicitly checking availability of small subsets of data
    - use this to verify the validity of crawled data by crawling peers.
- have some scheme of sharing reputation/quality of domains
    - domains that provide unsutable content or in some way undersirable content should be marked as such and that state should be shared among peers
- use some sort of partition scheme based on url's to sync work between nodes
- use some sort of ML autoencoder higher-level image representation (latent-space representation) to determine image similarty (and backoff from duplicate work between nodes) even though the image hashes might be different (and leading the algo to determine that they are unrelated images and are not duplicating work).
- use DHT to share state on what has already been crawled/processed by crawlers to avoid duplicate work.


# **Reputation** of peers / validation of peer-processing output
- establish some sort of a reputation mechanism that is earned by peers by prolonged operation within the GF network.
- faulty or undesired actions by peers should decrease their reputation
- investigate keeping reputation as state on the Eth chain managed in smart-contracts
    - who would fund the TXs costs?
    - who would issue TXs to change reputation state?
- Punishment system
    - use some kind of staking/stake-slashing system similar to Eth to punish users that process image in an invalid way?
- investigate Halochain as a validation solution
    - data integrity validation engine



# Release Schedule
- figure out a staged release of p2p functinality
    - prioritize various p2p functionality and aim for having at least some publicly usable functions as soon as possible.
    - come up with a operational set of instructions for minimaly technical node operators
        - ideally they should be able to just get a AWS/GCP/etc. node and do "docker run" to have a GF node up and running
- should the initial test-net of p2p nodes only be joinable by using some secret value manually supplied to trusted operators?
    - very primitive and naive approach but could be the simplest short-term approach


# Image Operations
- allow users to run image-processing workers in their browsers and receive jobs/shards of image datasets from the GF network
    - allow casual users to join the GF image processing network temporarily and only process without long-term commitments for a few hours or so and then leave the network.
    - investigate using Photon in the browser
        - https://github.com/silvia-odwyer/photon
- ultimately all image operations should be Rust based
    - cross-compiled to WebAssembly as well
    - executable in both the browser (by casual web users) and on the server (by powerful server farms and thirdparty companies)
    - Rust is callable from Py as well

# Filecoin integration
- lookin into it for incentivization for image file hosting by third-parties
- FVM
    - investigate to see if business-rules around file hosting can be developed or prototyped
    - proof-of-storage
    - proof-of-validity-of-computation
        - look into FVM and varifying computation and see if it applies to our problem of being able to validate compuite results for images that a peer/node recives back from a full-node/compute-node/node that execute some image operations on others behalf.
    - https://fvm.filecoin.io/
    - filecoin actors - GF should have a native Filecoin actor to run in the Filecoin network?
- dev-advocates are mentioning CDN/retreival networks being in the works; investigate this for image file serving
- possibly look into integrating with Filecoing (having support for it in the GF nodes), to have an avenue of allowing/supporting financial incentivization of file-storage (at least using the IPFS backend).

# p2p node keychain management
- goal is to have sensical key loading
- have integration with hardware keys for operatators to use to load secure key-pairs
- allow for loading of keypairs via ENV vars (even though not secure)
- integrate usage of AWS SecretsManager for loading in AWS environment
- provide backup logic-path for generating keys if none are supplied
- we should be able to load private keys from seed-phrases.
- possibly allow for people to use ssh-keys as their key-pair (bash key-gen utility)

# p2p peer discovery
- there is some delay in when old peer announcements in the DHT are garbage-collected
    - figure out how long this delay is
    - possibly create a simple tool for operators that can introspect the global DHT and check for garbage vs valid peers
- When a peer joins a DHT, it can use the key-value store to announce it presence and to find other peers in the network.
    - key used for announcing its presence is called the **rendezvous-point**

# Genesis event
- a moment in time when the first 2 nodes of the network start up
- does this event need to be managed in some special way
    - do we need to pick some initial values for the network via social consesus

# Bootstrap nodes
- currently the GF p2p test program uses the IPFS bootstrap nodes (same ones that the IPFS network uses and its clients)
- ultimatelly the GF network (community/foundations) should have its own set of geo-distribute bootstrap nodes. 
    - the GF public governing-body should run this core infra used by the whole network.
- hardcoded libp2p/ipfs bootstrap nodes seem to be defined in - https://github.com/libp2p/go-libp2p-kad-dht/blob/master/dht_bootstrap.go

# User/Peer Classes
- Full-clients vs Light clients
- important 2 major classes of nodes/peers in the network that behave differently.
- full clients are going to be long-running nodes, that will also satisfy various compute requests
- light-clients are going to be short lived nodes (users running GF nodes on their laptops for a few hours eveyry week) when the only for example want to view files/images and consume content (not satisfy compute requests).
    - look into the libp2p JS/browser impelementation to see if light-clients/peers can be run in a browser tab by certain users.

- potentially have storage-clients
    - clients/nodes that only store data/images, and cant do (or dont want to/dont advertise to be able to) conduct other operations (apply image filters/apply more comple image pipilens/apply ML piplines, etc)

- might have ML-clients
    - clients that can execute (or are willing) ML pipilines.

- build in this capability-level announcement process into the peer boostraping stage
    - when the peer first joins the network it announces which types of operations it is willing to satisfy/accept.

- some users of the GF network are not even peers
    - they are purely users that connect to some peer that serves the GF or any other UI from that server
    - those users (JS code in the browser) might only interact with the GF REST API, which then in turn would via the peer interface interact with the GF network.

# Blockchain
- Holochain (@kevin) - 
    - https://holo.host/whitepapers/
    - https://blog.holochain.org/real-p2p-networking-coming-to-holochain-rsm/