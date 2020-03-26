from typing import List
from bs4 import BeautifulSoup
from helpers import user_exists
from helpers import user_submission_ids

Submmission_link_vector = List[str]

def get_submimssion_links(username: str, count: int) -> Submmission_link_vector:
	if not user_exists(username):
		return []

	raise NotImplementedError


print(user_submission_ids("WeHaveInt",3))
