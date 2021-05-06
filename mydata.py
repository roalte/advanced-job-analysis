#!/usr/bin/env python
# coding: utf-8

# In[1]:


# https://github.com/onurakpolat/awesome-bigdata
big_data_ecosystem1 = [
'RDBMS',
    'MySQL',#T he world's most popular open source database.
    'PostgreSQL',# The world's most advanced open source database.
    'Oracle Database', 'Oracle',# - object-relational database management system.
    'Teradata',# - high-performance MPP data warehouse platform.
'Framework', "фреймворк",
    'Bistro',# - general-purpose data processing engine for both batch and stream analytics. It is based on a novel data model, which represents data via functions and processes data via column operations as opposed to having only set operations in conventional approaches like MapReduce or SQL.
    'IBM Streams', 'Streams',# - platform for distributed processing and real-time analytics. Integrates with many of the popular technologies in the Big Data ecosystem (Kafka, HDFS, Spark, etc.)
    'Apache Hadoop', 'Hadoop',# - framework for distributed processing. Integrates MapReduce (parallel processing), YARN (job scheduling) and HDFS (distributed file system).
    'Tigon',# - High Throughput Real-time Stream Processing Framework.
    'Pachyderm',# - Pachyderm is a data storage platform built on Docker and Kubernetes to provide reproducible data processing and analysis.
    'Polyaxon',# - A platform for reproducible and scalable machine learning and deep learning.
'Distributed Programming', "распределенный программирование",
    'AddThis Hydra','Hydra',# - distributed data processing and storage system originally developed at AddThis.
    'AMPLab SIMR','SIMR',# - run Spark on Hadoop MapReduce v1.
    'Apache APEX', 'APEX',# - a unified, enterprise platform for big data stream and batch processing.
    'Apache Beam', 'Beam',# - an unified model and set of language-specific SDKs for defining and executing data processing workflows.
    'Apache Crunch', 'Crunch',# - a simple Java API for tasks like joining and data aggregation that are tedious to implement on plain MapReduce.
    'Apache DataFu', 'DataFu',# - collection of user-defined functions for Hadoop and Pig developed by LinkedIn.
    'Apache Flink','Flink',# - high-performance runtime, and automatic program optimization.
    'Apache Gearpump','Gearpump',# - real-time big data streaming engine based on Akka.
    'Apache Gora','Gora',# - framework for in-memory data model and persistence.
    'Apache Hama','Hama',# - BSP (Bulk Synchronous Parallel) computing framework.
    'Apache MapReduce','MapReduce',# - programming model for processing large data sets with a parallel, distributed algorithm on a cluster.
    'Apache Pig','Pig',# - high level language to express data analysis programs for Hadoop.
    'Apache REEF','REEF',# - retainable evaluator execution framework to simplify and unify the lower layers of big data systems.
    'Apache S4','S4',# - framework for stream processing, implementation of S4.
    'Apache Spark','Spark',# - framework for in-memory cluster computing.
    'Apache Spark Streaming','Spark Streaming','Streaming',# - framework for stream processing, part of Spark.
    'Apache Storm','Storm',# - framework for stream processing by Twitter also on YARN.
    'Apache Samza','Samza',# - stream processing framework, based on Kafka and YARN.
    'Apache Tez','Tez',# - application framework for executing a complex DAG (directed acyclic graph) of tasks, built on YARN.
    'Apache Twill','Twill',# - abstraction over YARN that reduces the complexity of developing distributed applications.
    'Baidu Bigflow','Bigflow',# - an interface that allows for writing distributed computing programs providing lots of simple, flexible, powerful APIs to easily handle data of any scale.
    'Cascalog',# - data processing and querying library.
    'Cheetah',# - High Performance, Custom Data Warehouse on Top of MapReduce.
    'Concurrent Cascading',# - framework for data management/analytics on Hadoop.
    'Damballa Parkour','Parkour',# - MapReduce library for Clojure.
    'Datasalt Pangool','Pangool',# - alternative MapReduce paradigm.
    'DataTorrent StrAM','StrAM',# - real-time engine is designed to enable distributed, asynchronous, real time in-memory big-data computations in as unblocked a way as possible, with minimal overhead and impact on performance.
    'Facebook Corona','Corona',# - Hadoop enhancement which removes single point of failure.
    'Facebook Peregrine','Peregrine',# - Map Reduce framework.
    'Facebook Scuba','Scuba',# - distributed in-memory datastore.
    'Google Dataflow','Dataflow',#- create data pipelines to help themæingest, transform and analyze data.
    'Google MapReduce','MapReduce',# - map reduce framework.
    'Google MillWheel','MillWheel',# - fault tolerant stream processing framework.
    'IBM Streams','Streams',# - platform for distributed processing and real-time analytics. Provides toolkits for advanced analytics like geospatial, time series, etc. out of the box.
    'JAQL',# - declarative programming language for working with structured, semi-structured and unstructured data.
    'Kite',# - is a set of libraries, tools, examples, and documentation focused on making it easier to build systems on top of the Hadoop ecosystem.
    'Metamarkets Druid','Druid',# - framework for real-time analysis of large datasets.
    'Netflix PigPen','PigPen',# - map-reduce for Clojure which compiles to Apache Pig.
    'Nokia Disco','Disco',# - MapReduce framework developed by Nokia.
    'Onyx',# - Distributed computation for the cloud.
    'Pinterest Pinlater','Pinlater',# - asynchronous job execution system.
    'Pydoop',# - Python MapReduce and HDFS API for Hadoop.
    'Ray',# - A fast and simple framework for building and running distributed applications.
    'Rackerlabs Blueflood','Blueflood',# - multi-tenant distributed metric processing system
    'Skale',# - High performance distributed data processing in NodeJS.
    'Stratosphere',# - general purpose cluster computing framework.
    'Streamdrill',# - useful for counting activities of event streams over different time windows and finding the most active one.
    'streamsx.topology',# - Libraries to enable building IBM Streams application in Java, Python or Scala.
    'Tuktu',# - Easy-to-use platform for batch and streaming computation, built using Scala, Akka and Play!
    'Twitter Heron','Heron',# - Heron is a realtime, distributed, fault-tolerant stream processing engine from Twitter replacing Storm.
    'Twitter Scalding','Scalding',# - Scala library for Map Reduce jobs, built on Cascading.
    'Twitter Summingbird','Summingbird',# - Streaming MapReduce with Scalding and Storm, by Twitter.
    'Twitter TSAR','TSAR',# - TimeSeries AggregatoR by Twitter.
    'Wallaroo',# - The ultrafast and elastic data processing engine. Big or fast data - no fuss, no Java needed.    
'Distributed Filesystem', 'распределенный файловый система'
    'Ambry',# - a distributed object store that supports storage of trillion of small immutable objects as well as billions of large objects.
    'Apache HDFS','HDFS',# - a way to store large files across multiple machines.
    'Apache Kudu','Kudu',# - Hadoop's storage layer to enable fast analytics on fast data.
    'BeeGFS','FhGFS',# - formerly FhGFS, parallel distributed file system.
    'Ceph Filesystem',# - software storage platform designed.
    'Disco DDFS','DDFS',# - distributed filesystem.
    'Facebook Haystack','Haystack',# - object storage system.
    'Google GFS','GFS',# - distributed filesystem.
    'Google Megastore',# - scalable, highly available storage.
    'GridGain',# - GGFS, Hadoop compliant in-memory file system.
    'Lustre file system',# - high-performance distributed filesystem.
    'Microsoft Azure Data Lake Store', 'Microsoft Azure','Data Lake' # - HDFS-compatible storage in Azure cloud
    'Quantcast File System QFS','QFS',# - open-source distributed file system.
    'Red Hat GlusterFS','GlusterFS',# - scale-out network-attached storage file system.
    'Seaweed-FS','Seaweed FS'# - simple and highly scalable distributed file system.
    'Alluxio',# - reliable file sharing at memory speed across cluster frameworks.
    'Tahoe-LAFS','LAFS',# - decentralized cloud storage system.
    'Baidu File System',# - distributed filesystem.    
'Distributed Index', 'распределенный индекс',
    'Pilosa',# Open source distributed bitmap index that dramatically accelerates queries across multiple, massive data sets.
'Document Data Model',
    'Actian Versant','Versant',# - commercial object-oriented database management systems .
    'Crate Data',# - is an open source massively scalable data store. It requires zero administration.
    'Facebook Apollo','Apollo',# - Facebook’s Paxos-like NoSQL database.
    'jumboDB',# - document oriented datastore over Hadoop.
    'LinkedIn Espresso','Espresso',# - horizontally scalable document-oriented NoSQL data store.
    'MarkLogic',# - Schema-agnostic Enterprise NoSQL database technology.
    'Microsoft Azure DocumentDB','DocumentDB',# - NoSQL cloud database service with protocol support for MongoDB
    'MongoDB',# - Document-oriented database system.
    'RavenDB',# - A transactional, open-source Document Database.
    'RethinkDB',# - document database that supports queries like table joins and group by.    
'Key Map Data Model','Key Map',#
    'Apache Accumulo','Accumulo',# - distributed key/value store, built on Hadoop.
    'Apache Cassandra','Cassandra',# - column-oriented distributed datastore, inspired by BigTable.
    'Apache HBase','HBase',# - column-oriented distributed datastore, inspired by BigTable.
    'Baidu Tera','Tera',# - an Internet-scale database, inspired by BigTable.
    'Facebook HydraBase','HydraBase',# - evolution of HBase made by Facebook.
    'Google BigTable','BigTable',# - column-oriented distributed datastore.
    'Google Cloud Datastore','Cloud Datastore',# - is a fully managed, schemaless database for storing non-relational data over BigTable.
    'Hypertable',# - column-oriented distributed datastore, inspired by BigTable.
    'InfiniDB',# - is accessed through a MySQL interface and use massive parallel processing to parallelize queries.
    'Tephra',# - Transactions for HBase.
    'Twitter Manhattan','Manhattan',# - real-time, multi-tenant distributed database for Twitter scale.
    'ScyllaDB',# - column-oriented distributed datastore written in C++, totally compatible with Apache Cassandra.
'Key-value Data Model','Key value',#
    'Aerospike',# - NoSQL flash-optimized, in-memory. Open source and "Server code in 'C' (not Java or Erlang) precisely tuned to avoid context switching and memory copies."
    'Amazon DynamoDB','DynamoDB',# - distributed key/value store, implementation of Dynamo paper.
    'Badger',# - a fast, simple, efficient, and persistent key-value store written natively in Go.
    'Bolt',# - an embedded key-value database for Go.
    'BTDB',# - Key Value Database in .Net with Object DB Layer, RPC, dynamic IL and much more
    'BuntDB',# - a fast, embeddable, in-memory key/value database for Go with custom indexing and geospatial support.
    'Edis',# - is a protocol-compatible Server replacement for Redis.
    'ElephantDB',# - Distributed database specialized in exporting data from Hadoop.
    'EventStore',# - distributed time series database.
    'GhostDB',# - a distributed, in-memory, general purpose key-value data store that delivers microsecond performance at any scale.
    'Graviton',# - a simple, fast, versioned, authenticated, embeddable key-value store database in pure Go(lang).
    'GridDB',# - suitable for sensor data stored in a timeseries.
    'HyperDex',# - a scalable, next generation key-value and document store with a wide array of features, including consistency, fault tolerance and high performance.
    'Ignite',# - is an in-memory key-value data store providing full SQL-compliant data access that can optionally be backed by disk storage.
    'LinkedIn Krati','Krati',# - is a simple persistent data store with very low latency and high throughput.
    'Linkedin Voldemort','Voldemort',# - distributed key/value storage system.
    'Oracle NoSQL Database','NoSQL Database','NoSQL',# - distributed key-value database by Oracle Corporation.
    'Redis',# - in memory key value datastore.
    'Riak',# - a decentralized datastore.
    'Storehaus',# - library to work with asynchronous key value stores, by Twitter.
    'SummitDB',# - an in-memory, NoSQL key/value database, with disk persistance and using the Raft consensus algorithm.
    'Tarantool',# - an efficient NoSQL database and a Lua application server.
    'TiKV',# - a distributed key-value database powered by Rust and inspired by Google Spanner and HBase.
    'Tile38',# - a geolocation data store, spatial index, and realtime geofence, supporting a variety of object types including latitude/longitude points, bounding boxes, XYZ tiles, Geohashes, and GeoJSON
    'TreodeDB',# - key-value store that's replicated and sharded and provides atomic multirow writes.
'Graph Data Model',#
    'AgensGraph',# - a new generation multi-model graph database for the modern complex data environment.
    'Apache Giraph','Giraph',# - implementation of Pregel, based on Hadoop.
    'Apache Spark Bagel','Spark Bagel','Bagel',# - implementation of Pregel, part of Spark.
    'ArangoDB',# - multi model distributed database.
    'DGraph',# - A scalable, distributed, low latency, high throughput graph database aimed at providing Google production level scale and throughput, with low enough latency to be serving real time user queries, over terabytes of structured data.
    'EliasDB',# - a lightweight graph based database that does not require any third-party libraries.
    'Facebook TAO','TAO',# - TAO is the distributed data store that is widely used at facebook to store and serve the social graph.
    'GCHQ Gaffer','Gaffer',# - Gaffer by GCHQ is a framework that makes it easy to store large-scale graphs in which the nodes and edges have statistics.
    'Google Cayley','Cayley',# - open-source graph database.
    'Google Pregel','Pregel',# - graph processing framework.
    'GraphLab PowerGraph','PowerGraph',# - a core C++ GraphLab API and a collection of high-performance machine learning and data mining toolkits built on top of the GraphLab API.
    'GraphX',# - resilient Distributed Graph System on Spark.
    'Gremlin',# - graph traversal Language.
    'Infovore',# - RDF-centric Map/Reduce framework.
    'Intel GraphBuilder','GraphBuilder',# - tools to construct large-scale graphs on top of Hadoop.
    'JanusGraph',# - open-source, distributed graph database with multiple options for storage backends (Bigtable, HBase, Cassandra, etc.) and indexing backends (Elasticsearch, Solr, Lucene).
    'MapGraph',# - Massively Parallel Graph processing on GPUs.
    'Microsoft Graph Engine','Graph Engine',# - a distributed in-memory data processing engine, underpinned by a strongly-typed in-memory key-value store and a general distributed computation engine.
    'Neo4j',# - graph database written entirely in Java.
    'OrientDB',# - document and graph database.
    'Phoebus',# - framework for large scale graph processing.
    'Titan',# - distributed graph database, built over Cassandra.
    'Twitter FlockDB','FlockDB',# - distributed graph database.
    'NodeXL',# - A free, open-source template for Microsoft® Excel® 2007, 2010, 2013 and 2016 that makes it easy to explore network graphs.    
'Columnar Databases',#
    'Columnar Storage',# - an explanation of what columnar storage is and when you might want it.
    'Actian Vector',# - column-oriented analytic database.
    'ClickHouse',# - an open-source column-oriented database management system that allows generating analytical data reports in real time.
    'EventQL',# - a distributed, column-oriented database built for large-scale event collection and analytics.
    'MonetDB',# - column store database.
    'Parquet',# - columnar storage format for Hadoop.
    'Pivotal Greenplum','Greenplum',# - purpose-built, dedicated analytic data warehouse that offers a columnar engine as well as a traditional row-based one.
    'Vertica',# - is designed to manage large, fast-growing volumes of data and provide very fast query performance when used for data warehouses.
    'SQream DB','SQream',# - A GPU powered big data database, designed for analytics and data warehousing, with ANSI-92 compliant SQL, suitable for data sets from 10TB to 1PB.
    'Google BigQuery','BigQuery',# - Google's cloud offering backed by their pioneering work on Dremel.
    'Amazon Redshift','Redshift',# - Amazon's cloud offering, also based on a columnar datastore backend.
    'IndexR',# - an open-source columnar storage format for fast & realtime analytic with big data.
    'LocustDB',# - an experimental analytics database aiming to set a new standard for query performance on commodity hardware.    
'NewSQL Databases',#
    'Actian Ingres','Ingres',# - commercially supported, open-source SQL relational database management system.
    'ActorDB',# - a distributed SQL database with the scalability of a KV store, while keeping the query capabilities of a relational database.
    'Amazon RedShift','RedShift',# - data warehouse service, based on PostgreSQL.
    'BayesDB',# - statistic oriented SQL database.
    'Bedrock',# - a simple, modular, networked and distributed transaction layer built atop SQLite.
    'CitusDB',# - scales out PostgreSQL through sharding and replication.
    'Cockroach',# - Scalable, Geo-Replicated, Transactional Datastore.
    'Comdb2',# - a clustered RDBMS built on optimistic concurrency control techniques.
    'Datomic',# - distributed database designed to enable scalable, flexible and intelligent applications.
    'FoundationDB',# - distributed database, inspired by F1.
    'Google F1','F1',# - distributed SQL database built on Spanner.
    'Google Spanner','Spanner',# - globally distributed semi-relational database.
    'H-Store','H Store',# - is an experimental main-memory, parallel database management system that is optimized for on-line transaction processing (OLTP) applications.
    'Haeinsa',# - linearly scalable multi-row, multi-table transaction library for HBase based on Percolator.
    'HandlerSocket',# - NoSQL plugin for MySQL/MariaDB.
    'InfiniSQL',# - infinity scalable RDBMS.
    'KarelDB',# - a relational database backed by Apache Kafka.
    'Map-D','Map D',# - GPU in-memory database, big data analysis and visualization platform.
    'MemSQL',# - in memory SQL database witho optimized columnar storage on flash.
    'NuoDB',# - SQL/ACID compliant distributed database.
    'Oracle TimesTen in-Memory Database','TimesTen',# - in-memory, relational database management system with persistence and recoverability.
    'Pivotal GemFire XD','GemFire XD','GemFire',# - Low-latency, in-memory, distributed SQL data store. Provides SQL interface to in-memory table data, persistable in HDFS.
    'SAP HANA','HANA',# - is an in-memory, column-oriented, relational database management system.
    'SenseiDB',# - distributed, realtime, semi-structured database.
    'Sky',# - database used for flexible, high performance analysis of behavioral data.
    'SymmetricDS',# - open source software for both file and database synchronization.
    'TiDB',# - TiDB is a distributed SQL database. Inspired by the design of Google F1.
    'VoltDB',# - claims to be fastest in-memory database.
    'yugabyteDB',# - open source, high-performance, distributed SQL database compatible with PostgreSQL.    
'Time Series Databases','Time Series'#
    'Axibase Time Series Database','Axibase',# - Integrated time series database on top of HBase with built-in visualization, rule-engine and SQL support.
    'Chronix',# - a time series storage built to store time series highly compressed and for fast access times.
    'Cube',# - uses MongoDB to store time series data.
    'Heroic',# - is a scalable time series database based on Cassandra and Elasticsearch.
    'InfluxDB',# - distributed time series database.
    'IronDB',# - scalable, general-purpose time series database.
    'Kairosdb',# - similar to OpenTSDB but allows for Cassandra.
    'M3DB',# - a distributed time series database that can be used for storing realtime metrics at long retention.
    'Newts',# - a time series database based on Apache Cassandra.
    'TDengine',# - a time series database in C utilizing unique features of IoT to improve read/write throughput and reduce space needed to store data
    'OpenTSDB',# - distributed time series database on top of HBase.
    'Prometheus',# - a time series database and service monitoring system.
    'Beringei',# - Facebook's in-memory time-series database.
    'TrailDB',# - an efficient tool for storing and querying series of events.
    'Druid',# Column oriented distributed data store ideal for powering interactive applications
    'Riak-TS','Riak TS',# Riak TS is the only enterprise-grade NoSQL time series database optimized specifically for IoT and Time Series data.
    'Akumuli',# Akumuli is a numeric time-series database. It can be used to capture, store and process time-series data in real-time. The word "akumuli" can be translated from esperanto as "accumulate".
    'Rhombus',# A time-series object store for Cassandra that handles all the complexity of building wide row indexes.
    'Dalmatiner DB','Dalmatiner',# Fast distributed metrics database
    'Blueflood',# A distributed system designed to ingest and process time series data
    'Timely',# Timely is a time series database application that provides secure access to time series data based on Accumulo and Grafana.
    'SiriDB',# Highly-scalable, robust and fast, open source time series database with cluster functionality.
    'Thanos',# - Thanos is a set of components to create a highly available metric system with unlimited storage capacity using multiple (existing) Prometheus deployments.
    'VictoriaMetrics',# - fast, scalable and resource-effective open-source TSDB compatible with Prometheus. Single-node and cluster versions included
'SQL-like processing','SQL like'#
    'Actian SQL for Hadoop','Actian SQL',# - high performance interactive SQL access to all Hadoop data.
    'Apache Drill','Drill',# - framework for interactive analysis, inspired by Dremel.
    'Apache HCatalog','HCatalog',# - table and storage management layer for Hadoop.
    'Apache Hive','Hive',# - SQL-like data warehouse system for Hadoop.
    'Apache Calcite','Calcite',# - framework that allows efficient translation of queries involving heterogeneous and federated data.
    'Apache Phoenix','Phoenix',# - SQL skin over HBase.
    'Aster Database','Aster',# - SQL-like analytic processing for MapReduce.
    'Cloudera Impala','Impala',# - framework for interactive analysis, Inspired by Dremel.
    'Concurrent Lingual','Concurrent','Lingual',# - SQL-like query language for Cascading.
    'Datasalt Splout SQL','Splout SQL',# - full SQL query engine for big datasets.
    'Dremio',# - an open-source, SQL-like Data-as-a-Service Platform based on Apache Arrow.
    'Facebook PrestoDB','PrestoDB',# - distributed SQL query engine.
    'Google BigQuery','BigQuery',# - framework for interactive analysis, implementation of Dremel.
    'Materialize',# - is a streaming database for real-time applications using SQL for queries and supporting a large fraction of PostgreSQL.
    'Invantive SQL','Invantive',# - SQL engine for online and on-premise use with integrated local data replication and 70+ connectors.
    'PipelineDB',# - an open-source relational database that runs SQL queries continuously on streams, incrementally storing results in tables.
    'Pivotal HDB','HDB',# - SQL-like data warehouse system for Hadoop.
    'RainstorDB',# - database for storing petabyte-scale volumes of structured and semi-structured data.
    'Spark Catalyst','Catalyst',# - is a Query Optimization Framework for Spark and Shark.
    'SparkSQL',# - Manipulating Structured Data Using Spark.
    'Splice Machine',# - a full-featured SQL-on-Hadoop RDBMS with ACID transactions.
    'Stinger',# - interactive query for Hive.
    'Tajo',# - distributed data warehouse system on Hadoop.
    'Trafodion',# - enterprise-class SQL-on-HBase solution targeting big data transactional or operational workloads.    
'Data Ingestion',#
    'redpanda',# - A Kafka® replacement for mission critical systems; 10x faster. Written in C++.
    'Amazon Kinesis','Kinesis',# - real-time processing of streaming data at massive scale.
    'Amazon Web Services Glue','Glue','ETL'# - serverless fully managed extract, transform, and load (ETL) service
    'Apache Chukwa','Chukwa',# - data collection system.
    'Apache Flume','Flume',# - service to manage large amount of log data.
    'Apache Kafka','Kafka',# - distributed publish-subscribe messaging system.
    'Apache NiFi','NiFi',# - Apache NiFi is an integrated data logistics platform for automating the movement of data between disparate systems.
    'Apache Pulsar','Pulsar',# - a distributed pub-sub messaging platform with a very flexible messaging model and an intuitive client API.
    'Apache Sqoop','Sqoop',# - tool to transfer data between Hadoop and a structured datastore.
    'Embulk',# - open-source bulk data loader that helps data transfer between various databases, storages, file formats, and cloud services.
    'Facebook Scribe','Scribe',# - streamed log data aggregator.
    'Fluentd',# - tool to collect events and logs.
    'Gazette',# - Distributed streaming infrastructure built on cloud storage which makes it easy to mix and match batch and streaming paradigms.
    'Google Photon','Photon',# - geographically distributed system for joining multiple continuously flowing streams of data in real-time with high scalability and low latency.
    'Heka',# - open source stream processing software system.
    'HIHO',# - framework for connecting disparate data sources with Hadoop.
    'Kestrel',# - distributed message queue system.
    'LinkedIn Databus','Databus',# - stream of change capture events for a database.
    'LinkedIn Kamikaze','Kamikaze',# - utility package for compressing sorted integer arrays.
    'LinkedIn White Elephant','White Elephant',# - log aggregator and dashboard.
    'Logstash',# - a tool for managing events and logs.
    'Netflix Suro','Suro',# - log agregattor like Storm and Samza based on Chukwa.
    'Pinterest Secor','Secor',# - is a service implementing Kafka log persistance.
    'Linkedin Gobblin','Gobblin',# - linkedin's universal data ingestion framework.
    'Skizze',# - sketch data store to deal with all problems around counting and sketching using probabilistic data-structures.
    'StreamSets Data Collector','StreamSets',# - continuous big data ingest infrastructure with a simple to use IDE.
    'Alooma',# - data pipeline as a service enabling moving data sources such as MySQL into data warehouses.
    'RudderStack',# - an open source customer data infrastructure (segment, mParticle alternative) written in go.  
'Service Programming',#
    'Akka Toolkit',# - runtime for distributed, and fault tolerant event-driven applications on the JVM.
    'Apache Avro','Avro',# - data serialization system.
    'Apache Curator','Curator',# - Java libaries for Apache ZooKeeper.
    'Apache Karaf','Karaf',# - OSGi runtime that runs on top of any OSGi framework.
    'Apache Thrift','Thrift',# - framework to build binary protocols.
    'Apache Zookeeper','Zookeeper',# - centralized service for process management.
    'Google Chubby','Chubby',# - a lock service for loosely-coupled distributed systems.
    'Hydrosphere Mist','Mist',# - a service for exposing Apache Spark analytics jobs and machine learning models as realtime, batch or reactive web services.
    'Linkedin Norbert','Norbert',# - cluster manager.
    'Mara',# - A lightweight opinionated ETL framework, halfway between plain scripts and Apache Airflow
    'OpenMPI',# - message passing framework.
    'Serf',# - decentralized solution for service discovery and orchestration.
    'Spotify Luigi','Luigi',# - a Python package for building complex pipelines of batch jobs. It handles dependency resolution, workflow management, visualization, handling failures, command line integration, and much more.
    'Spring XD','XD',# - distributed and extensible system for data ingestion, real time analytics, batch processing, and data export.
    'Twitter Elephant Bird','Elephant Bird',# - libraries for working with LZOP-compressed data.
    'Twitter Finagle','Finagle',# - asynchronous network stack for the JVM.    
'Scheduling',#
    'Apache Airflow','Airflow',# - a platform to programmatically author, schedule and monitor workflows.
    'Apache Aurora','Aurora',# - is a service scheduler that runs on top of Apache Mesos.
    'Apache Falcon','Falcon',# - data management framework.
    'Apache Oozie','Oozie',# - workflow job scheduler.
    'Azure Data Factory','Data Factory',# - cloud-based pipeline orchestration for on-prem, cloud and HDInsight
    'Chronos',# - distributed and fault-tolerant scheduler.
    'Cronicle',# - Distributed, easy to install, NodeJS based, task scheduler
    'Dagster',# - a data orchestrator for machine learning, analytics, and ETL.
    'Linkedin Azkaban','Azkaban',# - batch workflow job scheduler.
    'Schedoscope',# - Scala DSL for agile scheduling of Hadoop jobs.
    'Sparrow',# - scheduling platform.    
'Machine Learning', 'ml', 'машинный обучение'#
    'Azure ML Studio','ML Studio',# - Cloud-based AzureML, R, Python Machine Learning platform
    'brain',# - Neural networks in JavaScript.
    'Oryx',# - Lambda architecture on Apache Spark, Apache Kafka for real-time large scale machine learning.
    'Concurrent Pattern',# - machine learning library for Cascading.
    'convnetjs',# - Deep Learning in Javascript. Train Convolutional Neural Networks (or ordinary ones) in your browser.
    'DataVec',# - A vectorization and data preprocessing library for deep learning in Java and Scala. Part of the Deeplearning4j ecosystem.
    'Deeplearning4j',# - Fast, open deep learning for the JVM (Java, Scala, Clojure). A neural network configuration layer powered by a C++ library. Uses Spark and Hadoop to train nets on multiple GPUs and CPUs.
    'Decider',# - Flexible and Extensible Machine Learning in Ruby.
    'ENCOG',# - machine learning framework that supports a variety of advanced algorithms, as well as support classes to normalize and process data.
    'etcML',# - text classification with machine learning.
    'Etsy Conjecture','Conjecture',# - scalable Machine Learning in Scalding.
    'Feast',# - A feature store for the management, discovery, and access of machine learning features. Feast provides a consistent view of feature data for both model training and model serving.
    'GraphLab Create','GraphLab',# - A machine learning platform in Python with a broad collection of ML toolkits, data engineering, and deployment tools.
    'H2O',# - statistical, machine learning and math runtime with Hadoop. R and Python.
    'Karate Club',# - An unsupervised machine learning library for graph structured data. Python
    'Keras',# - An intuitive neural net API inspired by Torch that runs atop Theano and Tensorflow.
    'Lambdo',# - Lambdo is a workflow engine which significantly simplifies the analysis process by unifying feature engineering and machine learning operations.
    'Little Ball of Fur',# - A subsampling library for graph structured data. Python
    'Mahout',# - An Apache-backed machine learning library for Hadoop.
    'MLbase',# - distributed machine learning libraries for the BDAS stack.
    'MLPNeuralNet',# - Fast multilayer perceptron neural network library for iOS and Mac OS X.
    'ML Workspace',# - All-in-one web-based IDE specialized for machine learning and data science.
    'MOA',# - MOA performs big data stream mining in real time, and large scale machine learning.
    'MonkeyLearn',# - Text mining made easy. Extract and classify data from text.
    'ND4J',# - A matrix library for the JVM. Numpy for Java.
    'nupic',# - Numenta Platform for Intelligent Computing: a brain-inspired machine intelligence platform, and biologically accurate neural network based on cortical learning algorithms.
    'PredictionIO',# - machine learning server buit on Hadoop, Mahout and Cascading.
    'PyTorch Geometric Temporal','PyTorch',# - a temporal extension library for PyTorch Geometric .
    'RL4J',# - Reinforcement learning for Java and Scala. Includes Deep-Q learning and A3C algorithms, and integrates with Open AI's Gym. Runs in the Deeplearning4j ecosystem.
    'SAMOA',# - distributed streaming machine learning framework.
    'scikit-learn','scikit learn',# - scikit-learn: machine learning in Python.
    'Shapley',# - A data-driven framework to quantify the value of classifiers in a machine learning ensemble.
    'Spark MLlib','MLlib',# - a Spark implementation of some common machine learning (ML) functionality.
    'Sibyl',# - System for Large Scale Machine Learning at Google.
    'TensorFlow',# - Library from Google for machine learning using data flow graphs.
    'Theano',# - A Python-focused machine learning library supported by the University of Montreal.
    'Torch',# - A deep learning library with a Lua API, supported by NYU and Facebook.
    'Velox',# - System for serving machine learning predictions.
    'Vowpal Wabbit','Wabbit',# - learning system sponsored by Microsoft and Yahoo!.
    'WEKA',# - suite of machine learning software.
    'BidMach',# - CPU and GPU-accelerated Machine Learning Library.    
'Benchmarking',#
    'Apache Hadoop Benchmarking','Hadoop Benchmarking',# - micro-benchmarks for testing Hadoop performances.
    'Berkeley SWIM Benchmark','SWIM Benchmark',# - real-world big data workload benchmark.
    'Intel HiBench','HiBench',# - a Hadoop benchmark suite.
    'PUMA Benchmarking',# - benchmark suite for MapReduce applications.
    'Yahoo Gridmix3','Gridmix3',# - Hadoop cluster benchmarking from Yahoo engineer team.
    'Deeplearning4j Benchmarks','Deeplearning4j',#
'Security',#
    'Apache Ranger','Ranger',# - Central security admin & fine-grained authorization for Hadoop
    'Apache Eagle','Eagle',# - real time monitoring solution
    'Apache Knox Gateway','Knox Gateway','Knox',# - single point of secure access for Hadoop clusters.
    'Apache Sentry','Sentry',# - security module for data stored in Hadoop.
    'BDA',# - The vulnerability detector for Hadoop and Spark    
'System Deployment',#
    'Apache Ambari','Ambari',# - operational framework for Hadoop mangement.
    'Apache Bigtop','Bigtop',# - system deployment framework for the Hadoop ecosystem.
    'Apache Helix','Helix',# - cluster management framework.
    'Apache Mesos','Mesos',# - cluster manager.
    'Apache Slider','Slider',# - is a YARN application to deploy existing distributed applications on YARN.
    'Apache Whirr','Whirr',# - set of libraries for running cloud services.
    'Apache YARN','YARN',# - Cluster manager.
    'Brooklyn',# - library that simplifies application deployment and management.
    'Buildoop',# - Similar to Apache BigTop based on Groovy language.
    'Cloudera HUE','HUE',# - web application for interacting with Hadoop.
    'Facebook Prism','Prism',# - multi datacenters replication system.
    'Google Borg','Borg',# - job scheduling and monitoring system.
    'Google Omega','Omega',# - job scheduling and monitoring system.
    'Hortonworks HOYA','HOYA',# - application that can deploy HBase cluster on YARN.
    'Kubernetes',# - a system for automating deployment, scaling, and management of containerized applications.
    'Marathon',# - Mesos framework for long-running services.
    'Linkis',# - Linkis helps easily connect to various back-end computation/storage engines.    
'Applications',#
    '411',# - an web application for alert management resulting from scheduled searches into Elasticsearch.
    'Adobe spindle','spindle',# - Next-generation web analytics processing with Scala, Spark, and Parquet.
    'Apache Metron','Metron',# - a platform that integrates a variety of open source big data technologies in order to offer a centralized tool for security monitoring and analysis.
    'Apache Nutch','Nutch',# - open source web crawler.
    'Apache OODT','OODT',# - capturing, processing and sharing of data for NASA's scientific archives.
    'Apache Tika','Tika',# - content analysis toolkit.
    'Argus',# - Time series monitoring and alerting platform.
    'AthenaX',# - a streaming analytics platform that enables users to run production-quality, large scale streaming analytics using Structured Query Language (SQL).
    'Atlas',# - a backend for managing dimensional time series data.
    'Countly',# - open source mobile and web analytics platform, based on Node.js & MongoDB.
    'Domino',# - Run, scale, share, and deploy models — without any infrastructure.
    'Eclipse BIRT','BIRT',# - Eclipse-based reporting system.
    'ElastAert',# - ElastAlert is a simple framework for alerting on anomalies, spikes, or other patterns of interest from data in ElasticSearch.
    'Eventhub',# - open source event analytics platform.
    'HASH',# - open source simulation and visualization platform.
    'Hermes',# - asynchronous message broker built on top of Kafka.
    'Hunk',# - Splunk analytics for Hadoop.
    'Imhotep',# - Large scale analytics platform by indeed.
    'Indicative',# - Web & mobile analytics tool, with data warehouse (AWS, BigQuery) integration.
    'Jupyter',# - Notebook and project application for interactive data science and scientific computing across all programming languages.
    'MADlib',# - data-processing library of an RDBMS to analyze data.
    'Kapacitor',# - an open source framework for processing, monitoring, and alerting on time series data.
    'Kylin',# - open source Distributed Analytics Engine from eBay.
    'PivotalR',# - R on Pivotal HD / HAWQ and PostgreSQL.
    'Rakam',# - open-source real-time custom analytics platform powered by Postgresql, Kinesis and PrestoDB.
    'Qubole',# - auto-scaling Hadoop cluster, built-in data connectors.
    'SnappyData',# - a distributed in-memory data store for real-time operational analytics, delivering stream analytics, OLTP (online transaction processing) and OLAP (online analytical processing) built on Spark in a single integrated cluster.
    'Snowplow',# - enterprise-strength web and event analytics, powered by Hadoop, Kinesis, Redshift and Postgres.
    'SparkR',# - R frontend for Spark.
    'Splunk',# - analyzer for machine-generated data.
    'Sumo Logic','Logic',# - cloud based analyzer for machine-generated data.
    'Talend',# - unified open source environment for YARN, Hadoop, HBASE, Hive, HCatalog & Pig.    
'Search engine', 'Search framework',#
    'Apache Lucene','Lucene',# - Search engine library.
    'Apache Solr','Solr',# - Search platform for Apache Lucene.
    'Elassandra',# - is a fork of Elasticsearch modified to run on top of Apache Cassandra in a scalable and resilient peer-to-peer architecture.
    'ElasticSearch',# - Search and analytics engine based on Apache Lucene.
    'Enigma.io','Enigma',# – Freemium robust web application for exploring, filtering, analyzing, searching and exporting massive datasets scraped from across the Web.
    'Google Caffeine','Caffeine',# - continuous indexing system.
    'Google Percolator','Percolator',# - continuous indexing system.
    'HBase Coprocessor','Coprocessor',# - implementation of Percolator, part of HBase.
    'Lily HBase Indexer','HBase Indexer','HBase',# - quickly and easily search for any content stored in HBase.
    'LinkedIn Bobo','Bobo',# - is a Faceted Search implementation written purely in Java, an extension to Apache Lucene.
    'LinkedIn Cleo','Cleo',# - is a flexible software library for enabling rapid development of partial, out-of-order and real-time typeahead search.
    'LinkedIn Galene','Galene',# - search architecture at LinkedIn.
    'LinkedIn Zoie','Zoie',# - is a realtime search/indexing system written in Java.
    'MG4J',# - MG4J (Managing Gigabytes for Java) is a full-text search engine for large document collections written in Java. It is highly customisable, high-performance and provides state-of-the-art features and new research algorithms.
    'Sphinx Search Server','Sphinx',# - fulltext search engine.
    'Vespa',# - is an engine for low-latency computation over large data sets. It stores and indexes your data such that queries, selection and processing over the data can be performed at serving time.
    'Facebook Faiss','Faiss',# - is a library for efficient similarity search and clustering of dense vectors. It contains algorithms that search in sets of vectors of any size, up to ones that possibly do not fit in RAM. It also contains supporting code for evaluation and parameter tuning. Faiss is written in C++ with complete wrappers for Python/numpy.
    'Annoy',# - is a C++ library with Python bindings to search for points in space that are close to a given query point. It also creates large read-only file-based data structures that are mmapped into memory so that many processes may share the same data.
    'Weaviate',# - Weaviate is a GraphQL-based semantic search engine with build-in (word) embeddings.    
'MySQL fork', 'MySQL evolution',#
    'Amazon RDS','RDS',# - MySQL databases in Amazon's cloud.
    'Drizzle',# - evolution of MySQL 6.0.
    'Google Cloud SQL','Cloud SQL',# - MySQL databases in Google's cloud.
    'MariaDB',# - enhanced, drop-in replacement for MySQL.
    'MySQL Cluster',# - MySQL implementation using NDB Cluster storage engine.
    'Percona Server',# - enhanced, drop-in replacement for MySQL.
    'ProxySQL',# - High Performance Proxy for MySQL.
    'TokuDB',# - TokuDB is a storage engine for MySQL and MariaDB.
    'WebScaleSQL',# - is a collaboration among engineers from several companies that face similar challenges in running MySQL at scale.    
'PostgreSQL fork' 'PostgreSQL evolution',#
    'HadoopDB',# - hybrid of MapReduce and DBMS.
    'IBM Netezza','Netezza',# - high-performance data warehouse appliances.
    'Postgres-XL','Postgres XL',# - Scalable Open Source PostgreSQL-based Database Cluster.
    'RecDB',# - Open Source Recommendation Engine Built Entirely Inside PostgreSQL.
    'Stado',# - open source MPP database system solely targeted at data warehousing and data mart applications.
    'Yahoo Everest','Everest',# - multi-peta-byte database / MPP derived by PostgreSQL.
    'TimescaleDB',# - An open-source time-series database optimized for fast ingest and complex queries
    'PipelineDB',# - The Streaming SQL Database. An open-source relational database that runs SQL queries continuously on streams, incrementally storing results in tables    
'Memcached fork', 'Memcached evolution',#
    'Facebook McDipper','McDipper',# - key/value cache for flash storage.
    'Facebook Memcached','Memcached',# - fork of Memcache.
    'Twemproxy',# - A fast, light-weight proxy for memcached and redis.
    'Twitter Fatcache','Fatcache',# - key/value cache for flash storage.
    'Twitter Twemcache','Twemcache',# - fork of Memcache.
'Embedded Database',#
    'Actian PSQL','PSQL',# - ACID-compliant DBMS developed by Pervasive Software, optimized for embedding in applications.
    'BerkeleyDB',# - a software library that provides a high-performance embedded database for key/value data.
    'HanoiDB',# - Erlang LSM BTree Storage.
    'LevelDB',# - a fast key-value storage library written at Google that provides an ordered mapping from string keys to string values.
    'LMDB',# - ultra-fast, ultra-compact key-value embedded data store developed by Symas.
    'RocksDB',# - embeddable persistent key-value store for fast storage based on LevelDB.
'Business Intelligence',#
    'BIME Analytics',# - business intelligence platform in the cloud.
    'Blazer',# - business intelligence made simple.
    'Chartio',# - lean business intelligence platform to visualize and explore your data.
    'Count',# - notebook-based anlytics and visualisation platform using SQL or drag-and-drop.
    'datapine',# - self-service business intelligence tool in the cloud.
    'GoodData',# - platform for data products and embedded analytics.
    'Jaspersoft',# - powerful business intelligence suite.
    'Jedox Palo','Palo',# - customisable Business Intelligence platform.
    'Jethrodata',# - Interactive Big Data Analytics.
    'intermix.io','intermix',# - Performance Monitoring for Amazon Redshift
    'Metabase',# - The simplest, fastest way to get business intelligence and analytics to everyone in your company.
    'Microsoft',# - business intelligence software and platform.
    'Microstrategy',# - software platforms for business intelligence, mobile intelligence, and network applications.
    'Numeracy',# - Fast, clean SQL client and business intelligence.
    'Pentaho',# - business intelligence platform.
    'Qlik',# - business intelligence and analytics platform.
    'Redash',# - Open source business intelligence platform, supporting multiple data sources and planned queries.
    'Saiku Analytics',# - Open source analytics platform.
    'Knowage',# - open source business intelligence platform. (former SpagoBi)
    'SparklineData SNAP','SparklineData','SNAP',# - modern B.I platform powered by Apache Spark.
    'Tableau',# - business intelligence platform.
    'Zoomdata',# - Big Data Analytics.
'Data Visualization','визуализация данные'#
    'Airpal',# - Web UI for PrestoDB.
    'AnyChart',# - fast, simple and flexible JavaScript (HTML5) charting library featuring pure JS API.
    'Arbor',# - graph visualization library using web workers and jQuery.
    'Banana',# - visualize logs and time-stamped data stored in Solr. Port of Kibana.
    'Bloomery',# - Web UI for Impala.
    'Bokeh',# - A powerful Python interactive visualization library that targets modern web browsers for presentation, with the goal of providing elegant, concise construction of novel graphics in the style of D3.js, but also delivering this capability with high-performance interactivity over very large or streaming datasets.
    'C3',# - D3-based reusable chart library
    'CartoDB',# - open-source or freemium hosting for geospatial databases with powerful front-end editing capabilities and a robust API.
    'chartd',# - responsive, retina-compatible charts with just an img tag.
    'Chart.js',# - open source HTML5 Charts visualizations.
    'Chartist.js',# - another open source HTML5 Charts visualization.
    'Crossfilter',# - JavaScript library for exploring large multivariate datasets in the browser. Works well with dc.js and d3.js.
    'Cubism',# - JavaScript library for time series visualization.
    'Cytoscape',# - JavaScript library for visualizing complex networks.
    'DC.js',# - Dimensional charting built to work natively with crossfilter rendered using d3.js. Excellent for connecting charts/additional metadata to hover events in D3.
    'D3',# - javaScript library for manipulating documents.
    'D3.compose',# - Compose complex, data-driven visualizations from reusable charts and components.
    'D3Plus',# - A fairly robust set of reusable charts and styles for d3.js.
    'Dash',# - Analytical Web Apps for Python, R, Julia, and Jupyter. Built on top of plotly, no JS required
    'DevExtreme React Chart','DevExtreme',# - High-performance plugin-based React chart for Bootstrap and Material Design.
    'Echarts',# - Baidus enterprise charts.
    'Envisionjs',# - dynamic HTML5 visualization.
    'FnordMetric',# - write SQL queries that return SVG charts rather than tables
    'Frappe Charts','Frappe',# - GitHub-inspired simple and modern SVG charts for the web with zero dependencies.
    'Freeboard',# - pen source real-time dashboard builder for IOT and other web mashups.
    'Gephi',# - An award-winning open-source platform for visualizing and manipulating large graphs and network connections. It's like Photoshop, but for graphs. Available for Windows and Mac OS X.
    'Google Charts',# - simple charting API.
    'Grafana',# - graphite dashboard frontend, editor and graph composer.
    'Graphite',# - scalable Realtime Graphing.
    'Highcharts',# - simple and flexible charting API.
    'IPython',# - provides a rich architecture for interactive computing.
    'Kibana',# - visualize logs and time-stamped data
    'Lumify',# - open source big data analysis and visualization platform
    'Matplotlib',# - plotting with Python.
    'Metricsgraphic.js',# - a library built on top of D3 that is optimized for time-series data
    'NVD3',# - chart components for d3.js.
    'Peity',# - Progressive SVG bar, line and pie charts.
    'Plot.ly','Plotly',# - Easy-to-use web service that allows for rapid creation of complex charts, from heatmaps to histograms. Upload data to create and style charts with Plotly's online spreadsheet. Fork others' plots.
    'Plotly.js',# The open source javascript graphing library that powers plotly.
    'Recline',# - simple but powerful library for building data applications in pure Javascript and HTML.
    'Redash',# - open-source platform to query and visualize data.
    'ReCharts',# - A composable charting library built on React components
    'Shiny',# - a web application framework for R.
    'Sigma.js',# - JavaScript library dedicated to graph drawing.
    'Superset',# - a data exploration platform designed to be visual, intuitive and interactive, making it easy to slice, dice and visualize data and perform analytics at the speed of thought.
    'Vega',# - a visualization grammar.
    'Zeppelin',# - a notebook-style collaborative data analysis.
    'Zing Charts',# - JavaScript charting library for big data.
    'DataSphere Studio','DataSphere',# - one-stop data application development management portal.
'Internet of things', 'sensor data',#
    'Apache Edgent','Edgent',# - a programming model and micro-kernel style runtime that can be embedded in gateways and small footprint edge devices enabling local, real-time, analytics on the edge devices.
    'Azure IoT Hub',# - Cloud-based bi-directional monitoring and messaging hub
    'TempoIQ',# - Cloud-based sensor analytics.
    '2lemetry',# - Platform for Internet of things.
    'Pubnub',# - Data stream network
    'ThingWorx',# - Rapid development and connection of intelligent systems
    'IFTTT',# - If this then that
    'Evrything',#- Making products smart
    'NetLytics',# - Analytics platform to process network data on Spark.   
]


