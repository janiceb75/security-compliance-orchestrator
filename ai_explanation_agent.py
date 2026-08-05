from openai import OpenAI


class AIExplanationAgent:
    def __init__(self):
        self.client = OpenAI()

    def explain_finding(self, finding):
        response = self.client.responses.create(
        model="gpt-5",
        input=f"""
    You are a senior cloud security engineer that is a NIST 800-53 expert.

    Use only the information in the finding.
    User clear professional language.
    List the NIST 800-53 control(s) that it partially or fully relates to.
    Assume the resource is AWS S3.
    Do not mention other cloud providers.
    Keep the response under 200 words.
    Return only:
    - Why it matters
    - Risk
    - Recommended remediation
    - Provide a NIST flavor implementation statement if the control is met

    Finding:
    {finding}
    """,
            )

        return response.output_text