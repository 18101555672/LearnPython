# encoding=utf-8
# 快速上手
# 发送请求
import requests
r_get = requests.get('https://api.github.com/events')
# r_post = requests.post('http://httpbin.org/post',data={'key':'value'})
# r_put = requests.put('http://httpbin.org/put',data={'key':'value'})
# r_delete = requests.delete('http://httpbin.org/delete')
# r_head = requests.head('http://httpbin.org/get')
# r_options = requests.options('http://httpbin.org/get')

# 传递URL参数
# params关键字参数
payload = {'key1':'value1','key2':'value2','key3':None}
r_params = requests.get('http://httpbin.org/get',params=payload)
print(r_params.url)
# 注意字典里值为 None 的键都不会被添加到 URL 的查询字符串里
# 还可以将一个列表作为值传入：
payload = {'key1':'value1','key2':'value2','key3':['value31','value32']}
r_params = requests.get('http://httpbin.org/get',params=payload)
print(r_params.url)

# 响应内容
print(r_get.text)
# 获取requests使用的编码类型
print(r_get.encoding)
# 更改编码类型
# r_get.encoding = '***'

# 二进制响应内容
print(r_get.content)

# JSON影响内容
print(r_get.json())
# 获取请求的状态码
print(r_get.status_code)
# 获取请求是否有报错
print(r_get.raise_for_status())

# 原始响应内容
r_raw = requests.get('https://api.github.com/events',stream=True)
print(r_raw.raw)
print(r_raw.raw.read(10))
# 将文本流保存到文件
# with open(filename,'wb') as f:
#     for chunk in r.iter_content(chunk_size):
#         f.write(chunk)
# 使用 Response.iter_content 将会处理大量你直接使用 Response.raw 不得不处理的。
# 当流下载时，上面是优先推荐的获取内容方式。
# Note that chunk_size can be freely adjusted to a number that may better fit your use cases.

# 定制请求头
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent':'my-app/0.0.1'}
r_headers = requests.get(url,headers=headers)
# 注意: 定制 header 的优先级低于某些特定的信息源，例如：
# 如果在 .netrc 中设置了用户认证信息，使用 headers= 设置的授权就不会生效。而如果设置了 auth= 参数，``.netrc`` 的设置就无效了。
# 如果被重定向到别的主机，授权 header 就会被删除。
# 代理授权 header 会被 URL 中提供的代理身份覆盖掉。
# 在我们能判断内容长度的情况下，header 的 Content-Length 会被改写。
# 更进一步讲，Requests 不会基于定制 header 的具体情况改变自己的行为。只不过在最后的请求中，所有的 header 信息都会被传递进去。
# 注意: 所有的 header 值必须是 string、bytestring 或者 unicode。尽管传递 unicode header 也是允许的，但不建议这样做。





