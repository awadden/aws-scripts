import boto3
import json

# Define widgets, with a text widget first stating that this DashBoard is being maintained automatically.
# This widget is a basic EC2 CPU Utilization widget with default values for x, y, etc....
# This is where want to customize your widgets to what you desire, but you will need to edit the function that creates the widgets below
widStart = """{"widgets":[{"type":"text","properties":{"markdown":"This Dashboard is generated automatically so don't mess with it.  Please!!"}},"""
widEC2 = """{"type":"metric","properties":{"metrics":[["AWS/EC2","CPUUtilization","InstanceId",""]],"region":"ca-central-1"}}"""
widFinish = "]}"


cwclient = boto3.client('cloudwatch')
client = boto3.client('autoscaling')


def lambda_handler(event, context):
    asgName1 = event['detail']['AutoScalingGroupName']
    asgName = ''.join(asgName1)
    asresult = client.describe_auto_scaling_groups(AutoScalingGroupNames=[asgName])
    instcount = str(asresult['AutoScalingGroups']).count('InstanceId')

# Count number of spaces needed to insert the instance id's into to JSON file, and declare a string var
# to to store the new EC2 widget portion in the JSON file
    x = widEC2.find("InstanceId")
    instwid =("")

# Create the EC2 widget(s) portion for the new JSON file
    i=0
    for i in range(instcount):
        instwid = (instwid+widEC2[:x+13]+asresult['AutoScalingGroups'][0]['Instances'][i]['InstanceId']+widEC2[x+13:])
        i += 1
# add comma if multiple Widgets
        if i < instcount:
            instwid = (instwid+',')

# Define the dashboard name, and concatinate the JSON file portions
    dbname = ('DB-'+asresult['AutoScalingGroups'][0]['AutoScalingGroupName'])
    dbbody = (widStart+instwid+widFinish)

# Create the new DashBoard
    result = cwclient.put_dashboard(DashboardName=dbname, DashboardBody=dbbody)
