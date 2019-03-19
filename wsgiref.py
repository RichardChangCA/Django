from wsgiref.simple_server import make_server
import time
def yimi(url):
    with open("yimi.html", "r", encoding = 'utf-8') as f:
        s = f.read()
        now = str(time.time())
        s = s.replace("@@xx@@", now)
    return bytes(s, encoding = 'utf-8')  # 只能发送字节

def xiaohei(url):
    ret = 'hello {}'.format(url)
    return bytes(ret, encoding = 'utf-8')


list1 = [("/yimi/", yimi), ("/xiaohei/", xiaohei)]

def run_server(environ, start_response):
    start_response('200 OK',[('Content-Type', 'text/html;charset=utf-8'),]) # 设置HTTP相应的状态码和头信息
    url = environ['PATH_INFO'] # 取到用户输入的url
    func = None
    for i in list1:
        if i[0] == url:
            func = i[1]
            break
    if func:
        response = func(url)
    else:
        response = b'404 not found!'
    return [response,]

if __name__ =='__main__':
    httpd = make_server('127.0.0.1', 8090, run_server)
    print("我在8090端口等你哦")
    httpd.serve_forever()