# In[11]:


# http://hadoopecosystemtable.github.io/

hadoop_ecosystem = [
'Distributed Filesystem', 'распределенный файловый система', 'DFS',    
    'Apache HDFS','HDFS',
    'Red Hat GlusterFS', 'GlusterFS',
    'Quantcast File System QFS', 'QFS',
    'Ceph Filesystem', 'Ceph',
    'Lustre file system', 'Lustre',
    'Alluxio',
    'GridGain', 'GGFS',
    'XtreemFS',
'Distributed Programming','распределенный программирование',
    'Apache Ignite','Ignite',
    'Apache MapReduce','MapReduce',
    'Apache Pig','Pig',
    'JAQL',
    'Apache Spark','Spark',
    'Apache Storm','Storm',
    'Apache Flink','Flink',
    'Apache Apex','Apex',
    'Netflix PigPen','PigPen',
    'AMPLab SIMR','SIMR',
    'Facebook Corona','Corona',
    'Apache REEF','REEF',
    'Apache Twill','Twill',
    'Damballa Parkour','Parkour',
    'Apache Hama','Hama',
    'Datasalt Pangool','Pangool',
    'Apache Tez','Tez',
    'Apache DataFu','DataFu',
    'Pydoop',
    'Kangaroo',
    'TinkerPop',
    'Pachyderm MapReduce', 'PMR',
    'Apache Beam','Beam',
'NoSQL Database', 'Column Data Model',
    'Apache HBase','HBase',
    'Apache Cassandra','Cassandra',
    'Hypertable',
    'Apache Accumulo','Accumulo',
    'Apache Kudu','Kudu',
    'Apache Parquet','Parquet',
'NoSQL Database', 'Document Data Model',
    'MongoDB',
    'RethinkDB',
    'ArangoDB',
'NoSQL Database', 'Stream Data Model', 
    'EventStore',
'NoSQL Database', 'Key Value Data Model',
    'Redis DataBase','Redis',
    'Linkedin Voldemort','Voldemort',
    'RocksDB',
    'OpenTSDB',
'NoSQL Database', 'Graph Data Model',
    'ArangoDB',
    'Neo4j',
    'TitanDB',
'NewSQL Database',
    'TokuDB',
    'HandlerSocket',
    'Akiban Server','Akiban'
    'Drizzle',
    'Haeinsa',
    'SenseiDB',
    'Sky',
    'BayesDB',
    'InfluxDB',
'SQL On Hadoop',
    'Apache Hive','Hive',
    'Apache HCatalog','HCatalog',
    'Apache Trafodion','Trafodion',
    'Apache HAWQ','HAWQ',
    'Apache Drill','Drill',
    'Cloudera Impala','Impala',
    'Facebook Presto','Presto',
    'Datasalt Splout SQL','Splout SQL',
    'Apache Tajo','Tajo',
    'Apache Phoenix','Phoenix',
    'Apache MRQL','MRQL',
    'Kylin',
'Data Ingestion',
    'Apache Flume','Flume',
    'Apache Sqoop','Sqoop',
    'Facebook Scribe','Scribe',
    'Apache Chukwa','Chukwa',
    'Apache Kafka','Kafka',
    'Netflix Suro','Suro',
    'Apache Samza','Samza',
    'Cloudera Morphline','Morphline',
    'HIHO',
    'Apache NiFi','NiFi',
    'Apache ManifoldCF','ManifoldCF',
'Service Programming',
    'Apache Thrift','Thrift',
    'Apache Zookeeper','Zookeeper',
    'Apache Avro','Avro',
    'Apache Curator','Curator',
    'Apache karaf','karaf',
    'Twitter Elephant Bird','Elephant Bird',
    'Linkedin Norbert','Norbert',
'Scheduling & DR',
    'Apache Oozie','Oozie',
    'LinkedIn Azkaban','Azkaban',
    'Apache Falcon','Falcon',
    'Schedoscope',
'Machine Learning','ml','машинный обучение',
    'Apache Mahout','Mahout',
    'WEKA',
    'Cloudera Oryx','Oryx',
    'Deeplearning4j',
    'MADlib',
    'H2O',
    'Sparkling Water',
    'Apache SystemML','SystemML',
'Benchmarking', 'QA Tools',
    'Apache Hadoop Benchmarking','Hadoop Benchmarking',
    'Yahoo Gridmix3','Gridmix3',
    'PUMA Benchmarking','PUMA',
    'Berkeley SWIM Benchmark','SWIM',
    'Intel HiBench','HiBench',
    'Apache Yetus','Yetus',
'Security',
    'Apache Sentry','Sentry',
    'Apache Knox Gateway','Knox Gateway','Knox',
    'Apache Ranger','Ranger',
'Metadata Management',
    'Metascope',
'System Deployment',   
    'Apache Ambari','Ambari',
    'Cloudera HUE','HUE',
    'Apache Mesos','Mesos',
    'Myriad',
    'Marathon',
    'Brooklyn',
    'Hortonworks HOYA','HOYA',
    'Apache Helix','Helix',
    'Apache Bigtop','Bigtop',
    'Buildoop',
    'Deploop',
    'SequenceIQ Cloudbreak','Cloudbreak',
    'Apache Eagle','Eagle',
'Application',
    'Apache Nutch','Nutch',
    'Sphinx Search Server','Sphinx',
    'Apache OODT','OODT',
    'HIPI Library','HIPI',
    'PivotalR',
'Development Framework',
    'Jumbune',
    'Spring XD','XD',
    'Cask Data Application Platform','Cask',
'Categorize Pending',
    'Apache Fluo','Fluo',
    'Twitter Summingbird','Summingbird',
    'Apache Kiji','Kiji',
    'S4 Yahoo','S4',
    'Metamarkers Druid','Druid',
    'Concurrent Cascading','Cascading',
    'Concurrent Lingual','Lingual',
    'Concurrent Pattern','Pattern',
    'Apache Giraph','Giraph',
    'Talend',
    'Akka Toolkit','Akka',
    'Eclipse BIRT','BIRT',
    'Spango BI','Spango',
    'Jedox Palo','Palo',
    'Twitter Finagle','Finagle',
    'Intel GraphBuilder','GraphBuilder',
    'Apache Tika','Tika',
    'Apache Zeppelin','Zeppelin',
    
    
    'yandeх метрика', 'яндекс метрика', 'google analytics',
]


