import boto3


class AWSIdentityCollector:
    """Collects identity information from AWS STS"""

    def __init__(self):
        self.sts_client = boto3.client("sts")

    def get_identity(self):
        """Return the current AWS caller identity."""

        response = self.sts_client.get_caller_identity()
        return response
