import time


def get_random_email() -> str:
    return f"test.{time.time():.0f}@example.com"
