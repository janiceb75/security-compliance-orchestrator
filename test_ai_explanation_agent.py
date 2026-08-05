from ai_explanation_agent import AIExplanationAgent

finding = {
    "resource": "janicelb75-bucket1",
    "check": "Versioning",
    "finding": "Versioning is  Enabled",
    "severity": "Informational",
}

agent = AIExplanationAgent()

response = agent.explain_finding(finding)

print(response)