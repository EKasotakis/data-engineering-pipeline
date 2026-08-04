import time
from functools import wraps


def retry(max_attempts=3, delay=2):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(1, max_attempts + 1):
                try:
                    return function(*args, **kwargs)

                except Exception as error:
                    last_exception = error

                    print(
                        f"Attempt {attempt}/{max_attempts} failed: {error}"
                    )

                    if attempt < max_attempts:
                        time.sleep(delay)

            raise last_exception

        return wrapper

    return decorator