# In[2]:


# https://usefulstuff.io/big-data/
big_data_ecosystem2 = [
'Framework','фреймворк',#
    'Apache Hadoop','Hadoop',#: framework for distributed processing. Integrates MapReduce (parallel processing), YARN (job scheduling) and HDFS (distributed file system)
'Distributed Programming','распределенный программирование',#
    'AddThis Hydra','Hydra',#: distributed data processing and storage system originally developed at AddThis
    'Akela',#: Mozilla’s utility library for Hadoop, HBase, Pig, etc.
    'Amazon Lambda','Lambda',#: a compute service that runs your code in response to events and automatically manages the compute resources for you
    'Amazon SPICE','SPICE',#: Super-fast Parallel In-memory Calculation Engine
    'AMPcrowd',#: A RESTful web service that runs microtasks across multiple crowds
    'AMPLab G-OLA','G OLA',#: a novel mini-batch execution model that generalizes OLA to support general OLAP queries with arbitrarily nested aggregates using efficient delta maintenance techniques
    'AMPLab SIMR','SIMR',#: run Spark on Hadoop MapReduce v1
    'Apache Crunch','Crunch',#: a simple Java API for tasks like joining and data aggregation that are tedious to implement on plain MapReduce
    'Apache DataFu','DataFu',#: collection of user-defined functions for Hadoop and Pig developed by LinkedIn
    'Apache Flink','Flink',#: high-performance runtime, and automatic program optimization
    'Apache Gora','Gora',#: framework for in-memory data model and persistence
    'Apache Hama','Hama',#: BSP (Bulk Synchronous Parallel) computing framework
    'Apache Ignite','Ignite',#: high-performance, integrated and distributed in-memory platform for computing and transacting on large-scale data sets in real-time
    'Apache MapReduce','MapReduce',#: programming model for processing large data sets with a parallel, distributed algorithm on a cluster
    'Apache Pig','Pig',#: high level language to express data analysis programs for Hadoop
    'Apache S4','S4',#: framework for stream processing, implementation of S4
    'Apache Spark','Spark',#: framework for in-memory cluster computing
    'Apache Spark Streaming','Spark Streaming','Streaming',#: framework for stream processing, part of Spark
    'Apache Storm','Storm',#: framework for stream processing by Twitter also on YARN
    'Apache Tez','Tez',#: application framework for executing a complex DAG (directed acyclic graph) of tasks, built on YARN
    'Apache Twill','Twill',#: abstraction over YARN that reduces the complexity of developing distributed applications
    'Arvados',#: Spins a web of microservices around unsuspecting sysadmins
    'Blaze',#: Python users high-level access to efficient computation on inconveniently large data
    'Cascalog',#: data processing and querying library
    'Cheetah',#: High Performance, Custom Data Warehouse on Top of MapReduce
    'Concurrent Cascading','Cascading',#: framework for data management/analytics on Hadoop
    'Damballa Parkour','Parkour',#: MapReduce library for Clojure
    'Datasalt Pangool','Pangool',#: alternative MapReduce paradigm
    'DataTorrent StrAM','StrAM',#: real-time engine is designed to enable distributed, asynchronous, real time in-memory big-data computations in as unblocked a way as possible, with minimal overhead and impact on performance
    'DistributedR',#: scalable high-performance platform for the R language
    'Drools',#: a Business Rules Management System (BRMS) solution
    'eBay Oink','Oink',#: REST based interface for PIG execution
    'Esper',#: a highly scalable, memory-efficient, in-memory computing, SQL-standard, minimal latency, real-time streaming-capable Big Data processing engine for historical data
    'Facebook Corona','Corona',#: Hadoop enhancement which removes single point of failure
    'Facebook Peregrine','Peregrine',#: Map Reduce framework
    'Facebook Scuba','Scuba',#: distributed in-memory datastore
    'GearPump',#: a lightweight real-time big data streaming engine
    'Geotrellis',#: geographic data processing engine for high performance applications
    'GetStream Stream Framework','GetStream',#: a Python library, which allows you to build newsfeed and notification systems using Cassandra and/or Redis
    'GIS Tools for Hadoop','GIS Tools',#: Big Data Spatial Analytics for the Hadoop Framework
    'Google Dataflow','Dataflow',#: create data pipelines to help themæingest, transform and analyze data
    'Google FlumeJava','FlumeJava',#: Easy, Efficient Data-Parallel Pipelines. Base of Google Dataflow
    'Google MapReduce','MapReduce',#: map reduce framework
    'Google MillWheel','MillWheel',#: fault tolerant stream processing framework
    'GraphLab Dato','Dato',#: fast, scalable engine of GraphLab Create, a Python library
    'Hazelcast',#: In-Memory Data Grid
    'HParser',#: data parsing transformation environment optimized for Hadoop
    'IBM Streams','Streams',#: advanced analytic platform that allows user-developed applications to quickly ingest, analyze and correlate information as it arrives from thousands of real-time sources
    'JAQL',#: declarative programming language for working with structured, semi-structured and unstructured data
    'Kite',#: is a set of libraries, tools, examples, and documentation focused on making it easier to build systems on top of the Hadoop ecosystem
    'Kryo',#: Java serialization and cloning: fast, efficient, automatic
    'LinkedIn Cubert','Cubert',#: a fast and efficient batch computation engine for complex analysis and reporting of massive datasets on Hadoop
    'Lipstick',#: Pig workflow visualization tool
    'Metamarkers Druid','Druid',#: framework for real-time analysis of large datasets
    'Microsoft Azure Stream Analytics','Azure Stream Analytics','Azure Stream',#: an event processing engine that helps uncover real-time insights from devices, sensors, infrastructure, applications and data
    'Microsoft Orleans','Orleans',#: a straightforward approach to building distributed high-scale computing applications
    'Microsoft Project Orleans',#: a framework that provides a straightforward approach to building distributed high-scale computing applications
    'Microsoft Trill','Trill',#: a high-performance in-memory incremental analytics engine
    'Netflix Aegisthus','Aegisthus',#: Bulk Data Pipeline out of Cassandra. implements a reader for the SSTable format and provides a map/reduce program to create a compacted snapshot of the data contained in a column family
    'Netflix Lipstick','Lipstick',#: Pig Visualization framework
    'Netflix Mantis','Mantis',#: Event Stream Processing System
    'Netflix PigPen','PigPen',#: map-reduce for Clojure whiche compiles to Apache Pig
    'Netflix STAASH','STAASH',#: language-agnostic as well as storage-agnostic web interface for storing data into persistent storage systems
    'Netflix Surus','Surus',#: a collection of tools for analysis in Pig and Hive
    'Netflix Zeno','Zeno',#: Netflix’s In-Memory Data Propagation Framework
    'Nextflow',#: Dataflow oriented toolkit for parallel and distributed computational pipelines
    'Nokia Disco','Disco',#: MapReduce framework developed by Nokia
    'Oryx',#: is a realization of the lambda architecture built on Apache Spark and Apache Kafka, but with specialization for real-time large scale machine learning
    'Pachyderm',#: lets you store and analyze your data using containers.
    'Parsely Streamparse','Streamparse',#: streamparse lets you run Python code against real-time streams of data. It also integrates Python smoothly with Apache Storm.
    'PigPen',#: PigPen is map-reduce for Clojure, or distributed Clojure. It compiles to Apache Pig, but you don’t need to know much about Pig to use it
    'Pinterest Pinlater','Pinlater',#: asynchronous job execution system
    'Pubnub',#: Data stream network
    'Pydoop',#: Python MapReduce and HDFS API for Hadoop
    'ScaleOut hServer','hServer','ScaleOut',#: fast, scalable in-memory data grid for Hadoop
    'SeqPig',#: Simple and scalable scripting for large sequencing data set(ex: bioinfomation) in Hadoop
    'SigmoidAnalytics Spork','Spork',#: Pig on Apache Spark
    'SNAP',#: Stanford Network Analysis Platform is a general purpose, high performance system for analysis and manipulation of large networks
    'spark-dataflow','spark dataflow','dataflow',#: allows users to execute dataflow pipelines with Spark
    'SpatialHadoop',#: SpatialHadoop is a MapReduce extension to Apache Hadoop designed specially to work with spatial data.
    'Spring for Apache Hadoop','Spring',#: unified configuration model and easy to use APIs for using HDFS, MapReduce, Pig, and Hive
    'SQLStream Blaze','Blaze','SQLStream',#: stream processing platform
    'Stratio Crossdata', 'Crossdata',#: provides an unified way to access to multiple datastores
    'Stratio Decision','Decision',#: the union of a real-time messaging bus with a complex event processing engine using Spark Streaming
    'Stratio Streaming','Streaming',#: the union of a real-time messaging bus with a complex event processing engine using Spark Streaming
    'Stratosphere',#: general purpose cluster computing framework
    'Streamdrill',#: usefull for counting activities of event streams over different time windows and finding the most active one
    'Succinct Spark','Succinct',#: Enabling Queries on Compressed Data
    'Sumo Logic','Sumo',#: cloud based analyzer for machine-generated data.
    'Teradata QueryGrid','QueryGrid','Teradata',#: data-access layer that can orchestrate multiple modes of analysis across multiple databases plus Hadoop
    'TIBCO ActiveSpaces','ActiveSpaces',#: in-memory data grid
    'Tigon',#: a distributed framework built on Apache HadoopTM and Apache HBaseTM for real-time, high-throughput, low-latency data processing and analytics applications
    'Torch',#: Scientific computing for LuaJIT
    'Trident',#: a high-level abstraction for doing realtime computing on top of Storm
    'Twitter Crane','Crane',#: Java ETL
    'Twitter Gizzard','Gizzard',#: a flexible sharding framework for creating eventually-consistent distributed datastores
    'Twitter Heron','Heron',#: a realtime, distributed, fault-tolerant stream processing engine from Twitter
    'Twitter Scalding','Scalding',#: Scala library for Map Reduce jobs, built on Cascading
    'Twitter Summingbird','Summingbird',#: Streaming MapReduce with Scalding and Storm, by Twitter
    'Twitter TSAR','TSAR',#: TimeSeries AggregatoR by Twitter
'Distributed Filesystem','распределеный файловый система',#
    'Amazon Elastic File System','Elastic File System','Elastic',#: file storage service for Amazon Elastic Compute Cloud (Amazon EC2) instances
    'Amazon Simple Storage Service','Simple Storage Service',#: secure, durable, highly-scalable object storage
    'Apache HDFS','HDFS',#: a way to store large files across multiple machines
    'Apache Kudu','Kudu',#: completes Hadoop’s storage layer to enable fast analytics on fast data
    'BeeGFS',#: formerly FhGFS, parallel distributed file system
    'Ceph Filesystem',#: software storage platform designed
    'Disco DDFS','DDFS',#: distributed filesystem
    'Facebook Haystack','Haystack',#: object storage system
    'Google Cloud Storage',#: durable and highly available object storage
    'Google Cloud Storage Nearline','Nearline',#: a highly available, affordable solution for backup, archiving and disaster recovery.
    'Google Colossus','Colossus',#: distributed filesystem (GFS2)
    'Google GFS','GFS',#: distributed filesystem
    'Google Megastore','Megastore',#: scalable, highly available storage
    'GridGain',#: GGFS, Hadoop compliant in-memory file system
    'HDSF-DU','HDSF DU',#: HDFS-DU is an interactive visualization of the Hadoop distributed file system.
    'Lustre file system','Lustre',#: high-performance distributed filesystem
    'MapR-FS','MapR FS'#: Distributed filesystem from MapR
    'Microsoft Azure Data Lake','Azure Data Lake',#: a hyper scale repository for big data analytic workloads
    'Netflix S3mper','S3mper',#: library that provides an additional layer of consistency checking on top of Amazon’s S3 index through use of a consistent, secondary index
    'Quantcast File System QFS','Quantcast','QFS',#: open-source distributed file system
    'Red Hat GlusterFS','GlusterFS',#: scale-out network-attached storage file system
    'Tachyon',#: reliable file sharing at memory speed across cluster frameworks
'Key-Map Data Model','Key Map Data Model',#
    'Actian Vector','Vector',#: column-oriented analytic database
    'Apache Accumulo','Accumulo',#: distribuited key/value store, built on Hadoop
    'Apache Cassandra','Cassandra',#: column-oriented distribuited datastore, inspired by BigTable
    'Apache HBase','HBase',#: column-oriented distribuited datastore, inspired by BigTable
    'Facebook HydraBase','HydraBase',#: evolution of HBase made by Facebook
    'Google BigTable','BigTable',#: column-oriented distributed datastore
    'Google Cloud Datastore','Datastore',#: is a fully managed, schemaless database for storing non-relational data over BigTable
    'Hypertable',#: column-oriented distribuited datastore, inspired by BigTable
    'InfiniDB',#: is accessed through a MySQL interface and use massive parallel processing to parallelize queries
    'MapR-DB','MapR DB',#: fast, scalable, and enterprise-ready in-Hadoop database architected to manage big data
    'Netflix Priam','Priam',#: Co-Process for backup/recovery, Token Management, and Centralized Configuration management for Cassandra
    'OhmData C5','C5',#: improved version of HBase
    'Palantir AtlasDB','AtlasDB',#: a massively scalable datastore and transactional layer that can be placed on top of any key-value store to give it ACID properties
    'Sqrrl',#: NoSQL databases on top of Apache Accumulo
    'Stratio Cassandra','Cassandra',#: Cassandra index functionality has been extended to provide near real time search such as ElasticSearch or Solr, including full text search capabilities and multivariable, geospatial and bitemporal search
    'Tephra',#: Transactions for HBase
    'Twitter Manhattan','Manhattan',#: real-time, multi-tenant distributed database for Twitter scale
'Document Data Model',#
    'Actian Versant','Versant',#: commercial object-oriented database management systems
    'Amazon SimpleDB','SimpleDB'#: a highly available and flexible non-relational data store that offloads the work of database administration
    'BigchainDB',#: The scalable blockchain database.
    'Clusterpoint',#: a database software for high-speed storage and large-scale processing of XML and JSON data on clusters of commodity hardware
    'Crate Data',#: is an open source massively scalable data store. It requires zero administration
    'Facebook Apollo','Apollo',#: Facebook’s Paxos-like NoSQL database
    'jumboDB',#: document oriented datastore over Hadoop
    'LinkedIn Ambry','Ambry',#: Distributed object store
    'LinkedIn Espresso','Espresso',#: horizontally scalable document-oriented NoSQL data store
    'MarkLogic',#: Schema-agnostic Enterprise NoSQL database technology
    'Microsoft DocumentDB','DocumentDB',#: fully-managed, highly-scalable, NoSQL document database service
    'Microsoft StorSimple','StorSimple',#: a unique hybrid cloud storage solution that lowers costs and improves data protection
    'MongoDB',#: Document-oriented database system
    'RavenDB',#: A transactional, open-source Document Database
    'RethinkDB',#: document database that supports queries like table joins and group by
    'Terrastore',#: a modern document store which provides advanced scalability and elasticity features without sacrificing consistency
    'TokuMX',#: High-Performance MongoDB Distribution
    'Tokutek',#: Tokutek claims to improve MongoDB performance 20x
'Key-value Data Model','Key value Data Model'#
    'Aerospike',#: NoSQL flash-optimized, in-memory. Open source and “Server code in ‘C’ (not Java or Erlang) precisely tuned to avoid context switching and memory copies.
    'Amazon DynamoDB','DynamoDB',#: distributed key/value store, implementation of Dynamo paper
    'Couchbase ForestDB','ForestDB',#: Fast Key-Value Storage Engine Based on Hierarchical B+-Tree Trie
    'Edis',#: is a protocol-compatible Server replacement for Redis
    'ElephantDB',#: Distributed database specialized in exporting data from Hadoop
    'EventStore',#: distributed time series database
    'Exasolution',#: an in-memory, column-oriented, relational database management system
    'HyperDex',#: next generation key-value store
    'KAI',#: a distributed key-value datastore
    'LinkedIn Krati','Krati',#: is a simple persistent data store with very low latency and high throughput
    'Linkedin Voldemort','Voldemort',#: distributed key/value storage system
    'MemcacheDB',#: a distributed key-value storage system designed for persistent
    'Netflix Dynomite','Dynomite',#: thin Dynamo-based replication for cached data
    'Oracle NoSQL Database','NoSQL Database','NoSQL','Oracle NoSQL',#: distributed key-value database by Oracle Corporation
    'QDB',#: A fast, high availability, fully Redis compatible store
    'RAMCloud',#: storage system that provides large-scale low-latency storage by keeping all data in DRAM all the time and aggregating the main memories of thousands of servers
    'RebornDB',#: Distributed database fully compatible with redis protocol
    'Redis',#: in memory key value datastore
    'Redis Cluster',#: distributed implementation of Redis
    'Redis Sentinel','Sentinel',#: system designed to help managing Redis instances
    'Riak',#: a decentralized datastore
    'Scalaris',#: a distributed transactional key-value store
    'Storehaus',#: library to work with asynchronous key value stores, by Twitter
    'Tarantool',#: an efficient NoSQL database and a Lua application server
    'TreodeDB',#: key-value store that’s replicated and sharded and provides atomic multirow writes
    'Yahoo Sherpa','Sherpa',#: hosted, distributed and geographically replicated key-valueÊcloud storage platform
'Graph Data Model',#
    'Apache Giraph','Giraph',#: implementation of Pregel, based on Hadoop
    'Apache Spark Bagel','Bagel',#: implementation of Pregel, part of Spark
    'ArangoDB',#: multi model distribuited database
    'Doradus',#: Doradus is a REST service that extends a Cassandra NoSQL database with a graph-based data model, advanced indexing and search features, and a REST API
    'Facebook TAO','TAO',#: TAO is the distributed data store that is widely used at facebook to store and serve the social graph
    'Faunus',#: Hadoop-based graph analytics engine for analyzing graphs represented across a multi-machine compute cluster
    'Google Cayley','Cayley',#: open-source graph database
    'Google Pregel','Pregel',#: graph processing framework
    'GraphLab PowerGraph','PowerGraph',#: a core C++ GraphLab API and a collection of high-performance machine learning and data mining toolkits built on top of the GraphLab API
    'GraphX',#: resilient Distributed Graph System on Spark
    'Gremlin',#: graph traversal Language
    'HyperGraphDB',#: general purpose, open-source data storage mechanism based on a powerful knowledge management formalism known as directed hypergraphs
    'InfiniteGraph',#: distributed graph database
    'Infovore',#: RDF-centric Map/Reduce framework
    'Intel GraphBuilder','GraphBuilder',#: tools to construct large-scale graphs on top of Hadoop
    'MapGraph',#: Massively Parallel Graph processing on GPUs
    'Mazerunner for Neo4j','Mazerunner',#: extends a Neo4j graph database to run scheduled big data graph compute algorithms at scale with HDFS and Apache Spark.
    'MemGraph',#: cypher compatibile, high-performance in-memory transactional and real-time analytics graph database
    'Microsoft Graph Engine',#: a distributed, in-memory, large graph processing engine, underpinned by a strongly-typed RAM store and a general computation engine
    'Neo4j',#: graph database writting entirely in Java
    'OrientDB',#: document and graph database
    'Phoebus',#: framework for large scale graph processing
    'Pinterest Zen','Zen',#: Pinterest’s Graph Storage Service
    'Sparksee',#: scalable high-performance graph database
    'Stardog',#: graph database: search, query, reasoning, and constraints in a lightweight, pure Java system
    'Titan',#: distributed graph database, built over Cassandra
    'Twitter FlockDB','FlockDB',#: distribuited graph database
'NewSQL Database','NewSQL db','NewSQL',#
    'Actian Ingres','Ingres',#: commercially supported, open-source SQL relational database management system
    'BayesDB',#: statistic oriented SQL database
    'Cockroach',#: Scalable, Geo-Replicated, Transactional Datastore
    'Datomic',#: distributed database designed to enable scalable, flexible and intelligent applications
    'FoundationDB',#: distributed database, inspired by F1
    'Google F1','F1',#: distributed SQL database built on Spanner
    'Google Spanner','Spanner',#: globally distributed semi-relational database
    'H-Store','H Store',#: is an experimental main-memory, parallel database management system that is optimized for on-line transaction processing (OLTP) applications
    'HandlerSocket',#: NoSQL plugin for MySQL/MariaDB
    'IBM DB2','DB2',#: object-relational database management system
    'InfiniSQL',#: infinity scalable RDBMS
    'MemSQL',#: in memory SQL database witho optimized columnar storage on flash
    'NuoDB',#: SQL/ACID compliant distributed database
    'Oracle Database','Oracle',#: object-relational database management system
    'Oracle TimesTen in-Memory Database','TimesTen',#: in-memory, relational database management system with persistence and recoverability
    'Pivotal GemFire XD','GemFire XD','XD',#: Low-latency, in-memory, distributed SQL data store. Provides SQL interface to in-memory table data, persistable in HDFS
    'SAP HANA','HANA',#: is an in-memory, column-oriented, relational database management system
    'Segment SQL',#: Track your customer data to Amazon Redshift
    'SenseiDB',#: distributed, realtime, semi-structured database
    'Sky',#: database used for flexible, high performance analysis of behavioral data
    'SymmetricDS',#: open source software for both file and database synchronization
    'Teradata Database','Teradata',#: complete relational database management system
    'VoltDB',#: in-memory NewSQL database
'Columnar Database','Columnar db',#
    'Amazon RedShift','RedShift',#: data warehouse service, based on PostgreSQL
    'Apache Arrow','Arrow',#: Powering Columnar In-Memory Analytics
    'C-Store','C Store',#: column oriented DBMS
    'Google BigQuery','BigQuery',#: framework for interactive analysis, implementation of Dremel
    'Google Dremel','Dremel',#: framework for interactive analysis, implementation of Dremel
    'MonetDB',#: column store database
    'Parquet',#: columnar storage format for Hadoop
    'Pivotal Greenplum','Greenplum',#: purpose-built, dedicated analytic data warehouse
    'Vertica',#: is designed to manage large, fast-growing volumes of data and provide very fast query performance when used for data warehouses
'Time-Series Database','Time Series Database', 'TSDB',#
    'Chronix',#: fast and efficient time series storage based on Apache Lucene and Apache Solr
    'Cube',#: uses MongoDB to store time series data
    'Etsy StatsD','StatsD',#: simple daemon for easy stats aggregation
    'InfluxDB',#: distributed time series database
    'Kairos',#: Time series data storage in Redis, Mongo, SQL and Cassandra
    'Kairosdb',#: similar to OpenTSDB but allows for Cassandra
    'OpenTSDB',#: distributed time series database on top of HBase
    'Prometheus',#: an open-source service monitoring system and time series database
    'Square Cube',#: system for collecting timestamped events and deriving metrics
    'TempoIQ',#: Cloud-based sensor analytics
'SQL-like processing','SQL like processing',#
    'Actian SQL for Hadoop','Actian SQL',#: high performance interactive SQL access to all Hadoop data
    'Adabas',#: ADABAS was NoSQL from a time when there was no SQL
    'Akiban',#: Touted as SQL database with object structured storage
    'AMPLAB Shark','Shark',#: data warehouse system for Spark
    'Apache Drill','Drill',#: framework for interactive analysis, inspired by Dremel
    'Apache HCatalog','HCatalog',#: table and storage management layer for Hadoop
    'Apache Hive','Hive',#: SQL-like data warehouse system for Hadoop
    'Apache Optiq','Optiq',#: framework that allows efficient translation of queries involving heterogeneous and federated data
    'Apache Phoenix','Phoenix',#: SQL skin over HBase
    'BlinkDB',#: massively parallel, approximate query engine
    'Brytlyt',#: a fully enabled GPGPU database which allows for offloading of database operations to General Processing on Graphics Processor Units.
    'Cloudera Impala','Impala',#: framework for interactive analysis, Inspired by Dremel
    'Concurrent Lingual','Lingual',#: SQL-like query language for Cascading
    'Datasalt Splout SQL','Splout SQL',#: full SQL query engine for big datasets
    'eBay Kylin','Kylin',#: Distributed Analytics Engine from eBay Inc. that provides SQL interface and multi-dimensional analysis (OLAP) on Hadoop supporting extremely large datasets
    'Facebook PrestoDB','PrestoDB',#: distributed SQL query engine
    'Hadapt',#: a native implementation of SQL for the Apache Hadoop open-source project
    'Hekaton',#: Refer to lock-free architecture for SQL Server 2014
    'JethroData',#: index-based SQL engine for Hadoop
    'Metanautix Quest',#: data compute engine
    'Pivotal HAWQ','HAWQ',#: SQL-like data warehouse system for Hadoop
    'RainstorDB',#: database for storing petabyte-scale volumes of structured and semi-structured data
    'Spark Catalyst','Catalyst',#: is a Query Optimization Framework for Spark and Shark
    'SparkSQL',#: Manipulating Structured Data Using Spark
    'Splice Machine',#: a full-featured SQL-on-Hadoop RDBMS with ACID transactions
    'Stinger',#: interactive query for Hive
    'Tajo',#: distributed data warehouse system on Hadoop
    'Trafodion',#: enterprise-class SQL-on-HBase solution targeting big data transactional or operational workloads
'Integrated Development Environment',#
    'R-Studio','R Studio',#: IDE for R
'Data Ingestion',#
    'Amazon Kinesis','Kinesis',#: real-time processing of streaming data at massive scale
    'Amazon Snowball','Snowball',#: a petabyte-scale data transport solution that uses secure appliances to transfer large amounts of data into and out of AWS
    'AMPLab SampleClean','SampleClean',#: scalable techniques for data cleaning and statistical inference on dirty data
    'Apache BookKeeper','BookKeeper',#: a distributed logging service called BookKeeper and a distributed publish/subscribe system built on top of BookKeeper called Hedwig
    'Apache Chukwa','Chukwa',#: data collection system
    'Apache Flume','Flume',#: service to manage large amount of log data
    'Apache Samza','Samza',#: stream processing framework, based on Kafla and YARN
    'Apache Sqoop','Sqoop',#: tool to transfer data between Hadoop and a structured datastore
    'Apache UIMA','UIMA',#: Unstructured Information Management applications are software systems that analyze large volumes of unstructured information in order to discover knowledge that is relevant to an end user
    'Cloudera Morphlines','Morphlines',#: framework that help ETL to Solr, HBase and HDFS
    'Facebook Scribe','Scribe',#: streamed log data aggregator
    'Fluentd',#: tool to collect events and logs
    'Google Photon','Photon',#: geographically distributed system for joining multiple continuously flowing streams of data in real-time with high scalability and low latency
    'Heka',#: open source stream processing software system
    'HIHO',#: framework for connecting disparate data sources with Hadoop
    'LinkedIn Camus','Camus',#: Kafka to HDFS pipeline. It is a mapreduce job that does distributed data loads out of Kafka
    'LinkedIn Databus','Databus',#: stream of change capture events for a database
    'LinkedIn Gobblin','Gobblin',#: a framework for Solving Big Data Ingestion Problem
    'LinkedIn Kamikaze','Kamikaze',#: utility package for compressing sorted integer arrays
    'Linkedin Lumos','Lumos',#: bridge from OLTP to OLAP for use it on Hadoop
    'LinkedIn White Elephant','White Elephant',#: log aggregator and dashboard
    'Logstash',#: a tool for managing events and logs
    'Netflix Ribbon','Ribbon',#: a Inter Process Communication (remote procedure calls) library with built in software load balancers. The primary usage model involves REST calls with various serialization scheme support
    'Netflix Suro','Suro',#: data pipeline service for collecting, aggregating, and dispatching large volume of application events including log data based on Chukwa
    'Pinterest Secor','Secor',#: is a service implementing Kafka log persistance
    'Record Breaker',#: Automatic structure for your text-formatted data
    'Sawmill',#: extensive log processing and reporting features
    'Stratio Ingestion','Ingestion',#: Apache Flume with steroids
    'TIBCO Enterprise Message Service','TIBCO',#: standards-based messaging middleware
    'Twitter Zipkin','Zipkin',#: distributed tracing system that helps us gather timing data for all the disparate services at Twitter
    'Vibe Data Stream',#: streaming data collection for real-time Big Data analytics
'Message-oriented middleware','Message oriented middleware',#
    'ActiveMQ',#: open source messaging and Integration Patterns server
    'Amazon Simple Queue Service','Simple Queue Service',#: fast, reliable, scalable, fully managed queue service
    'Apache Kafka','Kafka',#: distributed publish-subscribe messaging system
    'Apache Qpid','Qpid',#: messaging tools that speak AMQP and support many languages and platforms
    'Apcera NATS','NATS',#: an open-source, high-performance, lightweight cloud native messaging system
    'Apollo',#: ActiveMQ’s next generation of messaging
    'Azure Event Hubs','Event Hubs',#: a highly scalable publish-subscribe event ingestor
    'Beanstalkd',#: simple, fast work queue
    'Bit.ly NSQ','NSQ',#: realtime distributed message processing at scale
    'Celery',#: Distributed Task Queue
    'Crossroads I/O','Crossroads',#: library for building scalable and high performance distributed applications
    'Darner',#: simple, lightweight message queue
    'Facebook Iris','Iris',#: a totally ordered queue of messaging updates with separate pointers into the queue indicating the last update sent to your Messenger app and the traditional storage tier
    'Gearman',#: Job Server
    'Google Cloud Pub/Sub','Pub/Sub',#: reliable, many-to-many, asynchronous messaging hosted on Google’s infrastructure
    'Google Pub/Sub',#: reliable, many-to-many, asynchronous messaging hosted on Google’s infrastructure
    'HornetQ',#: open source project to build a multi-protocol, embeddable, very high performance, clustered, asynchronous messaging system
    'IronMQ',#: easy-to-use highly available message queuing service
    'Kestrel',#: distributed message queue system
    'Marconi',#: queuing and notification service made by and for OpenStack, but not only for it
    'RabbitMQ',#: Robust messaging for applications
    'RestMQ',#: message queue which uses HTTP as transport, JSON to format a minimalist protocol and is organized as REST resources
    'RQ',#: simple Python library for queueing jobs and processing them in the background with workers
    'Sidekiq',#: Simple, efficient background processing for Ruby
    'ZeroMQ',#: The Intelligent Transport Layer
'Service Programming',#
    'Akka Toolkit','Akka',#: runtime for distributed, and fault tolerant event-driven applications on the JVM
    'Apache Avro','Avro',#: data serialization system
    'Apache Curator','Curator',#: Java libaries for Apache ZooKeeper
    'Apache Karaf','Karaf',#: OSGi runtime that runs on top of any OSGi framework
    'Apache Thrift','Thrift',#: framework to build binary protocols
    'Apache Zookeeper','Zookeeper',#: centralized service for process management
    'Google Chubby','Chubby',#: a lock service for loosely-coupled distributed systems
    'Linkedin Norbert','Norbert',#: cluster manager
    'MPICH',#: high performance and widely portable implementation of the Message Passing Interface (MPI) standard
    'OpenMPI',#: message passing framework
    'Serf',#: decentralized solution for service discovery and orchestration
    'Spotify Luigi','Luigi',#: a Python package for building complex pipelines of batch jobs. It handles dependency resolution, workflow management, visualization, handling failures, command line integration, and much more
    'Spring XD','XD',#: distributed and extensible system for data ingestion, real time analytics, batch processing, and data export
    'Twitter Elephant Bird','Elephant Bird',#: libraries for working with LZOP-compressed data
    'Twitter Finagle','Finagle',#: asynchronous network stack for the JVM
'Scheduling',#
    'AirBnB Airflow','Airflow',#: AirFlow is a system to programmatically author, schedule and monitor data pipelines
    'Apache Aurora','Aurora',#: is a service scheduler that runs on top of Apache Mesos
    'Apache Falcon','Falcon',#: data management framework
    'Apache Oozie','Oozie',#: workflow job scheduler
    'Chronos',#: distributed and fault-tolerant scheduler
    'Linkedin Azkaban','Azkaban',#: batch workflow job scheduler
    'Pinterest Pinball','Pinball',#: customizable platform for creating workflow managers
    'Sparrow',#: scheduling platform
'Machine Learning',#
    'Amazon Machine Learning','Amazon ML',#: visualization tools and wizards that guide you through the process of creating machine learning (ML) models without having to learn complex ML algorithms and technology
    'AMPLab Splash','Splash',#: a general framework for parallelizing stochastic learning algorithms on multi-node clusters
    'AMPLab Velox','Velox',#: a data management system for facilitating the next steps in real-world, large-scale analytics pipelines
    'Apache Mahout','Mahout',#: machine learning library for Hadoop
    'Ayasdi Core',#: tool for topological data analysis
    'brain',#: Neural networks in JavaScript
    'Caffe',#: a deep learning framework made with expression, speed, and modularity in mind. It is developed by the Berkeley Vision and Learning Cente
    'Cloudera Oryx','Oryx',#: real-time large-scale machine learning
    'Concurrent Pattern',#: machine learning library for Cascading
    'convnetjs',#: Deep Learning in Javascript. Train Convolutional Neural Networks (or ordinary ones) in your browser
    'cuDNN',#: GPU-accelerated library of primitives for deep neural networks
    'Decider',#: Flexible and Extensible Machine Learning in Ruby
    'DeepCL',#: OpenCL library to train deep convolutional neural networks
    'etcML',#: text classification with machine learning
    'Etsy Conjecture','Conjecture',#: scalable Machine Learning in Scalding
    'Facebook DeepText','DeepText',#: a deep learning-based text understanding engine that can understand with near-human accuracy the textual content of several thousands posts per second, spanning more than 20 languages
    'Facebook FBLearner Flow','FBLearner Flow','FBLearner',#: provides innovative functionality, like automatic generation of UI experiences from pipeline definitions and automatic parallelization of Python code using futures
    'fbcunn',#: Deep Learning CUDA Extensions from Facebook AI Research
    'Google DistBelief','DistBelief',#: software framework that can utilize computing clusters with thousands of machines to train large models
    'Google Sibyl','Sibyl',#: System for Large Scale Machine Learning at Google
    'Google TensorFlow','TensorFlow',#: an Open Source Software Library for Machine Intelligence
    'H2O',#: statistical, machine learning and math runtime for Hadoop
    'IBM Watson','Watson',#: cognitive computing system
    'KeystoneML',#: Simplifying robust end-to-end machine learning on Apache Spark
    'LinkedIn FeatureFu','FeatureFu',#: contains a collection of library/tools for advanced feature engineering to derive features on top of other features, or convert a light weighted model into a feature
    'LinkedIn ml-ease','ml ease',#: ADMM based large scale logistic regression
    'Microsoft Azure Machine Learning','Azure ML',#: is built on the machine learning capabilities already available in several Microsoft products including Xbox and Bing and using predefined templates and workflows
    'Microsoft CNTK','CNTK',#: Computational Network Toolkit
    'MLbase',#: distributed machine learning libraries for the BDAS stack
    'MLPNeuralNet',#: Fast multilayer perceptron neural network library for iOS and Mac OS X
    'Neon',#: a highly configurable deep learning framework
    'nupic',#: Numenta Platform for Intelligent Computing: a brain-inspired machine intelligence platform, and biologically accurate neural network based on cortical learning algorithms
    'OpenAI Gym',#: a toolkit for developing and comparing reinforcement learning algorithms
    'PredictionIO',#: machine learning server buit on Hadoop, Mahout and Cascading
    'scikit-learn','scikit learn',#: scikit-learn: machine learning in Python
    'Seldon',#: an open source predictive analytics platform based upon Spark, Kafka and Hadoop
    'Spark MLlib','MLlib',#: a Spark implementation of some common machine learning (ML) functionality
    'Sparkling Water',#: combine H2OÕs Machine Learning capabilities with the power of the Spark platform
    'SparkNet',#: Distributed Neural Networks for Spark
    'Theano',#: Python package for deep learning that can utilize NVIDIA’s CUDA toolkit to run on the GPU
    'Thunder',#: Large-scale analysis of neural data
    'Vahara',#: Machine learning and natural language processing with Apache Pig
    'Velox',#: a system for serving machine learning predictions
    'Viv',#: global platform that enables developers to plug into and create an intelligent, conversational interface to anything
    'Vowpal Wabbit','Wabbit',#: learning system sponsored by Microsoft and Yahoo!
    'WEKA',#: suite of machine learning software
    'Wit',#: Natural Language for the Internet of Things
    'Wolfram Alpha','Alpha',#: computational knowledge engine
    'YHat ScienceOps','ScienceOps',#: platform for deploying, managing, and scaling predictive models in production applications
'Benchmarking',#
    'Apache Hadoop Benchmarking','Hadoop Benchmarking',#: micro-benchmarks for testing Hadoop performances
    'Berkeley SWIM Benchmark','SWIM Benchmark',#: real-world big data workload benchmark
    'Big-Bench','Big Bench,'#: Big Bench Workload Development
    'Hive-benchmarks','Hive benchmarks',#: some benchmarking queries for Apache Hive
    'Hive-testbench','Hive testbench',#: Testbench for experimenting with Apache Hive at any data scale.
    'Intel HiBench','HiBench',#: a Hadoop benchmark suite
    'Mesosaurus',#: Mesos task load simulator framework for (cluster and Mesos) performance analysis
    'Netflix Inviso','Inviso',#: performance focused Big Data tool
    'PUMA Benchmarking','PUMA',#: benchmark suite for MapReduce applications
    'Yahoo Gridmix3','Gridmix3',#: Hadoop cluster benchmarking from Yahoo engineer team
'Security'
    'Apache Knox Gateway','Knox Gateway','Knox',#: single point of secure access for Hadoop clusters
    'Apache Ranger','Ranger',#: framework to enable, monitor and manage comprehensive data security across the Hadoop platform (formerly called Apache Argus)
    'Apache Sentry','Sentry',#: security module for data stored in Hadoop
    'PacketPig',#: Open Source Big Data Security Analytics
    'Voltage SecureData','SecureData',#: data protection framework
'System Deployment',#
    'Ankush',#: A big data cluster management tool that creates and manages clusters of different technologies.
    'Apache Ambari','Ambari',#: operational framework for Hadoop mangement
    'Apache Bigtop','Bigtop',#: system deployment framework for the Hadoop ecosystem
    'Apache Helix','Helix',#: cluster management framework
    'Apache Mesos','Mesos',#: cluster manager
    'Apache Slider','Slider',#: is a YARN application to deploy existing distributed applications on YARN
    'Apache Whirr','Whirr',#: set of libraries for running cloud services
    'Apache YARN','YARN',#: Cluster manager
    'Brooklyn',#: library that simplifies application deployment and management
    'Buildoop',#: Similar to Apache BigTop based on Groovy language
    'Cloudera Director',#: a comprehensive data management platform with the flexibility and power to evolve with your business
    'Cloudera HUE','HUE',#: web application for interacting with Hadoop
    'CloudPhysics',#: collect operational metadata from your virtualized infrastructure, then correlate and analyze it to expose operational hazards and waste that pose a threat to your datacenter performance, efficiency and uptime
    'Deimos',#: Mesos containerizer hooks for Docker
    'Develoop',#: tool for provisioning, managing and monitoring Apache Hadoop
    'Etsy Sahale','Sahale',#: Visualizing Cascading Workflows at Etsy
    'Facebook Autoscale','Autoscale',#: the load balancer will concentrate workload to a server until it has at least a medium-level workload
    'Facebook Prism','Prism',#: multi datacenters replication system
    'Ganglia Monitoring System','Ganglia',#: scalable distributed monitoring system for high-performance computing systems such as clusters and Grids
    'Genie',#: Genie provides REST-ful APIs to run Hadoop, Hive and Pig jobs, and to manage multiple Hadoop resources and perform job submissions across them.
    'Google Borg','Borg',#: job scheduling and monitoring system
    'Google Omega','Omega',#: job scheduling and monitoring system
    'Hannibal',#: Hannibal is tool to help monitor and maintain HBase-Clusters that are configured for manual splitting.
    'Hortonworks HOYA','HOYA',#: application that can deploy HBase cluster on YARN
    'Jumbune',#: Jumbune is an open-source product built for analyzing Hadoop cluster and MapReduce jobs.
    'Marathon',#: Mesos framework for long-running services
    'Minotaur',#: scripts/recipes/configs to spin up VPC-based infrastructure in AWS from scratch and deploy labs to it
    'Myriad',#: a mesos framework designed for scaling YARN clusters on Mesos. Myriad can expand or shrink one or more YARN clusters in response to events as per configured rules and policies.
    'Neflix SimianArmy','SimianArmy',#: a suite of tools for keeping your cloud operating in top form
    'Netflix Eureka','Eureka',#: AWS Service registry for resilient mid-tier load balancing and failover
    'Netflix Hystrix','Hystrix',#: a latency and fault tolerance library designed to isolate points of access to remote systems, services and 3rd party libraries, stop cascading failure and enable resilience in complex distributed systems where failure is inevitable
    'Scaling Data',#: tracing data center problems to root cause, predict capacity issues, identify emerging failures and highlight latent threats
    'Stratio Manager',#: install, manage and monitor all the technology stack related to the Stratio Platform
    'Tumblr Collins','Collins',#: Infrastructure management for engineers
    'Tumblr Genesis','Genesis',#: a tool for data center automation
'Container Manager',#
    'Amazon EC2 Container Service','EC2',#: a highly scalable, high performance container management service that supports Docker containers
    'CoreOS Fleet',#: cluster management tool from CoreOS
    'Docker',#: an open platform for developers and sysadmins to build, ship, and run distributed applications
    'Docker Swarm','Swarm',#: native clustering for Docker
    'Fig',#: fast, isolated development environments using Docker
    'Google Container Engine',#: Run Docker containers on Google Cloud Platform, powered by Kubernetes
    'HashiCorp Nomad','Nomad',#: a Distributed, Highly Available, Datacenter-Aware Scheduler
    'Kubernetes',#: open source implementation of container cluster management
    'Pumba',#: Chaos testing tool for Docker
    'Rocket',#: an alternative to the Docker runtime, designed for server environments with the most rigorous security and production requirements
'Application',#
    'Adobe Spindle','Spindle',#: Next-generation web analytics processing with Scala, Spark, and Parquet
    'Apache Kiji','Kiji',#: framework to collect and analyze data in real-time, based on HBase
    'Apache Nutch','Nutch',#: open source web crawler
    'Apache OODT','OODT',#: capturing, processing and sharing of data for NASA’s scientific archives
    'Apache Tika','Tika',#: content analysis toolkit
    'Domino',#: Run, scale, share, and deploy models Ñ without any infrastructure.
    'Eclipse BIRT','BIRT',#: Eclipse-based reporting system
    'Eventhub',#: open source event analytics platform
    'HIPI Library','HIPI',#: API for performing image processing tasks on Hadoop’s MapReduce
    'Hunk',#: Splunk analytics for Hadoop
    'MADlib',#: data-processing library of an RDBMS to analyze data
    'PivotalR',#: R on Pivotal HD / HAWQ and PostgreSQL
    'Qubole',#: auto-scaling Hadoop cluster, built-in data connectors
    'Sense',#: Cloud Platform for Data Science and Big Data Analytics
    'Snowplow',#: enterprise-strength web and event analytics, powered by Hadoop, Kinesis, Redshift and Postgres
    'SparkR',#: R frontend for Spark
    'Splunk',#: analyzer for machine-generated date
    'Talend',#: unified open source environment for YARN, Hadoop, HBASE, Hive, HCatalog & Pig
'Search engine','Search framework',#
    'Algolia',#: Hosted Search API that delivers instant and relevant results from the first keystroke
    'Apache Blur','Blur',#: a search engine capable of querying massive amounts of structured data at incredible speeds
    'Apache Lucene','Lucene',#: Search engine library
    'Apache Solr','Solr',#: Search platform for Apache Lucene
    'ElasticSearch',#: Search and analytics engine based on Apache Lucene
    'Elasticsearch Hadoop',#: Elasticsearch real-time search and analytics natively integrated with Hadoop. Supports Map/Reduce, Cascading, Apache Hive and Apache Pig.
    'Enigma.io',#: Freemium robust web application for exploring, filtering, analyzing, searching and exporting massive datasets scraped from across the Web
    'Facebook Unicorn','Unicorn',#: social graph search platform
    'Google Caffeine','Caffeine',#: continuous indexing system
    'Google Percolator','Percolator',#: continuous indexing system
    'TeraGoogle',#: large search index
    'Haeinsa',#: linearly scalable multi-row, multi-table transaction library for HBase based on Percolator
    'HBase Coprocessor','Coprocessor',#: implementation of Percolator, part of HBase
    'hIndex',#: Secondary Index for HBase
    'SF1R Search Engine','SF1R',#: distributed search engine written in c++
    'Lily HBase Indexer','HBase Indexer',#: quickly and easily search for any content stored in HBase
    'LinkedIn Bobo','Bobo',#: is a Faceted Search implementation written purely in Java, an extension to Apache Lucene
    'LinkedIn Cleo','Cleo',#: is a flexible software library for enabling rapid development of partial, out-of-order and real-time typeahead search
    'LinkedIn Galene','Galene',#: search architecture at LinkedIn
    'LinkedIn Zoie','Zoie',#: is a realtime search/indexing system written in Java
    'Sphinx Search Server',#: fulltext search engine
'MySQL fork','MySQL evolution',#
    'Amazon Aurora','Aurora',#: a MySQL-compatible, relational database engine that combines the speed and availability of high-end commercial databases with the simplicity and cost-effectiveness of open source databases
    'Amazon RDS','RDS',#: MySQL databases in Amazon’s cloud
    'BigObject',#: Real-time Computing Engine Designed for Big Data
    'Drizzle',#: evolution of MySQL 6.0
    'Galera Cluster',#: a synchronous multi-master cluster for MySQL, Percona and MariaDB
    'Google Cloud SQL',#: MySQL databases in Google’s cloud
    'HiveDB',#: an open source framework for horizontally partitioning MySQL systems
    'MariaDB',#: enhanced, drop-in replacement for MySQL
    'MySQL Cluster',#: MySQL implementation using NDB Cluster storage engine providing shared-nothing clustering and auto-sharding
    'Percona Server',#: enhanced, drop-in replacement for MySQL
    'ProxySQL',#: High Performance Proxy for MySQL
    'TiDB',#: a distributed SQL database inspired by the design of Google F1
    'TokuDB',#: TokuDB is a storage engine for MySQL and MariaDB
    'WebScaleSQL',#: is a collaboration among engineers from several companies that face similar challenges in running MySQL at scale
    'Youtube Vitess','Vitess',#: provides servers and tools which facilitate scaling of MySQL databases for large scale web services
'PostgreSQL fork','PostgreSQL evolution',#
    'HadoopDB',#: hybrid of MapReduce and DBMS
    'IBM Netezza','Netezza',#: high-performance data warehouse appliances
    'Postgres-XL','Postgres XL',#: Scalable Open Source PostgreSQL-based Database Cluster
    'RecDB',#: Open Source Recommendation Engine Built Entirely Inside PostgreSQL
    'Stado',#: open source MPP database system solely targeted at data warehousing and data mart applications
    'Yahoo Everest','Everest',#: multi-peta-byte database / MPP derived by PostgreSQL
'Memcached fork','Memcached evolution',#
    'Box Tron','Tron',#: proxy to memcached servers
    'Facebook McDipper','McDipper',#: key/value cache for flash storage
    'Facebook Mcrouter','Mcrouter',#: a memcached protocol router for scaling memcached deployments
    'Facebook Memcached','Memcached',#: fork of Memcache
    'Twemproxy',#: A fast, light-weight proxy for memcached and redis
    'Twitter Fatcache','Fatcache',#: key/value cache for flash storage
    'Twitter Twemcache','Twemcache',#: fork of Memcache
'Embedded Database',#
    'Actian PSQL','PSQL',#: ACID-compliant DBMS developed by Pervasive Software, optimized for embedding in applications
    'BerkeleyDB',#: a software library that provides a high-performance embedded database for key/value data
    'eXtreme DB',#: in-memory database combines exceptional performance, reliability and developer efficiency in a proven real-time embedded database engine
    'FairCom c-treeACE','c treeACE',#: a cross-platform database engine
    'Google Firebase','Firebase',#: a powerful API to store and sync data in realtime
    'HamsterDB',#: transactional key-value database
    'HanoiDB',#: Erlang LSM BTree Storage
    'LevelDB',#: a fast key-value storage library written at Google that provides an ordered mapping from string keys to string values
    'LMDB',#: ultra-fast, ultra-compact key-value embedded data store developed by Symas
    'RocksDB',#: embeddable persistent key-value store for fast storage based on LevelDB
    'TokioCabinet',#: a library of routines for managing a database
    'UnQLite',#: a in-process software library which implements a self-contained, serverless, zero-configuration, transactional NoSQL database engine
'Business Intelligence','BI',#
    'ActivePivot',#: Java In-Memory OLAP cube stored in columns, with clearly decoupled pre/post processing
    'Adatao',#: business intelligence and data science platform
    'Amazon QuickSight','QuickSight',#: Business Intelligence for Big Data
    'Apama analytics',#: platform for streaming analytics and intelligent automated action
    'Atigeo xPatterns','xPatterns',#: data analytics platform
    'BIME Analytics',#: business intelligence platform in the cloud
    'Chartio',#: lean business intelligence platform to visualize and explore your data
    'Datapine',#: self-service business intelligence tool in the cloud
    'Jaspersoft',#: powerful business intelligence suite
    'Jedox Palo','Palo',#: customisable Business Intelligence platform
    'Lavastorm Analytics',#: used for audit analytics, revenue assurance, fraud management, and customer experience management
    'LinkedIn GoSpeed','GoSpeed',#: provides RUM data processing, visualization, monitoring, and analyses data daily, hourly, or on a near real-time basis
    'Map-D','Map D',#: GPU in-memory database, big data analysis and visualization platform
    'Microsoft',#: business intelligence software and platform
    'Microstrategy',#: software platforms for business intelligence, mobile intelligence, and network applications
    'Pentaho',#: business intelligence platform
    'Qlik',#: business intelligence and analytics platform
    'SpagoBI',#: open source business intelligence platform
    'Spotfire',#: business intelligence platform
    'Stratio Explorer',#: an Interactive Web interpreter to Apache Crossdata, Stratio Ingestion, Stratio Decision,Markdown, Apache Spark, Apache Spark-SQL and command Shell
    'Tableau',#: business intelligence platform
    'Teradata Aster','Aster',#: Big Data Analytics
    'Tessera',#: Environment for Deep Analysis of Large Complex Data
    'Zeppelin',#: open source data analysis environment on top of Hadoop.
    'Zoomdata',#: Big Data Analytics
'Data Analysis','анализ данные',#
    'Apache Zeppelin','Zeppelin',#: a web-based notebook that enables interactive data analytics
    'Datameer',#: data analytics application for Hadoop combines self-service data integration, analytics and visualization
    'Ibis',#: Python big data analysis framework for high performance at Hadoop-scale, with first-class integration with Impala
    'LinkedIn Pinot','Pinot',#: a distributed system that supports columnar indexes with the ability to add new types of indexes
    'Microsoft Cortana Analytics','Cortana Analytics',#: a fully managed big data and advanced analytics suite that enables you to transform your data into intelligent action.
    'Myria',#: scalable Analytics-as-a-Service platform based on relational algebra
    'Periscope',#: plugs directly into your databases and lets you run, save, and share analyses over billions of data rows in seconds
    'Pinalytics',#: Pinterestâs data analytics engine
    'Shiny',#: web application framework for R
    'Stratio Sparkta','Sparkta',#: real time monitoring
    'Tamr',#: standalone tool to catalog all of your enterprise metadata
    'Zaloni Bedrock','Bedrock',#: fully integrated Hadoop data management platform
    'Zaloni Mica','Mica',#: self-service data discovery, curation, and governance
    'Zillabyte',#: an API for distributed data computation. Scale with your data.
'Data Warehouse','DWH'#
    'Google Mesa','Mesa',#: highly scalable analytic data warehousing system
    'IBM BigInsights','BigInsights',#: data processing, warehousing and analytics
    'IBM dashDB','dashDB',#: Data Warehousing and Analysis Needs, all in the Cloud
    'Microsoft Azure SQL Data Warehouse',#: businesses access to an elastic petabyte-scale, data warehouse-as-a-service offering that can scale according to their needs
    'Microsoft Cosmos','Cosmos',#: Microsoft’s internal BigData analysis platform
'Data Visualization','визуализация данные',#
    'Arbor',#: graph visualization library using web workers and jQuery
    'C3',#: D3-based reusable chart library
    'CartoDB',#: open-source or freemium hosting for geospatial databases with powerful front-end editing capabilities and a robust API
    'Chart.js',#: open source HTML5 Charts visualizations
    'Chartist.js',#: another open source HTML5 Charts visualization
    'Crossfilter',#: avaScript library for exploring large multivariate datasets in the browser. Works well with dc.js and d3.js
    'Cubism',#: JavaScript library for time series visualization
    'Cytoscape',#: JavaScript library for visualizing complex networks
    'D3',#: javaScript library for manipulating documents
    'DC.js',#: Dimensional charting built to work natively with crossfilter rendered using d3.js. Excellent for connecting charts/additional metadata to hover events in D3
    'Envisionjs',#: dynamic HTML5 visualization
    'FnordMetric ChartSQL','ChartSQL',#: allows you to write SQL queries that return charts instead of tables. The charts are rendered as SVG vector graphics.
    'Freeboard',#: open source real-time dashboard builder for IOT and other web mashups
    'Gephi',#: An award-winning open-source platform for visualizing and manipulating large graphs and network connections
    'Google Charts',#: simple charting API
    'Grafana',#: open source, feature rich metrics dashboard and graph editor for Graphite, InfluxDB & OpenTSDB
    'Graphistry',#: running on GPUs and turns static designs into interactive tools using client/cloud GPU infrastructure and GPU-accelerated languages like Superconductor
    'Graphite',#: scalable Realtime Graphing
    'Highcharts',#: simple and flexible charting API
    'IPython',#: provides a rich architecture for interactive computing
    'Keylines',#: toolkit for visualizing the networks in your data
    'Kibana',#: visualize logs and time-stamped data
    'Matplotlib',#: plotting with Python
    'Microsoft SandDance','SandDance',#: visually explore data sets to find stories and extract insights
    'NVD3',#: chart components for d3.js
    'Peity',#: Progressive SVG bar, line and pie charts
    'Plot.ly','Plotly',#: Easy-to-use web service that allows for rapid creation of complex charts, from heatmaps to histograms. Upload data to create and style charts with Plotly’s online spreadsheet. Fork others’ plots.
    'Recline',#: simple but powerful library for building data applications in pure Javascript and HTML
    'Redash',#: open-source platform to query and visualize data
    'Sigma.js',#: JavaScript library dedicated to graph drawing
    'Square Cubism.js',#: aÊD3Êplugin for visualizing time series. Use Cubism to construct better realtime dashboards, pulling data fromÊGraphite,ÊCubeÊand other sources
    'Stratio Viewer',#: dashboarding tool
    'Vega',#: a visualization grammar
'Internet of Things','интернет вещь',#
    '2lemetry',#: Platform for Internet of things
    'Evrything',#: Making products smart
    'ThingWorx',#: Rapid development and connection of intelligent systems
]


