class PasswordAuditAgent:
    """Audits user accounts for password policy violations."""

    def __init__(self):
        self.findings = []
        self.high_findings = 0
        self.med_findings = 0
        self.summary_report = {}

    def audit_passwords(self, users, password_policy):
        """Evaluate users against the organization's password policy and generate security findings."""

        for user in users:

            if user["password_age"] > password_policy["max_password_age"]:
                self.findings.append(
                    {
                        "resource": user["username"],
                        "resource type": "User",
                        "finding": "Password expired",
                        "severity": "Medium",
                    }
                )
                self.med_findings += 1
            if user["mfa_enabled"] != password_policy["mfa_required"]:
                self.findings.append(
                    {
                        "resource": user["username"],
                        "resource type": "User",
                        "finding": "MFA not enabled",
                        "severity": "High",
                    }
                )
                self.high_findings += 1
            if user["password_reused"] != password_policy["password_reuse_allowed"]:
                self.findings.append(
                    {
                        "resource": user["username"],
                        "resource type": "User",
                        "finding": "Password Reused",
                        "severity": "High",
                    }
                )
                self.high_findings += 1
        self.summary_report = {
            "Total findings:": len(self.findings),
            "High Findings:": self.high_findings,
            "Medium Findings:": self.med_findings,
        }
        return self.findings
