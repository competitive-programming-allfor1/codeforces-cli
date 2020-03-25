
from codeforces_publicAPI_provider import user_info
import json

def user_exists(user: str) -> bool :
	httpresponse = user_info(user)
	print(httpresponse.status)
	if httpresponse.status != 200:
		return False
	return True

