# Assignment No.3

### Q1: Explain the concept of auto-scaling.
Auto scaling is a cloud computing feature that allows for provisioning and launching additional instances to meet a growing demand in load, or increasing oncoming traffic. AWS offers this using their product called Auto Scaling Groups. AWS monitors applications and automatically adjusts capacity thus retaining a steady and predictable performance. 

### Q2: Explain Cloud Formation Solution.
Cloud formation is AWS’s Infrastructure as Code offering. It helps developers, businesses and enterprises create their required resources for any given application easily, and programmatically. Further in this manner, they are able to provision and manage them in an orderly fashion. 

### Q3: Mention and explain AWS services that are not specialized to a specific location.
Global services:
1.	IAM - AWS Identity and Access Management (IAM) let’s one create and manage AWS users and groups and use permissions in the form of policies to allow and deny their access to AWS resources.
2.	S3 - S3 is an abbreviation for Simple Storage Service. It allows a user to store data in the form of objects. It is scalable, has features for improving availability, and is very secure. All kinds of data from all kinds of sources such as data storage for data lakes, websites, IoT etc. can be stored using S3. Additionally, S3 can be optimised, organised, and access controlled using IAM. Data is stored in the form of objects, and different objects are put into what AWS calls S3 buckets.
3.	CloudFront – CloudFront is a content distribution network. You point your website to CloudFront so that it will route requests to nearest Edge Location cache
4.	Route53 – Route53 is a Domain Name service that AWS offers. 

### Q4: What's the difference between pausing and terminating an Amazon Elastic Compute Cloud instance?
In both cases, the EC2 instance that was provisioned will be taken away. The difference lies in what happens with the EBS volume snapshot. If the instance is terminated, by default the volume will be deleted. However, if it is paused, the attached bootable EBS volume will not be deleted. The data on the EBS volume will remain after stopping while all information on the local (ephemeral) hard drive will be lost as usual.

### Q5: Describe how to set up CloudWatch to recover an EC2 instance.
1.	Select the instance that needs to be configured and monitored to be recovered using the EC2 console.
2.	Choose actions, and choose monitor and troubleshoot. Then choose manage CloudWatch alarms.
3.	Create an alarm (IAM access to stop and start the particular instance needs to be given)
4.	Use SNS to create alarm notification
5.	Toggle alarm action, and choose recover
6.	For Group samples by and Type of data to sample, choose an appropriate statistic and metric for your use case.
7.	For Consecutive period and Period, specify the evaluation period for the alarm.
8.	Choose create
