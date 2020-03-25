from urllib.request import Request, urlopen

def user_info(user: str):
	url = 'https://codeforces.com/api/user.info?handles={}'.format(user)
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	response =  urlopen(req)
	return response
