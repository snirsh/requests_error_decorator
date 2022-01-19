# requests_error_decorator
A simple decorator for python requests

## Example:
```python
import requests
from requests_error_handling_package.requests_error_decorators import requests_error_handler
from requests_error_handling_package.example import example

@requests_error_handler
def foo():
    """
    A function that shows a basic example.
    """
    resp = requests.get("https://google.com/foo")
    resp.raise_for_status() # THIS IS A MUST-DO STEP!
    return resp

example() # an example function that you can run yourself and see what the output looks like
```