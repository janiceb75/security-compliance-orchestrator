import boto3
from pprint import pprint


class AWSS3Collector:
    """Collects S3 Information from AWS"""

    def __init__(self):
        self.s3_client = boto3.client("s3")
    def list_buckets(self):
        response = self.s3_client.list_buckets()
        normalized_buckets = []
        for bucket in response["Buckets"]:
            name = bucket["Name"]
            date = bucket["CreationDate"].isoformat()
            encryption = self.s3_client.get_bucket_encryption(Bucket=name)
            versioning = self.s3_client.get_bucket_versioning(Bucket=name)
            versioning_status = versioning.get("Status", "NotConfigured")
            encryption_algorithm = encryption["ServerSideEncryptionConfiguration"][
                "Rules"
            ][0]["ApplyServerSideEncryptionByDefault"]["SSEAlgorithm"]
            public_access_block = self.s3_client.get_public_access_block(Bucket=name)
            public_access_settings = public_access_block[
                "PublicAccessBlockConfiguration"
            ]
            # pprint(public_access_block)
            normalized_bucket = {
                "name": name,
                "created": date,
                "algorithm": encryption_algorithm,
                "versioning": versioning_status,
                "public access settings": public_access_settings,
            }
            normalized_buckets.append(normalized_bucket)
            # self.bucket_names.append(bucket_name)
        # pprint(response)  # here to give me the full dict view
        return normalized_buckets


collector = AWSS3Collector()
data = collector.list_buckets()

print()
print()
print("Following is the normalized bucket data")
print()
print()
pprint(data, sort_dicts=False)
