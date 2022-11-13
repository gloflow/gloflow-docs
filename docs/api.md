


# API abstraction layer
- investigate possibly creating an abstraction layer for the API
- abstracts REST/gRPC/GraphQL

# REST
- basic API model very well suitable for junior devs to connect with  
- should be supported regardless of which other more advanced API models are used

# gRPC
- services defined using protobuffs  
- autogenerating client/server stubs for services using specified API's  
- gRPC services is defined using protobuffs  

# Protobuffs
- exposing current REST API's  
- binary serialization toolset  
- https://buf.build/  
- good step is to get API's formaly described via an IDL  

# GraphQL
- for flexible query definitions