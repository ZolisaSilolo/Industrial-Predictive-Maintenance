import json
import boto3
import random

# Clients for SageMaker and SNS with region specification
sagemaker = boto3.client('sagemaker-runtime', region_name='us-east-1')
sns = boto3.client('sns', region_name='us-east-1')

#You must have an existing SageMaker endpoint and SNS topic to use this code. Hence the values are hardcoded with placeholders.
# This is very IMPORTANT if you want to run the project yourself: Replace these with your actual values!
SAGEMAKER_ENDPOINT = "your-sagemaker-endpoint"
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:123456789012:FaultAlertingtopic"  # Adjust region if needed and create a topic in your account

def lambda_handler(event, context):
    """
    Handles the Lambda function event.

    Simulates sensor data, invokes a SageMaker endpoint for prediction,
    and publishes an alert to SNS if a fault is detected.

    Args:
        event (dict): The event data passed to the Lambda function.
        context (object): The runtime information of the Lambda function.

    Returns:
        dict: A dictionary containing the status code and response body.
    """
    # Simulate sensor data (temperature and vibration)
    sensor_data = {
        "temperature": random.uniform(20, 30),
        "vibration": random.uniform(0, 10),
    }

    try:
        # Now this my dear friend is to:Invoke SageMaker endpoint for prediction
        response = sagemaker.invoke_endpoint(
            EndpointName=SAGEMAKER_ENDPOINT,
            Body=json.dumps(sensor_data),
            ContentType='application/json',
        )
        result = json.loads(response['Body'].read().decode("utf-8"))
        prediction = result.get('prediction')  # Expected: 0 (OK) or 10 (FAULT)
    except Exception as e:
        print(f"Error invoking SageMaker: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'SageMaker invocation failed'})
        }

    # Log the sensor data and prediction
    print(f"Sensor_Data: {sensor_data}")
    print(f"Prediction: {prediction}")

    # Keep in mind, you have to :Publish to SNS if a fault is detected
    if prediction == 10:
        message = f"Alert: fault detected with sensor data: {sensor_data}"
        try:
            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Message=message,
                Subject="Maintenance Alert"
            )
            print("SNS alert published")
        except Exception as e:
            print(f"Error publishing to SNS: {e}")
            return {
                'statusCode': 500,
                'body': json.dumps({'error': 'SNS publishing failed'})
            }
    else:
        print("No fault detected")

    return {
        'statusCode': 200,
        'body': json.dumps({
            'sensor_data': sensor_data,
            'prediction': prediction
        })
    }

# This is the end of the code.
# Now, you can test the Lambda function by invoking it with a test event. COnsidering you have the required resources.
# You can also deploy the Lambda function to your AWS account and configure it to run periodically using Amazon CloudWatch Events.
#Imagine such a small script can do so much. It can simulate sensor data, invoke a SageMaker endpoint for prediction, and publish an alert to SNS if a fault is detected.
#This is the power of AWS Lambda functions and the AWS SDK for Python (Boto3).
#You can use this as a template to build your own serverless applications that leverage AWS services to solve real-world problems.
#I hope you enjoyed this project and learned something new about serverless computing with AWS Lambda.
#Thank you for reading!