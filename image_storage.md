








# Image **Storage**
- should peers that belong to the decentralized image store be required to store data on IPFS?
    - to take advantage of content addressing
    - to allow for replication of data accross IPFS nodes?
- IPFS backend for image storage should be prioritized
- crawler subsystem should be migrated to the Image storage abstraction layer as soon as possible.

- flow->backend(s3/ipfs/etc.) mapping should not be staticly defined (as currently it is via YAML config file), and instead it should be dynamically settable by node operators/users
    - possibly operators should be able to enable this for users on node-startup (if for example they want to force users to only use s3 storage, or IPFS, etc.)