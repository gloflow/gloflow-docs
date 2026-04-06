# GloFlow Documentation - Table of Contents

## Core Documentation Files

1. **api.md** - Explores API abstraction layers and discusses the implementation of REST, gRPC, GraphQL, and Protocol Buffers for formal API definitions.

2. **apps-core.md** - Describes the core applications within GloFlow including gf_solo, gf_images, gf_publisher, gf_landing_page, gf_analytics, and gf_crawl with their respective responsibilities.

3. **code_style.md** - Establishes naming conventions and coding style guidelines across multiple languages (Go, Python, TypeScript, Rust) with emphasis on functional programming principles.

4. **db.md** - Documents the database layer architecture, including current MongoDB support and planned PostgreSQL and SQLite support with DB abstraction goals.

5. **file-system.md** - Outlines the file system abstraction layer designed to allow flexible storage operations across AWS S3, GCP, local filesystem, and IPFS.

6. **identity.md** - Details the identity and authentication system supporting standard username/password, Web3 Ethereum-based authentication, and Auth0 OAuth2.0 integration.

7. **image_storage.md** - Discusses persistent image storage strategies, IPFS backend prioritization, and dynamic storage backend configuration for image flows.

8. **langs.md** - Covers the programming languages used in GloFlow, highlighting Rust integration for image operations and TensorFlow for machine learning workflows.

9. **ui.md** - Mentions the Tauri framework for building a cross-platform desktop application to replace Electron.

10. **history.md** - Provides a comprehensive historical overview of GloFlow's evolution from Python and Erlang backends to Dart, then to Go, and frontend evolution from JavaScript to Dart to TypeScript.

## Images System

11. **images/gf_images_lib.mdx** - Comprehensive documentation of the GloFlow image processing and management library, covering HTTP handlers, storage system (S3, local, IPFS), jobs manager for asynchronous processing, image flows, and the complete upload/processing pipeline.

---

## Summary

The GloFlow documentation collection presents a comprehensive system architecture spanning multiple domains. The documentation covers foundational elements including API design patterns (REST, gRPC, GraphQL), core applications (image management, publishing, analytics, and crawling), and infrastructure concerns such as databases, file systems, identity management, and image storage. 

The Images System documentation provides detailed technical specifications for the gf_images_lib package, including all HTTP handlers for image operations (upload, classification, sharing), the multi-backend storage system (S3, local filesystem, IPFS), the asynchronous jobs manager for image processing, and the flows system for organizing images into collections. This includes complete API references, workflow diagrams, and best practices for integrating with the image processing pipeline.

Additional documentation establishes coding standards across supported languages and records the technical evolution of the GloFlow platform from its origins in Python to its current Go backend and TypeScript frontend implementation. Together, these documents provide both current technical specifications and historical context for understanding the GloFlow project's architecture and development trajectory.
