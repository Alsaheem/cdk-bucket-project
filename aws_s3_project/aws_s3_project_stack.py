from aws_cdk import (
    Stack,
    CfnOutput,
    aws_s3 as _s3,
)
from constructs import Construct


class AwsS3CreateStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        bucket = _s3.Bucket(self, "my-cdk-bucket",
                            bucket_name="vector-cdk-test-bucket",
                            versioned=True,
                            encryption=_s3.BucketEncryption.KMS_MANAGED)

        CfnOutput(self, "bucket_name", value=bucket.bucket_name)
