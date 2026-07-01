class ServerAuditAgent:
    def __init__(self):
        self.findings = []

    def audit_servers(self, servers, os_policy):
        for server in servers:
            if server["OS"] in os_policy:
                finding_dict = {
                    "resource": server["Hostname"],
                    "resource type": "Server",
                    "os": server["OS"],
                    "finding": "Unsupported operating system",
                    "severity": os_policy[server["OS"]]["severity"],
                }
                self.findings.append(finding_dict)

        return self.findings
