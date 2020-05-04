from time import time, sleep
from typing import Callable

from selenium.common.exceptions import TimeoutException


def wait_until(valid: Callable[[], bool], timeout: int = 15, timeout_message: str = None):
    """
    Wait until validation function pass
    :param valid: function to be used for validation. It should return True if validation passed, or False otherwise
    :param timeout: optional maximum time for validation to pass
    :param timeout_message: optional message to be thrown within TimeoutException
    :raises TimeoutException: validation block doesn't pass until timeout
    """
    end_time = time() + timeout
    while time() < end_time:
        if not valid():
            sleep(1)
        else:
            return
    if timeout_message is None:
        timeout_message = '{} is False after {} seconds"'.format(valid.__name__, timeout)
    raise TimeoutException(timeout_message)
