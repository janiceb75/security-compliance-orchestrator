from compliance_orchestrator import ComplianceOrchestrator
from sample_data import users, password_policy, servers, os_policy

JanCompOrchestrator = ComplianceOrchestrator()


findings = JanCompOrchestrator.run_audits(users, password_policy, servers, os_policy)

for finding in findings:
    print(finding)

print()

print(JanCompOrchestrator.generate_summary())
