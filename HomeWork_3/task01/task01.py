from collections.abc import Callable


def cache(times: int) -> Callable:
    def decorator(func):

        results = {}
        results_count = {}

        def wrapper(*args, **kwargs):

            if (*args, *kwargs) in results:
                results_count[(*args, *kwargs)] -= 1
                result = results[(*args, *kwargs)]
                if results_count[(*args, *kwargs)] == 0:
                    del results[(*args, *kwargs)], results_count[(*args, *kwargs)]
                return result

            else:
                result = func(*args, **kwargs)
                results[(*args, *kwargs)] = result
                results_count[(*args, *kwargs)] = times
                return result

        return wrapper

    return decorator
