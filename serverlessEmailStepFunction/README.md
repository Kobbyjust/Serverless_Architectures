# Serverless Email Architecture
This projects is a simple serverless architecture

It contains:
    S3 Bucket for static hosting
    API fronted lambda for processing
    A simple step function with a lambda that triggers Amazon SES
    Amazon SES to send email notification to users

## Steps
    SES Configuration
    1. Verify SES APPLICATION SENDING EMAIL ADDRESS by creating a new Identity
    2. Verify SES APPLICATION CUSTOMER EMAIL ADDRESS by creating a new Identity

    CREATING LAMBDA FUNCTIONS
    1. First upload the LambdaRole.yml in the cloudformation console to create the roles required by the lambda functions
    2. Create and Configure the email_reminder_lambda function - using the code in the email_reminder.py
    3. Create and Configure the api_lambda function - using the code in the api_lambda.py

    CREATE STEP FUNCTION STATE MACHINE
    1. First upload the StateMachineRole.yml in the Role folder in the cloudformation console to create the roles required by the State Machine
    2. Create a new state machice - Select Write your workflow in code 
    3. Copy and paste the stepfunction_ASL.json
    4. Change and use all the appriopriate parameters

    CREATE API
    1. Create a new API in the API Gateway console
    2. Create Resource - Enable API Gateway CORS
    3. Create a POST method with lambda integration. Ensure you have "Use Lambda Proxy integration" and "Use Default Timeout" box IS ticked.
    4. Deploy API
    At the top of the screen will be an Invoke URL

    HOSTING FRONTEND APPLICATION
    1. Create S3 bucket
    2. UNTICK Block all public access
    3. Click the Permissions tab.
       Scroll down and in the Bucket Policy area, click Edit
    4. Copy and Paste the code in the policy_public_bucket.json
    5. Download the serverless_folder
    6. Edit the serverless.js in the serverless_frontend folder with the invoke url.
    it should look something like this "https://somethingsomething.execute-api.us-east-1.amazonaws.com/prod/[api_resoure_name]"
    7. Upload to all four objects into the s3 bucket
    8. Visit the s3 bucket url generated for the static web hosting to test your application

### Note
Certain resources from this project were obtain from https://github.com/acantril/learn-cantrill-io-labs/blob/master/aws-serverless-pet-cuddle-o-tron/0

For absolute begins kindly visit the site for a deeper understanding of this architecture
