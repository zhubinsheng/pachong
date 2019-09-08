from urllib.request import quote, unquote
import random
import requests

# keyword = quote('java').strip()
# print(keyword, type(keyword))
# city = quote('郑州').strip()
# print(unquote(city))

refer_url = 'https://ssl.gongyi.qq.com/wxact/2019mainvenue/mainvenue.html?et=venue'
ajax_url = 'https://97bd8fc25c64468ebd3aaa48e5d696fe@report.url.cn/sentry/497'
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
]

data = {

}
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '46',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': refer_url,
    'User-Agent': user_agents[random.randrange(0, 3)],
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest',
}
resp = requests.post(ajax_url, data=data, headers=headers)

result = resp.json()
print(result)
# print(result)
# result 就是最终获得的json格式数据
item = result['content']['positionResult']['result'][0]
print(item)
# item就是单个招聘条目信息
print("程序结束")
