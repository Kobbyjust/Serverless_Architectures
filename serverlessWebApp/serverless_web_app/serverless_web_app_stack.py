from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_amplify as amplify,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_dynamodb,
    aws_codebuild as codebuild,
    aws_iam as iam,
    aws_sns_subscriptions as subs,
)


class ServerlessWebAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        amplify_app = amplify.CfnApp(self, "MyApp",
            name="ServerlessWebStack",
            
        )

        #Creating the compute Lambda function
        compute_lambda = _lambda.Function(self,'computeLambda',
            handler='lambda_handler.lambda_handler',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('serverless_web_app/app_lambda/'),
        )

        #Create an API GW Rest API
        base_api = apigw.RestApi(self, 'serverlessWebAPI',
        rest_api_name='serverlessWebAPI',
        )

        #Create a resource named "myserverless" on the base API
        api_resource = base_api.root.add_resource(
            'serverlessWeb',
            default_cors_preflight_options=apigw.CorsOptions(
                allow_methods=apigw.Cors.ALL_METHODS,
                allow_origins=apigw.Cors.ALL_ORIGINS,
                allow_headers=apigw.Cors.DEFAULT_HEADERS
                )       
        )

        #Create a Method Response Object: https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_apigateway/MethodResponse.html
        method_response = apigw.MethodResponse(
            status_code="200",
            response_parameters={
                    'method.response.header.Access-Control-Allow-Origin': True
                })

        #Add the API GW Integration to the "example" API GW Resource
        api_resource.add_method(
            "POST",
            apigw.LambdaIntegration(compute_lambda,
            #proxy=False,
            ),
            method_responses=[method_response],
        )

        # create dynamo table
        ServerlessWebAppDB = aws_dynamodb.Table(
            self, "ServerlessWebAppDB",
            partition_key=aws_dynamodb.Attribute(
                name="ID",
                type=aws_dynamodb.AttributeType.STRING
            )
        )

        compute_lambda.add_environment("TABLE_NAME", ServerlessWebAppDB.table_name)

        # grant permission to lambda to write to demo table
        #ServerlessWebAppDB.grant_write_data(compute_lambda)
        ServerlessWebAppDB.grant_full_access(compute_lambda)


        

        