from contextlib import contextmanager


class SuppressorClass:
    """
    Write a context manager, that suppresses passed exception.
    Do it both ways: as a class and as a generator.
    # >>> with suppressor(IndexError):
    # ...    [][2]
    """

    def __init__(self, suppressed_error):
        self.suppressed_error = suppressed_error

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == self.suppressed_error:
            return True
        return False


@contextmanager
def suppressor_function(suppressed_error):
    try:
        yield
    except suppressed_error:
        pass
    finally:
        pass
