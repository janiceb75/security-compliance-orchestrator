import boto3
from pprint import pprint
from botocore.exceptions import ClientError


class AWSS3Collector:
    """Collects S3 Information from AWS"""

    def __init__(self):
        self.s3_client = boto3.client("s3")
        self.normalized_names = []
        # self.bucket_names = []

    def list_buckets(self):
        response = self.s3_client.list_buckets()
        for bucket in response["Buckets"]:
            name = bucket["Name"]
            date = bucket["CreationDate"].isoformat()
            encryption = self.s3_client.get_bucket_encryption(Bucket=name)
            normalized_name = {
                "name": name,
                "created": date,
                "encryption": encryption,
            }
            self.normalized_names.append(normalized_name)
            # self.bucket_names.append(bucket_name)
        # pprint(response)  # here to give me the full dict view
        return self.normalized_names


collector = AWSS3Collector()

pprint(collector.list_buckets(), sort_dicts=False)
