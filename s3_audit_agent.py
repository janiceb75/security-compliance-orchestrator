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
            if bucket["versioning"] == "Enabled":
                version_status = "Passed"
                finding = "Versioning is Enabled"
                severity = "Informational"

            else:
                version_status = "Failed"
                finding = "Versioning is not Enabled"
                severity = "High"

            versioning_assessment_result = {
                "resource": bucket["name"],
                "resource type": "S3 Bucket",
                "check": "Versioning",
                "finding": finding,
                "status": version_status,
                "severity": severity,
                "evidence": bucket["versioning"],
            }

            if bucket["public access settings"]["BlockPublicAcls"] == True:
                block_public_acl_status = "Passed"
                block_public_acl_finding = "Block Public ACL is Enabled"
                block_public_acl_severity ="Informational"
            else:
                block_public_acl_status = "Failed"
                block_public_acl_finding = "Block Public ACL is not Enabled"
                block_public_acl_severity ="High"
                
                
            if bucket["public access settings"]["IgnorePublicAcls"] == True:
                ignore_public_acl_status = "Passed"
                ignore_public_acl_finding = "Ignore Public ACL is Enabled"
                ignore_public_acl_severity ="Informational"
            else:
                ignore_public_acl_status = "Failed"
                ignore_public_acl_finding = "Ignore Public ACL is not Enabled"
                ignore_public_acl_severity ="High"
                            
                            
            if bucket["public access settings"]["BlockPublicPolicy"] == True:
                block_public_policy_status = "Passed"
                block_public_policy_finding = "Block Public Policy is Enabled"
                block_public_policy_severity ="Informational"
            else:
                block_public_policy_status = "Failed"
                block_public_policy_finding = "Block Public Policy is not Enabled"
                block_public_policy_severity ="High"
                                            
            if bucket["public access settings"]["RestrictPublicBuckets"] == True:
                restrict_public_buckets_status = "Passed"
                restrict_public_buckets_finding = "Restrict Public Buckets is Enabled"
                restrict_public_buckets_severity ="Informational"
            else:
                restrict_public_buckets_status = "Failed"
                restrict_public_buckets_finding = "Restrict Public Buckets is not Enabled"
                restrict_public_buckets_severity ="High"
        
            block_public_acl_settings_assessment_result = {
                "resource": bucket["name"],
                "resource type": "S3 Bucket",
                "check": "Block Public ACLs",
                "finding": block_public_acl_finding,
                "status": block_public_acl_status,
                "severity": block_public_acl_severity,
                "evidence": bucket["public access settings"]["BlockPublicAcls"],
            } 
                
                
            ignore_public_acl_settings_assessment_result = {
                "resource": bucket["name"],
                "resource type": "S3 Bucket",
                "check": "Ignore Public ACLs",
                "finding": ignore_public_acl_finding,
                "status": ignore_public_acl_status,
                "severity": ignore_public_acl_severity,
                "evidence": bucket["public access settings"]["IgnorePublicAcls"],
            } 
                            
                            
            block_public_policy_assessment_result = {
                "resource": bucket["name"],
                "resource type": "S3 Bucket",
                "check": "Block Public Policy",
                "finding": block_public_policy_finding,
                "status": block_public_policy_status,
                "severity": block_public_policy_severity,
                "evidence": bucket["public access settings"]["BlockPublicPolicy"],
            } 
                                            
                                            
            restrict_public_buckets_assessment_result = {
                "resource": bucket["name"],
                "resource type": "S3 Bucket",
                "check": "Restrict Public Buckets",
                "finding": restrict_public_buckets_finding,
                "status": restrict_public_buckets_status,
                "severity": restrict_public_buckets_severity,
                "evidence": bucket["public access settings"]["RestrictPublicBuckets"],
            } 
                                                              
                
                
                
                
            bucket_findings.append(encryption_assessment_result)
            bucket_findings.append(versioning_assessment_result)
            bucket_findings.append(block_public_acl_settings_assessment_result)
            bucket_findings.append(ignore_public_acl_settings_assessment_result)
            bucket_findings.append(block_public_policy_assessment_result)
            bucket_findings.append(restrict_public_buckets_assessment_result)
            

        return bucket_findings
