





## Core Applications 

# gf_solo
- monolith that compils all the sub-apps into a single package - (gf_images/gf_publisher/gf_analytics/etc.).  
- it is built into a single Docker container, and meant to be used by power-users on their personal machines or servers.  

# gf_images  
- main application, responsible for working with images. this application contains its own HTTP handlers for REST API endpoints for adding images to the system. it also contains functions for working with Image Flows (which are collections of images). this application has several sub-packages:  
    - **gf_gif_lib** - this is responsible for working with GIF files.  
    - **gf_image_editor** - collection of functions for saving versions of images (versions that were edited). Image filters are for now appliced on the front-end in JS code, in the browser, but in the future we need to move to applying filters on the backend as well since we can scale and be much more performant there for really large images (or for less powerful.  
    - **gf_images_jobs** - this is the main image operations image manager, parallel process that applies various image transformation to potentially large collections of images. This is purely Go for now, but Rust will be plugged in here as well for the most performant operations.  
    - **gf_images_stats** - for now just a few simple image statistics function that collection some aggregate metrics from the DB  
    - **gf_images_core**  - various image functions used by both the gf_images application, and other applications (gf_publisher, gf_crawl, etc.)  

# gf_publisher
- publishing posts that are compositions of images and text.

# gf_landing_page
- main landing page of the GF system, meant to hold links to all sub-apps and provide a single initial place for users to access GF. 

# gf_analytics
- used for analytics by admins of a particular GF installation. Analytics of end-user interaction with the GF system.  

# gf_crawl  
- discovers images on target web-pages and downloads them. after download images are registered into the GF system and transformed.  
- meant for automated collection of images from sites of interest.  

# gf_domains  
- allows for viewing and registering domains of interest.  

# gf_tagger  
- used for tagging/annotating all of the main resource types in the GF system - images/posts/domains/etc.  
- allows for both adding of simple **tags**, as well as **notes** which are longer form text bits.  
- bookmarking of web-pages has also been added, to allow for saving web url's independent of the media that they might contain.  

# gf_bookmarks  
- functinality for storing/managing web **bookmarks**.  
- includes front-end components for creating (via browser bookmarklet) and viewing of bookmarks  