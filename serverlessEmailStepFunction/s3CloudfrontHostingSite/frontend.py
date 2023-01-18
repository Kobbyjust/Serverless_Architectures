"""
Two constructs to host static sites in aws using S3, cloudfront and Route53.

StaticSitePrivateS3 creates a private S3 bucket and uses S3 API endpoint as
an origin in cloudfront and Origin Access Identity (OAI) to access the s3 objects.

StaticSitePublicS3 creates a public S3 bucket with website enabled and
uses Origin Custom Header (referer) to limit the access of s3 objects to the
CloudFront only.
"""
from aws_cdk import (
    aws_s3 as s3,
    RemovalPolicy,
    Stack
)
from constructs import Construct

class StaticSitePublicS3(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        #
        self.bucket = s3.Bucket(
            self,
            "site_bucket",
            bucket_name="myfrontendbucket12345",
            website_index_document="index.html",
            website_error_document="404.html",
            public_read_access=True,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )
        #