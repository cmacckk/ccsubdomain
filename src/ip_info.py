from urllib import request as urllib_request
import json

def ip_data(ip):
    if ip is None:
        return
    API = "http://ip.taobao.com/service/getIpInfo.php?ip="
    url = API + ip
    headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': r'https://www.taobao.com',
    'Connection': 'keep-alive'
    }
    req = urllib_request.Request(url, headers=headers)
    page = urllib_request.urlopen(req)


    jsondata = json.load(page)

    if jsondata['code'] == 1:
        return
    else:
        return jsondata['city']