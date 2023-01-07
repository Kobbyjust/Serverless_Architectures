from constructs import Construct
from aws_cdk import (
    aws_iam as iam,
    aws_apigateway as apigw,
    aws_lambda as _lambda,
    aws_stepfunctions as _aws_stepfunctions,
    aws_stepfunctions_tasks as _aws_stepfunctions_tasks,
    aws_lambda_event_sources as lambda_event_source,
    aws_ses as ses,
    Aws,Duration , Stack
) 

class ApiLambdaStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #Creating SES Identities
        sender_email_identity = ses.CfnEmailIdentity(self, "MySenderEmailIdentity",
        email_identity="sagarinokoeaws1+main@gmail.com",)

        receiver_email_identity = ses.CfnEmailIdentity(self, "MyReceiverEmailIdentity",
        email_identity="sagarinokoeaws1+receiver@gmail.com",)


        #Creating Role for Lamda and APIGateway
        API_role = iam.Role(self, "APIEmailStepFunction",
        assumed_by=iam.ServicePrincipal("apigateway.amazonaws.com")

        )
        API_role.add_to_policy(iam.PolicyStatement(
        resources=["*"],
        actions=["lambda:InvokeFunction"]
        ))

        lambda_role = iam.Role(self, "MyTestLambda",
        assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        description="Lambda role for apigateway..."
        )

        lambda_role.add_to_policy(iam.PolicyStatement(
        resources=["*"],
        actions=["lambda:InvokeFunction"]
        ))

        
        #Creating the processing Lambda function
        processing_lambda = _lambda.Function(self,'ProcessingLambda',
            handler='lambda-handler.handler',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('applicationlayer/lambda/trigger'),
        )

        #Creating the processing Lambda function
        email_lambda = _lambda.Function(self,'EmailLambda',
            handler='lambda-handler.handler',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('applicationlayer/lambda/email'),
        )

        #Create an API GW Rest API
        base_api = apigw.RestApi(self, 'EmailStepFunctionAPI',
        rest_api_name='TestAPI',
        #proxy=True
        )

        base_api.root.add_method("ANY")

        #Create a resource named "myserverless" on the base API
        api_resource = base_api.root.add_resource('EmailStepFunction')


        #Create API Integration Response object: https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_apigateway/IntegrationResponse.html
        integration_response = apigw.IntegrationResponse(
            status_code="200",
            response_templates={"application/json": ""},

        )

        #Create a Method Response Object: https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_apigateway/MethodResponse.html
        method_response = apigw.MethodResponse(status_code="200")

        #Add the API GW Integration to the "example" API GW Resource
        api_resource.add_method(
            "POST",
            method_responses=[method_response]
        ) 

        # Step Function Definition
        wait_job = _aws_stepfunctions.Wait(
            self, "Wait 30 Seconds",
            time=_aws_stepfunctions.WaitTime.duration(
                Duration.seconds(30))
        )

        email_job = _aws_stepfunctions_tasks.LambdaInvoke(
            self, "Send Email",
            lambda_function=email_lambda
            #output_path="$.Payload"
        )

        #Create Chain
        definition = wait_job.next(email_job)\

         # Create state machine
        sm = _aws_stepfunctions.StateMachine(
            self, "StateMachine",
            definition=definition,
            timeout=Duration.minutes(5),
        )