"""
Implement a request parser prototype. Given an array of strings,
valid_auth_tokens, representing the valid auth tokens, and a 2D array
of strings, requests, representing the request types and URLs, for
each request, return the request status ("VALID", or "INVALID"). If
VALID, include a comma-separated string of parameters
"""

def get_responses(valid_auth_tokens, requests):
    pass


print(get_responses(["ah37j2ha483u", "safh34ywb0p5", "ba34wyi8t902"], [
    ["GET", "https://example.com/?token=347sd6yk8iu2&name=alex"],
    ["GET", "https://example.com/?token=safh34ywb0p5&name=alex"],
    ["POST", "https://example.com/?token=safh34ywb0p52&name=alex"],
    ["POST", "https://example.com/?token=safh34ywb0p52&csrf=ak2sh32dy&name=alex"],
]))
