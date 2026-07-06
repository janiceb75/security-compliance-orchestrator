from collectors.aws_iam_collector import AWSIAMCollector
from pprint import pprint

collector = AWSIAMCollector()

iam_users = collector.list_users()


pprint(iam_users)
