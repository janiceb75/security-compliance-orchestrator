import boto3


class AWSIAMCollector:
    """Collects IAM information from AWS."""

    def __init__(self):
        self.iam_client = boto3.client("iam")

    def list_users(self):
        """Return IAM users from AWS."""
        response = self.iam_client.list_users()
        normalized_users = []
        for user in response["Users"]:

            normalized_user = {
                "username": user["UserName"],
                "arn": user["Arn"],
                "created": user["CreateDate"],
                "password_last_used": user.get("PasswordLastUsed"),
            }

            normalized_users.append(normalized_user)

        return normalized_users
