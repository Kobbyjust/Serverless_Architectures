#!/usr/bin/env python3

import aws_cdk as cdk



#from s3CloudfrontHostingSite.site_stack import StaticSiteStack
from s3CloudfrontHostingSite.frontend import StaticSitePublicS3
from applicationlayer.api_lambda.api_lambda_stack import ApiLambdaStack

app = cdk.App()

# props = {
#     "namespace": app.node.try_get_context("namespace"),
#     "domain_name": app.node.try_get_context("domain_name"),
#     "sub_domain_name": app.node.try_get_context("sub_domain_name"),
#     "domain_certificate_arn": app.node.try_get_context(
#         "domain_certificate_arn"
#     ),
#     "enable_s3_website_endpoint": app.node.try_get_context(
#         "enable_s3_website_endpoint"
#     ),
#     "origin_custom_header_parameter_name": app.node.try_get_context(
#         "origin_custom_header_parameter_name"
#     ),
#     "hosted_zone_id": app.node.try_get_context("hosted_zone_id"),
#     "hosted_zone_name": app.node.try_get_context("hosted_zone_name"),
# }

# StaticSite = StaticSiteStack(
#     scope=app,
#     construct_id=f"{props['namespace']}-stack",
#     props=props,
#     description="Static Site using S3 and CloudFront",
# )
StaticSitePublicS3(app, "Myfrontend")

ApiLambdaStack(app, "ApiLambdaStack")

app.synth()
