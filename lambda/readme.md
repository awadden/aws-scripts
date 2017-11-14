Lambda ASG CloudWatch Dashboards
This script will call the describe-ASG function for the ASG that triggered it,  perform a count of EC2 instances in the ASG, and deploy a custom dashboard with a Text widget saying it’s an auto generated dashboard, and an individual CPU Utilization Metric widget for each EC2 instance in the ASG. 

Getting Started
1. Create your autoscaling group
2. Create a plain lambda function, for python3, and add the lambda-asg-cwdb.py python3 code.  Don’t create a trigger yet.
	- you can also edit the strings at the top of the script to change the widget parameters if desired
3. Create a rule from within CloudWatch for the ASG service, every time an EC2 instance is deployed or terminated in that ASG, and set it to trigger the lambda function created in the previous step

Prerequisites
Auto scaling group
CloudWatch rule that triggers the lambda function

Installing
see Getting Started

Running the tests
Add or remove EC2 instances from your ASG

Built With
python

Contributing

Versioning

Authors
	•	Andy Wadden - Initial work 

License
This project is licensed under the MIT License - see the LICENSE.md file for details

Acknowledgments

