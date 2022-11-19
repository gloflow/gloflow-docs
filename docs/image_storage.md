







Image **Storage**
- should peers that belong to the decentralized image store be required to store data on IPFS?
    - to take advantage of content addressing
    - to allow for replication of data accross IPFS nodes?
- IPFS backend for image storage should be prioritized
- crawler subsystem should be migrated to the Image storage abstraction layer as soon as possible.

- flow->backend(s3/ipfs/etc.) mapping should not be staticly defined (as currently it is via YAML config file), and instead it should be dynamically settable by node operators/users
    - possibly operators should be able to enable this for users on node-startup (if for example they want to force users to only use s3 storage, or IPFS, etc.)


image storage:
    - this represents storage of image that is expected to be durrable in some way  
    - does not include temporary storage of images on the local FS (workspace)  

---
functions that do persistent image storage:  

GF_GIF_LIB  
    - gf_apps/gf_images_lib/gf_gif_lib/gf_gif.go  
        - Process_and_upload()  
        - gif__s3_upload_preview_frames()  
        - Gif__frames__save_to_fs()  

GF_IMAGES_CORE  
    - gf_apps/gf_images_lib/gf_images_core/gf_images_s3.go  
        - S3__store_gf_image()        - uploads both main GF transformed image  
        - S3__store_gf_image_thumbs() - uploads thumbs  

GF_IMAGES_JOBS_CORE  
    - gf_apps/gf_images_lib/gf_images_jobs_core/gf_jobs_pipeline.go  
        - job__pipeline__process_image_uploaded()  
        - job__pipeline__process_image_extern()  

GF_IMAGES_SERVICE  
    - gf_apps/gf_images_lib/gf_images_service/gf_image_upload.go  
        - S3__get_image_s3_filepath()  

GF_CRAWL_CORE  
    - gf_apps/gf_crawl_lib/gf_crawl_core/gf_crawl_images_flows.go  
        - S3__get_image_original_file_s3_filepath()  
        - S3__get_image_thumbs_s3_filepaths()  
        - S3storeImage()  

    - gf_apps/gf_crawl_lib/gf_crawl_core/gf_crawl_images_s3.go  
        - S3storeImage()  

---
functions that use local temporary workspace FS storage:  

GF_IMAGE_EDITOR  
    - gf_apps/gf_images_lib/gf_image_editor/gf_image_editor.go  
        - save_edited_image()  