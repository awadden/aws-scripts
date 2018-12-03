import boto3
import json
import os
import cfnresponse


def lambda_handler(event, context):
  client = boto3.client('ec2')
  responseData = {}
  responseValue = client.create_vpc_endpoint(
  VpcEndpointType = os.environ['endpointtype'],
  VpcId = os.environ['vpcid'],
  ServiceName = os.environ['servicename'],
  SubnetIds = [os.environ['subnet']],
  SecurityGroupIds = [os.environ['securitygroup']],
  PrivateDnsEnabled = True
 )
 responseData['Data'] = str(responseValue)
 cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, CustomResourcePhysicalID")
