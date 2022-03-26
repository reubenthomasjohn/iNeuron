# Assignment No.3

### Q1: Explain the Snowball concept.
Snowball is a part of the AWS Snow Family. It is an edge computing, data migration and storage device. It is usually in the size of a briefcase. Most commonly, it is used as a data migration device, when data from an on-premise service needs to be moved over to AWS. It generally comes in two types, a storage optimized version and a compute optimized version. Snowball Edge Storage Optimized devices provide both block storage and Amazon S3-compatible object storage, and 40 vCPUs. They are well suited for local storage and large scale-data transfer. Snowball Edge Compute Optimized devices provide 52 vCPUs, block and object storage, and an optional GPU for use cases like advanced machine learning. Snowball also supports specific EC2 instance types and lambda functions, so development and testing can be done in the cloud, and can then be deploying in remote locations to collect, pre-process and send the data over to AWS. 

### Q2: Make a distinction between NAT Gateways and NAT Instances.
Amazon recommends that users use NAT gateways since they provide better availability and bandwidth, and require less effort to administer. 

Nat Gateways:
1)	Highly available. NAT gateways in each Availability Zone are implemented with redundancy. Create a NAT gateway in each Availability Zone to ensure zone-independent architecture.

2)	They can Scale up to 45 Gbps.

3)	Managed by AWS. You do not need to perform any maintenance.

4)	Software is optimized for handling NAT traffic.

NAT Instances:
1)	Use a script to manage failover between instances.

2)	Depends on the bandwidth of the instance type.

3)	Managed by the user, for example, by installing software updates or operating system patches on the instance.

4)	A generic AMI that's configured to perform NAT.

### Q3: Describe the essential components of Amazon Web Services (AWS).
The two most essential components of AWS is the global network infrastructure and EC2. The AWS Global Infrastructure is globally distributed hardware and data-centers that are physically networked together to act as one large resource for the end customer. EC2 is AWS compute offering that forms the backbone for most of AWS service offerings. 

### Q4: When should you utilize a spin-up server? Use examples to demonstrate your point.
An EC2 instance can be used when one wants complete control over the host operating system, guest operating system and the hypervisor configuration. When the elastic nature of the service is required, that is when it is required to instantly scale to meet spikes in traffic or demand. When computing requirements unexpectedly change (up or down), Amazon EC2 can instantly respond, meaning that developers have the ability to control how many resources are in use at any given point in time. Let us consider that we have a database where a number of vehicles are constantly uploading data to it. In such cases, it is useful to use a spin up server to run the database, since AWS can provision new servers if traffic increases. 

### Q5: Explain the concept of outlier car scaling.
Auto scaling automatically monitors applications, and automatically adjusts capacity to achieve steady and predictable performance. This is does, ensuring the lowest possible cost. It is easy to setup, using AWS Auto scaling, even for applications that use multiple instances, across multiple services. The Auto scaling service has a clean user interface, that allows one to build scaling plans for EC2 insances, DynamoDB tables, Aurora etc. The server also allows to dynamically scale EC2 instances, and thus, the applications always have the right resources at the right time. It is common to combine auto scaling groups with elastic load balancers for optimal performance. 
