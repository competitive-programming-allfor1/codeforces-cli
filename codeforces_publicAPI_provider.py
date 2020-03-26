from urllib.request import Request, urlopen
import urllib

def user_info(user: str):
    url = 'https://codeforces.com/api/user.info?handles={}'.format(user)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Content-Type':'application/json'})
    try :
        response = urlopen(req)
        return response.read().decode("utf-8")
    except urllib.error.HTTPError as p:
        return ""

def user_status(user: str, count: -1):
    url = "#"
    if count == -1:
        url = 'https://codeforces.com/api/user.status?handle={}&from=1'.format(user)
    else:
        url = 'https://codeforces.com/api/user.status?handle={}&from=1&count={}'.format(user, count)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Content-Type':'application/json'})
    try :
        response = urlopen(req)
        return response.read().decode("utf-8")
    except urllib.error.HTTPError as p:
        return ""