# In[4]:


programming_languages = [
    'Ansible',
    'AutoHotkey',
    'AutoIt',
    'C',
    'C/C++', 'C++', 'C#',
    'CMake',
    'Clojure',
    'ColdFusion',
    'Lisp',
    'Coronavirus',
    'Crystal',
    'D',
    'Delphi',
    'Elixir',
    'Elm',
    'Erlang',
    'F#',
    'Fortran',
    'Go',
    'Groovy',
    'Haskell',
    'Idris',
    'Java',
    'JavaScript',
    'Julia',
    'Kotlin',
    'Lua',
    'MongoDB',
    'MySQL',
    '.NET','NET',
    'Nim',
    'OCaml',
    'Perl',
    'PHP',
    'Postgres',
    'Python',
    'R',
    'Ruby',
    'Rust',
    'SAS',
    'Scala',
    'Shell',
    'Swift',
    'TypeScript',
    'v',
]


# In[5]:


# https://github.com/amusi/awesome-object-detection
object_detection = [
'R-CNN','R CNN',
'Fast R-CNN', 'Fast R CNN',
'Faster R-CNN','Faster R CNN',
'Mask R-CNN','Mask R CNN',
'Light-Head R-CNN','Light Head R CNN',
'Cascade R-CNN','Cascade R CNN',
'SPP-Net','SPP Net',
'YOLO',
'YOLOv2',
'YOLOv3',
'YOLT',
'SSD',
'DSSD',
'FSSD',
'ESSD',
'MDSSD',
'Pelee',
'Fire SSD',
'R-FCN','R FCN',
'FPN',
'DSOD',
'RetinaNet',
'MegDet',
'RefineNet',
'DetNet',
'SSOD',
'CornerNet',
'M2Det',
'3D Object Detection',
'ZSD（Zero-Shot Object Detection',
'OSD（One-Shot object Detection',
'Weakly Supervised Object Detection',
]


