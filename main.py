import json

from compliance_orchestrator import ComplianceOrchestrator

json_file = open("sample_data.json")
data = json.load(json_file)

users = data["users"]
password_policy = data["password_policy"]
servers = data["servers"]
os_policy = data["os_policy"]

JanCompOrchestrator = ComplianceOrchestrator()


findings = JanCompOrchestrator.run_audits(users, password_policy, servers, os_policy)

for finding in findings:
    print(finding)

print()

print(JanCompOrchestrator.generate_summary())
