import requests
def dl():
        dl_url = "http://api.xiequ.cn/VAD/GetIp.aspx?act=getturn51&uid=94212&vkey=58FC7BD5FB1EBED2F07615D3C8F74D51&num=1&time=6&plat=1&re=0&type=7&so=1&group=51&ow=1&spl=1&addr=&db=1"
        while True:
            response = requests.get(dl_url)
            if response.status_code == 200:
                proxy_str = response.text.strip()
                ip, port = proxy_str.split(":")
                proxy = {"https": f"http://{ip}:{port}"}
                try:
                    test_response = requests.get(
                        "http://www.baidu.com", proxies=proxy
                    )
                    if test_response.status_code == 200:
                        print(proxy)
                        return proxy
                except Exception as e:
                    print(f"代理IP {proxy} 无效: {e}")
            else:
                print("获取代理IP失败，重试中...")

dl()