from constructs import Construct
from aws_cdk import (
    aws_iam as iam,
    aws_apigateway as apigw,
    aws_lambda as _lambda,
    aws_dynamodb,
    aws_lambda_event_sources as lambda_event_source,
    Aws, Stack
) 

class ApiLambdaStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)


        #Creating Role for Lamda and APIGateway
        API_role = iam.Role(self, "APISurveyCollection",
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
            code=_lambda.Code.from_asset('applicationlayer/lambda'),
        )

        #Create an API GW Rest API
        base_api = apigw.RestApi(self, 'SurveyCollectAPI',
        rest_api_name='TestAPI',
        #proxy=True
        )

        base_api.root.add_method("ANY")

        #Create a resource named "myserverless" on the base API
        api_resource = base_api.root.add_resource('SurveyCollection')


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

        
        # create dynamo table
        surveyCollectiondb = aws_dynamodb.Table(
            self, "surveyCollectiondb",
            partition_key=aws_dynamodb.Attribute(
                name="id",
                type=aws_dynamodb.AttributeType.STRING
            )
        )

         
        processing_lambda.add_environment("TABLE_NAME", surveyCollectiondb.table_name)

        # grant permission to lambda to write to demo table
        surveyCollectiondb.grant_write_data(processing_lambda)
