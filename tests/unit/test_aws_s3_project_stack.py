import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_s3_project.aws_s3_project_stack import AwsS3ProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_s3_project/aws_s3_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsS3ProjectStack(app, "aws-s3-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