# In[8]:


# https://github.com/academic/awesome-datascience
data_science = [
'data science',
    'Supervised Learning', 'обучение учитель',
    'Regression',
    'Linear Regression',
    'Ordinary  Least Squares', 'Least Squares',
    'Logistic Regression',
    'Stepwise Regression',
    'Multivariate Adaptive Regression Splines',
    'Locally Estimated Scatterplot Smoothing',
    'Classification', 'классификация',
    'k-nearest neighbor', 'knn',
    'Support Vector Machines', 'svm', 'SVC',
    'Decision Trees', 'Decision Tree',
    'ID3 algorithm','ID3',
    'C4.5 algorithm','C4.5',
    'Ensemble Learning',
    'Boosting',
    'Bagging',
    'Random Forest',
    'AdaBoost',
    'Unsupervised Learning','обучение без учитель',
    'Clustering','кластеризация',
    'Hierchical clustering',
    'k means',
    'Fuzzy clustering',
    'Mixture model',
    'Neural Networks','нейросеть',
    'Self organizing map',
    'Adaptive resonance theory',
    'Semi Supervised Learning',
    'Reinforcement Learning','обучение подкрепление',
    'Q Learning',
    'SARSA (State-Action-Reward-State-Action) algorithm','SARSA',
    'Temporal difference learning',
    'Data Mining Algorithm-',
    'C4.5',
    'k-Means',
    'SVM',
    'Apriori',
    'EM',
    'PageRank',
    'AdaBoost',
    'kNN',
    'Naive Bayes',
    'CART',
'Machine Learning',
    'scikit-learn','scikit learn',
    'scikit-multilearn','scikit multilearn',
    'sklearn-expertsys','sklearn expertsys',
    'scikit-feature','scikit feature',
    'scikit-rebate','scikit rebate',
    'seqlearn',
    'sklearn-bayes','sklearn bayes',
    'sklearn-crfsuite','sklearn crfsuite',
    'sklearn-deap','sklearn deap',
    'sigopt_sklearn',
    'sklearn-evaluation','sklearn evaluation',
    'scikit-image','scikit image',
    'scikit-opt','scikit opt',
    'scikit-posthocs','scikit posthocs',
    'pystruct',
    'Shogun',
    'xLearn',
    'cuML',
    'causalml',
    'mlpack',
    'MLxtend',
    'modAL',
    'Sparkit-learn','Sparkit learn',
    'hyperlearn',
    'dlib',
    'RuleFit',
    'pyGAM',
'Deep Learning',
'pytorch',
    'PyTorch',
    'torchvision',
    'torchtext',
    'torchaudio',
    'ignite',
    'PyTorchNet',
    'PyToune',
    'skorch',
    'PyVarInf',
    'pytorch_geometric',
    'GPyTorch',
    'pyro',
    'Catalyst',
'TensorFlow',
    'TensorLayer',
    'TFLearn',
    'Sonnet',
    'tensorpack',
    'TRFL',
    'Polyaxon',
    'NeuPy',
    'tfdeploy',
    'tensorflow-upstream','tensorflow upstream',
    'TensorFlow Fold',
    'tensorlm',
    'TensorLight',
    'Mesh TensorFlow',
    'Ludwig',
    'TF-Agents','TF Agents',
    'TensorForce',
'Keras',
    'keras-contrib','keras contrib',
    'Hyperas',
    'Elephas',
    'Hera',
    'Spektral',
    'qkeras',
    'keras-rl','keras rl',
    'Talos',
'Visualization Tool',
    'addepar',
    'amcharts',
    'anychart',
    'bokeh',
    'slemma',
    'cartodb',
    'Cube',
    'd3plus',
    'Data-Driven Documents(D3js)','D3js',
    'datahero',
    'dygraphs',
    'ECharts',
    'exhibit',
    'gephi',
    'ggplot2',
    'Glue',
    'Google Chart Gallery','Google Chart',
    'highcarts',
    'import.io',
    'jqplot',
    'Matplotlib',
    'nvd3',
    'Opendata-tools','Opendata tool'
    'Openrefine',
    'plot.ly','plotly'
    'raw',
    'rcharts',
    'Seaborn',
    'techanjs',
    'Timeline',
    'variancecharts',
    'vida',
    'Wrangler',
    'r2d3',
    'NetworkX',
    'Redash',
    'C3',
    'TensorWatch',
]


