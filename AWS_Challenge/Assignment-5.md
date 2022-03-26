# Assignment No.5

### Q1: Describe the Amazon C4 instance.
C4 is the latest generation of EC2 Compute optimized instances. C in C4 stands for compute-optimized. They are designed for compute-bound workloads such as MMO gaming, media processing, HPC applications etc. They are available in 5 sizes, offering up to 36 vCPUs. They use the Intel Xeon E5-2666 v3 (codename Haswell) processors that run at a base frequency of 2.9 GHz, and can deliver clock speeds as high as 3.5 GHz with Intel ® Turbo Boost. Each C4 instance type is EBS-optimized by default and at no additional cost. This feature provides 500 Mbps to 4,000 Mbps of dedicated throughput to EBS above and beyond the general-purpose network throughput provided to the instance. C4 instances also provide Enhanced Networking for higher packet per second (PPS) performance, lower network jitter, and lower network latencies.

### Q2: What is ElastiCache?
Elasticache is a serverless, in-memory caching service. Caching using Elasticache accelerates application and database performance. It can also be used as a primary data store for use cases that don’t require much durability like session stores, leaderboards etc. It is compatible with Redis as well. 

### Q3: Explain SimpleDB.
SimpleDB is a highly available NoSQL data store that removed much of the work of a database administration. Hence, the name. Additionally, with hardly any administrative burden, SimpleDB creates geographically distributed replicas of the data to enable high availability and durability. The cost one pays is simply for the resourced consumed in the storing of data and serving of retrieval requests. 

### Q4: Mention the benefits of WAF.
1.	Agile protection against web attacks
2.	Time saved with managed rules
3.	Improved web traffic visibility
4.	Easy deployment and maintenance
5.	Easily monitor, block or rate limit bots
6.	Security integrated during development of applications

### Q5: Explain Elastic Block is a store that sells elastic blocks.
Essentially, each block is a storage volume that is used in conjunction with EC2 instances. Elastic block store volumes behave like raw, unformatted block devices, and these can be mounted as devices onto EC2 instances. There are different volume types that can be purchased from the elastic block store, each having their own advantages and disadvantages. For example, there are gp3, gp3-iops, gp3-throughput, gp2, io2-storage, op2-iops etc. Hence, it is said that the elastic block store is a store that sells elastic blocks, where each block is a virtual storage volume to be mounted onto an EC2 instance. 
