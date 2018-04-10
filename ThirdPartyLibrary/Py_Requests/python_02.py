# encoding=utf-8
# 快速上手
import requests

# 更加复杂的POST请求
paypoad = {'key1':'value1','key2':'value2'}
r = requests.post('http://httpbin.org/post',data=paypoad)
print(r.text)
# 还可以为 data 参数传入一个元组列表
# 在表单中多个元素使用同一 key 的时候，这种方式尤其有效
paypoad = (('key1','value1'),('key1','value2'))
r = requests.post('http://httpbin.org/post',data=paypoad)
print(r.text)

import json
url = 'https://api.github.com/some/endpoint'
payload = {'some':'data'}
r = requests.post(url,data=json.dumps(payload))
print(r.text)
r = requests.post(url,json=payload)
print(r.text)

# POST一个多部分编码(Multipart-Encoded)的文件
# Requests 使得上传多部分编码文件变得很简单：
url = 'http://httpbin.org/post'
files = {'file':open('report.txt','rb')}
r = requests.post(url,files=files)
print(r.text)
# 你可以显式地设置文件名，文件类型和请求头：
files = {'file':('report.txt',open('report.txt','rb'),'application/vnd.ms-excek',{'Expires':'0'})}
r = requests.post(url,files=files)
print(r.text)
# 如果你想，你也可以发送作为文件来接收的字符串：
files = {'file':('report.txt','some,data,to,send\nanother,row,to,send\n')}
r = requests.post(url,files=files)
print(r.text)

# 响应状态码
r = requests.get('http://httpbin.org/get')
print(r.status_code)
# 状态码查询对象
print(r.status_code == requests.codes.ok)

r_bad = requests.get('http://httpbin.org/status/504')
print(r_bad.status_code)
# print(r_bad.raise_for_status())
print(r.raise_for_status())

# 响应头
print(r.headers)
print(r.headers['Content-Type'])
print(r.headers['CONTENT-TYPE'])

# Cookie
# 快速访问cookie
url = 'http://example.com/some/cookie/setting/url'
# r = requests.get(url)
# print(r.cookies['example_cookie_name'])
# 发送你的cookies到服务器
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url,cookies=cookies)
print(r.text)

# 重定向与请求历史
r = requests.get('http://github.com')
print(r.url)
print(r.status_code)
print(r.history)
# 通过 allow_redirects 参数禁用重定向处理
r = requests.get('http://github.com',allow_redirects=False)
print(r.status_code)
print(r.history)

# 超时
r = requests.get('http://github.com',timeout = 0.001)