# In[9]:


# https://github.com/ChristosChristofidis/awesome-deep-learning
deep_learning = [
'Framework',
    'Caffe',
    'Torch7',
    'Theano',
    'cuda-convnet',
    'convetjs',
    'Ccv',
    'NuPIC',
    'DeepLearning4J',
    'Brain',
    'DeepLearnToolbox',
    'Deepnet',
    'Deeppy',
    'JavaNN',
    'hebel',
    'Mocha.jl',
    'OpenDL',
    'cuDNN',
    'MGL',#
    'Knet.jl',#
    'Nvidia DIGITS',# - a web app based on Caffe
    'Neon',#- Python based Deep Learning Framework
    'Keras',# - Theano based Deep Learning Library
    'Chainer',# - A flexible framework of neural networks for deep learning
    'RNNLM Toolkit','RNNLM',
    'RNNLIB',# - A recurrent neural network library
    'char-rnn','char rnn'
    'MatConvNet',#: CNNs for MATLAB
    'Minerva',# - a fast and flexible tool for deep learning on multi-GPU
    'Brainstorm',# - Fast, flexible and fun neural networks.
    'Tensorflow',# - Open source software library for numerical computation using data flow graphs
    'DMTK',# - Microsoft Distributed Machine Learning Tookit
    'Scikit Flow',# - Simplified interface for TensorFlow (mimicking Scikit Learn)
    'MXnet',# - Lightweight, Portable, Flexible Distributed/Mobile Deep Learning framework
    'Veles',# - Samsung Distributed machine learning platform
    'Marvin',# - A Minimalist GPU-only N-Dimensional ConvNets Framework
    'Apache SINGA','SINGA',# - A General Distributed Deep Learning Platform
    'DSSTNE',# - Amazon's library for building Deep Learning models
    'SyntaxNet',# - Google's syntactic parser - A TensorFlow dependency library
    'mlpack',# - A scalable Machine Learning library
    'Torchnet',# - Torch based Deep Learning Library
    'Paddle',# - PArallel Distributed Deep LEarning by Baidu
    'NeuPy',# - Theano based Python library for ANN and Deep Learning
    'Lasagne',# - a lightweight library to build and train neural networks in Theano
    'nolearn',# - wrappers and abstractions around existing neural network libraries, most notably Lasagne
    'Sonnet',# - a library for constructing neural networks by Google's DeepMind
    'PyTorch',# - Tensors and Dynamic neural networks in Python with strong GPU acceleration
    'CNTK',# - Microsoft Cognitive Toolkit
    'Serpent.AI',# - Game agent framework: Use any video game as a deep learning sandbox
    'Caffe2',# - A New Lightweight, Modular, and Scalable Deep Learning Framework
    'deeplearn.js',# - Hardware-accelerated deep learning and linear algebra (NumPy) library for the web
    'TVM',# - End to End Deep Learning Compiler Stack for CPUs, GPUs and specialized accelerators
    'Coach',# - Reinforcement Learning Coach by Intel® AI Lab
    'albumentations',# - A fast and framework agnostic image augmentation library
    'Neuraxle',# - A general-purpose ML pipelining framework
    'Catalyst',#: High-level utils for PyTorch DL & RL research. It was developed with a focus on reproducibility, fast experimentation and code/ideas reusing
    'garage',# - A toolkit for reproducible reinforcement learning research
    'Detecto',# - Train and run object detection models with 5-10 lines of code
    'Karate Club',# - An unsupervised machine learning library for graph structured data
    'Synapses',# - A lightweight library for neural networks that runs anywhere
    'TensorForce',# - A TensorFlow library for applied reinforcement learning
    'Hopsworks',# - A Feature Store for ML and Data-Intensive AI
    'Feast',# - A Feature Store for ML for GCP by Gojek/Google
    'PyTorch Geometric Temporal',# - Representation learning on dynamic graphs
    'lightly',# - A computer vision framework for self-supervised learning
    'Trax',# — Deep Learning with Clear Code and Speed
    'Flax',# - a neural network ecosystem for JAX that is designed for flexibility
    'QuickVision',#
'Tools',#
    'Netron',# - Visualizer for deep learning and machine learning models
    'Jupyter Notebook','Jupyter',# - Web-based notebook environment for interactive computing
    'TensorBoard',# - TensorFlow's Visualization Toolkit
    'Visual Studio Tools for AI - Develop',# debug and deploy deep learning and AI solutions
    'TensorWatch',# - Debugging and visualization for deep learning
    'ML Workspace',# - All-in-one web-based IDE for machine learning and data science.
    'dowel',# - A little logger for machine learning research. Log any object to the console, CSVs, TensorBoard, text log files, and more with just one call to logger.log()
    'Neptune',# - Lightweight tool for experiment tracking and results visualization.
    'CatalyzeX',# - Browser extension (Chrome and Firefox) that automatically finds and links to code implementations for ML papers anywhere online: Google, Twitter, Arxiv, Scholar, etc.
    'Determined',# - Deep learning training platform with integrated support for distributed training, hyperparameter tuning, smart GPU scheduling, experiment tracking, and a model registry.
    'DAGsHub',# - Community platform for Open Source ML – Manage experiments, data & models and create collaborative ML projects easily.
]


# In[8]:


# http://bigdata.andreamostosi.name/


# In[10]:


# https://github.com/josephmisiti/awesome-machine-learning#frameworks-and-libraries


# In[ ]:




