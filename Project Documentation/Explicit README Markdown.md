# Predictive Maintenance System with AWS and Machine Learning

## Project Overview

This project simulates sensor data for predictive maintenance and integrates with Amazon SageMaker and Amazon SNS to predict equipment faults and trigger alerts. Designed for industrial applications, this solution helps reduce downtime, optimize maintenance schedules, and prevent costly equipment failures. By leveraging AWS serverless technologies, it provides a scalable and cost-effective approach to predictive maintenance, particularly relevant to industries in South Africa such as mining, agriculture, and manufacturing.

---

## Key Features

- *Sensor Data Simulation*: Generates realistic sensor readings for temperature and vibration.
- *Machine Learning Integration*: Uses Amazon SageMaker to predict equipment faults.
- *Real-Time Alerts*: Sends notifications via Amazon SNS when faults are detected.
- *Serverless Architecture*: Built on AWS Lambda for automatic scaling and minimal operational overhead.

---

## Real-World Use Cases in South Africa

### 1. *Mining Industry*
   - Monitor heavy machinery (e.g., drills, conveyors) to detect anomalies in vibration or temperature, preventing unplanned downtime in high-stakes environments like the platinum or gold mines of Gauteng and Limpopo.

### 2. *Agricultural Sector*
   - Predict failures in irrigation systems or harvesting equipment, critical for farms in the Western Cape and Free State, where equipment reliability directly impacts crop yield.

### 3. *Manufacturing*
   - Ensure continuous operation of production lines in automotive factories (e.g., Nelson Mandela Bay's industrial zone) by identifying wear-and-tear in machinery.

### 4. *Energy Infrastructure*
   - Monitor wind turbines or solar inverters in renewable energy projects (e.g., Northern Cape solar farms) to maintain consistent energy output.

---

## Technical Overview

### Architecture Flow
1. *AWS Lambda* simulates sensor data (temperature and vibration).
2. *Amazon SageMaker* endpoint processes the data and returns a prediction (0 for OK, 10 for FAULT).
3. *Amazon SNS* sends an email/SMS alert if a fault is detected.

![Architecture Diagram]![alt text](<Industrial Maintenance flowchart.jpeg>) 

### Components
- *Sensor Simulation*  
  Generates random values within operational ranges:
  - Temperature: 20–30°C (typical for machinery).
  - Vibration: 0–10 units (higher values indicate instability).

- *Machine Learning Model*  
  A SageMaker endpoint hosts a pre-trained model to classify sensor data. Replace SAGEMAKER_ENDPOINT with your deployed endpoint.

- *Alerting System*  
  SNS notifications are sent to maintenance teams for immediate action.

---

## Configuration

### Prerequisites
1. *AWS Account*: With permissions for Lambda, SageMaker, and SNS.
2. *SageMaker Endpoint*: Deploy a trained model (e.g., Scikit-Learn or TensorFlow) and update SAGEMAKER_ENDPOINT.
3. *SNS Topic*: Create an SNS topic (email or SMS subscriptions) and update SNS_TOPIC_ARN.

### AWS Region
The default region is us-east-1. For South African deployments, use af-south-1 (Cape Town region) where applicable.

python
# Example: Initialize clients in af-south-1
sagemaker = boto3.client('sagemaker-runtime', region_name='af-south-1')
sns = boto3.client('sns', region_name='af-south-1')


---

## Deployment

### 1. Lambda Function Setup
- *Runtime*: Python 3.9+
- *Permissions*: Attach an IAM role with policies for sagemaker:InvokeEndpoint and sns:Publish.

### 2. Testing
- *Local Testing*: Use the AWS SAM CLI to simulate events.
- *Cloud Deployment*: Deploy via AWS Console, CLI, or infrastructure-as-code (IaC) tools like CloudFormation.

### 3. Monitoring
- Use Amazon CloudWatch to track Lambda invocations, SageMaker latency, and SNS delivery metrics.

---

## Error Handling
- *SageMaker Errors*: Retry failed inference requests.
- *SNS Failures*: Log delivery issues and implement dead-letter queues (DLQs) for retries.
- *Lambda Logs*: All errors are logged in CloudWatch for auditing.

---

## Skills Developed

### AWS Cloud Competencies
- *Serverless Computing*: Designed a scalable Lambda function with event-driven execution.
- *Machine Learning Operations (MLOps)*: Integrated SageMaker endpoints for real-time inference.
- *Event Messaging*: Configured SNS for cross-team alerting.
- *IAM Security*: Implemented least-privilege access for AWS services.

### Python Development
- *Boto3 Mastery*: Used AWS SDK for Python to interact with SageMaker and SNS.
- *Data Simulation*: Generated synthetic sensor data for testing.
- *Error Handling*: Implemented robust exception handling for production reliability.
- *JSON Processing*: Parsed and formatted data for API requests/responses.

---

## Future Enhancements
1. *IoT Integration*: Connect to real sensors via AWS IoT Core for live data ingestion.
2. *Advanced Analytics*: Use Amazon QuickSight for predictive maintenance dashboards.
3. *Multi-Sensor Support*: Add pressure, humidity, or RPM metrics for mining equipment.
4. *Regional Adaptations*: Optimize models for local environmental conditions (e.g., high temperatures in the Karoo).

---

## Dependencies
- [Boto3](https://github.com/boto/boto3) (AWS SDK for Python)
- Python 3.9+

---

## License
Apache 2.0 (See [LICENSE](LICENSE) for details).

---

By implementing this project, I gained hands-on experience in building end-to-end cloud solutions, from data simulation to actionable insights—a critical skillset for enabling Industry 4.0 innovations in South Africa and beyond.

---

### How AWS IoT Could Be Integrated (Future Expansion):

The current setup is a good starting point for development and testing. However, in a real-world industrial predictive maintenance scenario, you would likely want to integrate with AWS IoT. Here's how and why:

## Real Sensor Data:

Instead of simulation, you'd have real sensors (e.g., on machines in a factory) sending data.
These sensors would likely be connected to AWS IoT Core.
AWS IoT Core would act as a central hub for receiving and managing sensor data streams.
Data Routing and Transformation:

AWS IoT Core's rules engine could be used to:
Receive data from devices (via MQTT, HTTP, or other protocols).
Transform data (e.g., change formats, combine multiple data points).
Route data to other AWS services, such as:
Lambda: The data could be sent to a Lambda function (or the same one) for further processing.
Kinesis: For real-time data streaming to other analytics tools.
S3: For data storage and historical analysis.
Device Management:

AWS IoT Device Management can be used to manage the devices themselves (e.g., security updates, firmware updates).
Security

# AWS IoT is a great way to secure the exchange of data between your devices and the cloud.
In Summary:

The current code is a great starting point for a proof-of-concept or a controlled testing environment. It successfully demonstrates the core logic of simulating data, calling a SageMaker endpoint, and triggering SNS alerts.

