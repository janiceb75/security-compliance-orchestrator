class S3AuditAgent:
    def __init__(self):
        pass

    def evaluate_buckets(self, normalized_data):
        bucket_findings = []
        for bucket in normalized_data:
            if bucket["algorithm"]:
                encryption_status = "Passed"
                finding = "Encryption is Enabled"
                severity = "Informational"

            else:
                encryption_status = "Failed"
                finding = "Encryption is not Enabled"
                severity = "High"
            encryption_assessment_result = {
                "resource": bucket["name"],
                "resource type": "S3 Bucket",
                "check": "Encryption",
                "finding": finding,
                "status": encryption_status,
                "severity": severity,
                "evidence": bucket["algorithm"],
            }
            if bucket["versioning"] == "NotConfigured":
                version_status = "Failed"
                finding = "Versioning is not Enabled"
                severity = "High"

            else:
                version_status = "Passed"
                finding = "Versioning is Enabled"
                severity = "Informational"

            versioning_assessment_result = {
                "resource": bucket["name"],
                "resource type": "S3 Bucket",
                "check": "Versioning",
                "finding": finding,
                "status": version_status,
                "severity": severity,
                "evidence": bucket["versioning"],
            }
            bucket_findings.append(encryption_assessment_result)
            bucket_findings.append(versioning_assessment_result)

        return bucket_findings
