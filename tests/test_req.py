"""
test req
    pytest --base-url=https://httpbin.org
"""

def test_req_get(req):
    """
    test req
    """
    req("GET", '/get', headers={'x-test2': 'true'}, params={'key': 'value'})


def test_req_post(req):
    """
    test req
    """
    req("POST", '/post', headers={'x-test2': 'true'}, json={'key': 'value'})
