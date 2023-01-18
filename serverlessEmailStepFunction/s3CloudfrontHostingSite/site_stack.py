from aws_cdk import CfnOutput, Stack
from s3CloudfrontHostingSite.frontend import StaticSitePublicS3


class StaticSiteStack(Stack):
    def __init__(self, scope, construct_id, props, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        site = StaticSitePublicS3(
                self,
                f"{props['namespace']}-construct",

                origin_referer_header_parameter_name=props[
                    "origin_custom_header_parameter_name"
                ],
               
            )

        # Add stack outputs
        CfnOutput(
            self,
            "SiteBucketName",
            value=site.bucket.bucket_name,
        )


#