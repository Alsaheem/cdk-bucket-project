from aws_cdk import (
    Stack,
    CfnOutput,
    aws_s3 as _s3,
    aws_iam as _iam
)
from constructs import Construct


class AwsS3CreateStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        group = _iam.Group(self, "cdk-group", group_name="cdk-group")

        # The code that defines your stack goes here
        bucket = _s3.Bucket(self, "my-cdk-bucket",
                            bucket_name="vector-cdk-test-bucket",
                            versioned=False,
                            encryption=_s3.BucketEncryption.S3_MANAGED,
                            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL,
                            )

        _s3.Bucket(self, "my-cdk-bucket2",
                   bucket_name="vector-cdk-test-bucket-2",
                   versioned=False,
                   encryption=_s3.BucketEncryption.S3_MANAGED,
                   block_public_access=_s3.BlockPublicAccess.BLOCK_ALL,
                   )

        CfnOutput(self, "bucket_name_output", value=bucket.bucket_name)
        CfnOutput(self, "cdk_group_name_output", value=group.group_name,
                  description="cdk-group name description", export_name="cdk-group")
