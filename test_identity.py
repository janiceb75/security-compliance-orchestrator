from collectors.aws_identity_collector import AWSIdentityCollector

collector = AWSIdentityCollector()

identity = collector.get_identity()


print(identity["Account"])
print(identity["Arn"])
