import os


def env(key: str) -> str:
    """
    read values from environment variables, if they are not present then raise
    exceptions
    """
    value = os.environ.get(key)
    if not value:
        raise Exception(f"environment variable '{key}' not found")

    return value.strip()
