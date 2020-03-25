from typing import List
from bs4 import BeautifulSoup
from helpers import user_exists

Submmission_link_vector = List[str]
Submmission_list_vector = List[str]

def get_submission_lists(username: str) -> Submmission_list_vector:
	if user_exists(username) == False:
		return []
	else:
		raise NotImplementedError
		

def get_submimssion_links(username: str) -> Submmission_link_vector:
	raise NotImplementedError
