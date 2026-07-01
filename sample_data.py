"""
Original Python sample data.

This file has been retained for reference.
The application now loads data from sample_data.json.
"""

servers = [
    {"Hostname": "WEB01", "OS": "Windows Server 2019"},
    {"Hostname": "APP01", "OS": "Windows Server 2008"},
    {"Hostname": "LEGACY01", "OS": "Windows Server 2003"},
    {"Hostname": "DB01", "OS": "Ubuntu 22.04"},
]

os_policy = {
    "Windows Server 2003": {"status": "Unsupported", "severity": "Critical"},
    "Windows Server 2008": {"status": "Unsupported", "severity": "High"},
}

password_policy = {
    "max_password_age": 30,
    "mfa_required": True,
    "password_reuse_allowed": False,
}

users = [
    {
        "username": "jsmith",
        "password_age": 45,
        "mfa_enabled": True,
        "password_reused": False,
    },
    {
        "username": "agarcia",
        "password_age": 10,
        "mfa_enabled": False,
        "password_reused": False,
    },
    {
        "username": "mbrown",
        "password_age": 90,
        "mfa_enabled": False,
        "password_reused": True,
    },
    {
        "username": "kwilson",
        "password_age": 5,
        "mfa_enabled": True,
        "password_reused": False,
    },
]
