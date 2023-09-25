"""
Implement a request parser prototype. Given an array of strings,
valid_auth_tokens, representing the valid auth tokens, and a 2D array
of strings, requests, representing the request types and URLs, for
each request, return the request status ("VALID", or "INVALID"). If
VALID, include a comma-separated string of parameters
"""

def get_responses(valid_auth_tokens, requests):
    # Write your code here
    # cast valid_auth_tokens list to set to improve look up time
    valid_tokens = set(valid_auth_tokens)
    # responses list
    responses = []
    # iterate through requests
    # unpack into req method and url
    for method, url in requests:
        # has_valid_token = False
        # has_valid_csrf = False if method == "POST" else True
        has_valid_token = False
        has_valid_csrf = False if method == "POST" else True

        # get req_param_string by splitting req_parameters on "?"
        req_param_str = url.split("?")
        # get req_param list by splitting req_param_string on "&"
        req_params = req_param_str[1].split("&")
        # response_str = ""
        response = ""
        # iterate through req_param list
        for param in req_params:
            # param_key_value = split param on "="
            key_val = param.split("=")
            # if param[0] == "token"
            if key_val[0] == "token":
                # check if string after "=" is in valid_auth_tokens
                # if True has_valid_token = True
                has_valid_token = key_val[1] in valid_tokens
            # if method == "POST" and param[0] == "csrf"
            elif method == "POST" and key_val[0] == "csrf":
                # check if string after "=" is in valid_auth_tokens
                # if True has_valid_csrf = True
                has_valid_csrf = is_valid_csrf(key_val[1])
            # else
            else:
                response = f"{response},{','.join(key_val)}"
                # join param_key_value on ","
                # concat to response_str
        # if has_valid_token and has_valid_csrf:
        if has_valid_token and has_valid_csrf:
            # responses_list.append(f"VALID,{response_str}")
            responses.append(f"VALID{response}")
        # else:
        else:
            # responses_list.append("INVALID")
            responses.append("INVALID")

    # return responses list
    return responses


def is_valid_csrf(token):
    if len(token) < 8 or not token.isalnum() or token.lower() != token:
        return False
    return True


print(get_responses(["ah37j2ha483u", "safh34ywb0p5", "ba34wyi8t902"], [
    ["GET", "https://example.com/?token=347sd6yk8iu2&name=alex"],
    ["GET", "https://example.com/?token=safh34ywb0p5&name=alex"],
    ["POST", "https://example.com/?token=safh34ywb0p52&name=alex"],
    ["POST", "https://example.com/?token=safh34ywb0p52&csrf=ak2sh32dy&name=alex"],
]))
