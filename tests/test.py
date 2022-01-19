import requests

from src.requests_error_handling_package.requests_error_decorator import requests_error_handler


@requests_error_handler
def example():
    response = requests.get("http://google.com/doesntexist")
    response.raise_for_status()
    return response.status_code
