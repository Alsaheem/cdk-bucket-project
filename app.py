#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_s3_project.aws_s3_project_stack import AwsS3CreateStack


app = cdk.App()
AwsS3CreateStack(app, "my-aws-s3-stack")

app.synth()
