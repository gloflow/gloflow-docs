**Rust** is used for the gf_images_jobs module at the moment. It includes basic image operations that are coded in Rust without dependencies, for image saturation, contrast, brightness, noise. More operations need to be added:
    - Blur
    - Various shifting in color-space towards a particular color.
    - Image Entropy measurements and croping basic on the highest-entropy region.

**TensorFlow** - at the moment GF can pack images into .tfrecords files, for loading into Tensorflow for model training. The goal is have Tensorflow integrated into GF fully, and allow for image flows to be packaged as .tfrecords and piped into various models for training. Model inferencing is to be integrated as well, for classification of images in flows, for training of models from tags added to images by users. Reinforcment-learning is also to be used in gf_crawl so that the crawler can learn to crawl sites/domains that have high-quality images (and to depth-search those url tree's first).