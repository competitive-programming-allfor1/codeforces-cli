
from codeforces_publicAPI_provider import user_info
import json

def user_exists(user: str) -> bool :
	http_response_body = user_info(user)
	print(http_response_body)
	if http_response_body == "":
		return False
	return True

