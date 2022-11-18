









The goal is to abstract file operations. This is mainly relevant for the gf_images and gf_crawl applications, where files are downloaded either from the user or from remote url's.  
gf_images downloads images, operates on them (transforms them with filters or resizes them or reformats them,etc.), and then persists them on a FS. The FS abstraction layer will allow
for configurability so that these operations can be applied to:  
    - AWS S3  
    - GCP storage  
    - local FS  
    - IPFS  