from urllib.request import Request, urlopen
import urllib

def user_info(user: str):
    url = 'https://codeforces.com/api/user.info?handles={}'.format(user)
    print("url is : ")
    print(url)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Content-Type':'application/json'})
    try :
        response = urlopen(req)
        return response.read().decode("utf-8")
    except urllib.error.HTTPError as p:
        return ""
