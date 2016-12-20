Moria
----

Cluster monitoring service with:  
* Master to node communication is done through an RPC Server/Client interface  
* REST API for querying metrics  
* Backing service for storing metrics (Mongo/Redis/PostgreSQL) (InfluxDB - TBD)
* A client for StatsD that enables you to push data to Graphite
* A plugin system that allows you to specify your own metric source