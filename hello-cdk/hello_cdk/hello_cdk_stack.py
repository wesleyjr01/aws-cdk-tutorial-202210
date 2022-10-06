import aws_cdk as cdk
from constructs import Construct
import aws_cdk.aws_s3 as s3


class HelloCdkStack(cdk.Stack):
    bucket_name = "my-first-bucket-test112"

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(
            self,
            id=self.bucket_name,
            bucket_name=self.bucket_name,
            versioned=True,
        )
