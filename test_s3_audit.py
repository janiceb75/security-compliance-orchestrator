from s3_audit_agent import S3AuditAgent
from collectors.aws_s3_collector import AWSS3Collector
from pprint import pprint

collector = AWSS3Collector()

normalized_buckets = collector.list_buckets()

agent = S3AuditAgent()
findings = agent.evaluate_buckets(normalized_buckets)

pprint(findings, sort_dicts=False)
