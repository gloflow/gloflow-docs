



# General protocol functions
- peers should be able to announce to each other which GF functions they support/have-enabled

# **Flow** Sharing/Discovery
- private flows belonging to a peer should only be discoverable by desired target peers
- public flows belonging to a peer should be broadcasted to the whole network of peers

# **Image sharing** between individual peers
- allow transfer of individual image files between peers that chose to exchange this data
- have flags on peer nodes that turns off this functionality on startup


# Image **Crawling** (Decentralized/Collective)
- should be prioritized since its the fastest way to rapidly expand the size of the image DB
- be able to synchronize between peers crawling of multiple domains
- handle a case where some max number of peers is crawling certain domains
    - avoid situations where too many crawlers crawl certain domains
    - have this max number be variable to account for some domains being very large, and some much smaller (and therefore needing much less crawling to cover in their entirity).
- share information between peers to prevent too many crawls of the same URL on some domain
    - possibly some amount of redundant crawling of a particular URL is beneficial to detect possibly fradulant/unfrendly crawlers that report URLs as crawled even though they're not.
- should crawling only fetch/permanently store images of reduced size, and redirect viewing users to full sized images on origin URL's (to remain fair to original content publishers)?
- look into Eth2 data sampling algos where availability of datasets can be verified by only explicitly checking availability of small subsets of data
    - use this to verify the validity of crawled data by crawling peers.
- have some scheme of sharing reputation/quality of domains
    - domains that provide unsutable content or in some way undersirable content should be marked as such and that state should be shared among peers

# **Reputation** of peers
- establish some sort of a reputation mechanism that is earned by peers by prolonged operation within the GF network.
- faulty or undesired actions by peers should decrease their reputation
- investigate keeping reputation as state on the Eth chain managed in smart-contracts
    - who would fund the TXs costs?
    - who would issue TXs to change reputation state?



# Release Schedule
- figure out a staged release of p2p functinality
    - prioritize various p2p functionality and aim for having at least some publicly usable functions as soon as possible.
    - come up with a operational set of instructions for minimaly technical node operators
        - ideally they should be able to just get a AWS/GCP/etc. node and do "docker run" to have a GF node up and running
- should the initial test-net of p2p nodes only be joinable by using some secret value manually supplied to trusted operators?
    - very primitive and naive approach but could be the simplest short-term approach