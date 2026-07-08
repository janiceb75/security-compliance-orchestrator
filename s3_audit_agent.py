class S3AuditAgent:
    def __init__(self):
        pass

    def evaluate_buckets(self, normalized_data):
        bucket_findings = []
        for bucket in normalized_data:
            if bucket["algorithm"]:
                encryption_status = "Passed"
            else:
                encryption_status = "Failed"
            if bucket["versioning"] == "NotConfigured":
                version_status = "Failed"
            else:
                version_status = "Passed"

            bucket_results = {
                "name": bucket["name"],
                "encryption status": encryption_status,
                "version status": version_status,
            }
            bucket_findings.append(bucket_results)

        return bucket_findings
