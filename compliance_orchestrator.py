from password_audit_agent import PasswordAuditAgent
from server_audit_agent import ServerAuditAgent


class ComplianceOrchestrator:
    def __init__(self):
        self.all_findings = []
        self.overall_summary = {}

    def run_audits(self, users, password_policy, servers, os_policy):
        print()
        password_agent = PasswordAuditAgent()
        pass_audit_results = password_agent.audit_passwords(users, password_policy)
        self.all_findings.extend(pass_audit_results)
        server_agent = ServerAuditAgent()
        server_audit_results = server_agent.audit_servers(servers, os_policy)
        self.all_findings.extend(server_audit_results)

        return self.all_findings

    def generate_summary(self):
        totals = len(self.all_findings)
        highs = 0
        criticals = 0
        mediums = 0
        for finding in self.all_findings:

            if finding["severity"] == "High":
                highs += 1
            if finding["severity"] == "Medium":
                mediums += 1
            if finding["severity"] == "Critical":
                criticals += 1

        self.overall_summary = {
            "Total Findings:": totals,
            "Critical Findings:": criticals,
            "High Findings:": highs,
            "Medium Findings:": mediums,
        }
        return self.overall_summary
