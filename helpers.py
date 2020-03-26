
from codeforces_publicAPI_provider import user_info
from codeforces_publicAPI_provider import user_status
import json
from glom import glom


def user_exists(user: str) -> bool :
	http_response_body = user_info(user)
	if http_response_body == "":
		return False
	return True

def user_submission_ids(user: str, count: int) -> [int]:
	if not user_exists(user):
		return ""
	result = []

	http_response_body = user_status(user,count)
	parsed_json_dict = json.loads(http_response_body)

	result_id_map = map(lambda submission_result : glom(submission_result,'id'), parsed_json_dict['result'])
	result = [result_id for result_id in list(result_id_map)]
	return result
