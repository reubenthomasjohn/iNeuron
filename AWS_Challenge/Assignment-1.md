# Assignment No.1

## Q1: Describe how to link numerous sites to a VPC?
Firstly, the VPC needs to be expanded by adding four secondary IP address (IPv4) ranges. This is in addition to the default primary IP address. Next, EC2 instances need to be launched that will hold the infrastructure and code for the websites. The IP address for one instance at a time needs to be specified while launching the instance. In this way, different websites can be linked to the same VPC. As long as the VPC is appropriately sized to have an IPv4 address assigned to each instance, any number of EC2 instances hosting websites can be run within a VPC. 

## Q2: What is the difference between EBS and Instance Store, and how do you explain it?
EBS volumes are drives attached to a network. It is slower compared to instance stores, but the data is persistent. So even if the instance is rebooted, the data will remain. 

Instance stores are temporary storage for an instance. The storage is done on a disk that is physically attached to the host computer. 

EC2 instances can be launched using both these methods. Using instance stores, and EBS but EBS is the recommended method since they have persistent storage. 

## Q3: What are the different types of load balancers available in AWS?
There are four types of load balances available.
a.	Application load balancer
b.	Network load balancer
c.	Gateway load balancer
d.	Classic load balancer

## Q4: How does AWS IAM make a profit?
AWS IAM itself is free to use, but it makes it’s profit indirectly when other AWS services are purchased using IAM. EC2, EBS, S3 and RDS bring the most profit for AWS. AWS makes it hard for customers to move to other providers by emphasizing on higher level capabilities that it’s competitors. 

## Q5: Demonstrate the DynamoDB support mechanism.
DynamoDB is a serverless NOSQL database service. It is highly scalable, and offers a flexible model using autoscaling of throughput capacity.

DynamoDB supports GET/PUT operations using a user-defined primary key, and applications running on most operating systems (Linux, Windows, iOS, Android, Solaris, AIX and HP-UX) can use DynamoDB. 
