import requests, re
from urllib.parse import unquote, quote
from retry import retry


class APPLE:

    def __init__(self, **kwargs) -> None:
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.year = kwargs.get("year_item")
        self.monthOfYear = kwargs.get("monthOfYear_item")
        self.dayOfMonth = kwargs.get("dayOfMonth_item")
        self.question_one = kwargs.get("Question_one")
        self.answer_one = kwargs.get("Answer_one")
        self.question_two = kwargs.get("Question_two")
        self.answer_two = kwargs.get("Answer_two")
        self.question_three = kwargs.get("Question_three")
        self.answer_three = kwargs.get("Answer_three")
        self.pass_2 = ""

        # self.DL = {
        #     "http": "http://usera1:pwdword2@tunnel1.docip.net:18199",
        #     "https": "http://usera1:pwdword2@tunnel1.docip.net:18199",
        # }
        self.time = (20, 20)

    @retry(tries=20)
    def Get_sstt(self):
        headers = {
            "Host": "iforgot.apple.com",
            "Connection": "keep-alive",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://idmsa.apple.com.cn/",
            # "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            # "Cookie": "idclient=web; dslang=CN-ZH; site=CHN; ifssp=8F6D6A18FFA1A8AFF0ADB6956DB0E7474DAD3DBE0B9B52D7DEE473886AFA3295C1C6359E8C6370EABACF449D8ED6993B287621F6199695CA11613D923CB4EAF9F3514E0D4C1D3F12ABC1761B59A5836867B436AE0AA82721C95453EC30C465C1E35177645C16EF1C8B90C7B4B8BC2B8876C7A6D869F9F1F1; geo=CN"
        }
        response = requests.get(
            "https://iforgot.apple.com/password/verify/appleid", headers=headers
        )
        self.sstt = re.search(r'"sstt":"([^"]+)"', response.text).group(1)
        self.x_apple_i_web_token = response.cookies.get("X-Apple-I-Web-Token")
        self.ifssp = response.cookies.get("ifssp")
        return self

    @retry(tries=20)
    def get_verification_code(self):
        headers = {
            "Host": "iforgot.apple.com",
            "Connection": "keep-alive",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sstt": quote(self.sstt),
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9cedK9AqApNurJhBR.uMp4UdHz13Nl_jV2pNk0ug9WJ3uJsjMm_U_WU_v25BNlY5cklY5BqNAE.lTjV.9OX"}',
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua-platform": '"Windows"',
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://iforgot.apple.com/",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; geo=CN; X-Apple-I-Web-Token={self.x_apple_i_web_token}; ifssp={self.ifssp}",
        }
        params = {
            "captchaType": "IMAGE",
        }
        response = requests.get(
            "https://iforgot.apple.com/captcha", params=params, headers=headers
        )
        self.captcha = response.json()["payload"]["content"]
        self.x_apple_i_web_token_2 = response.cookies.get("X-Apple-I-Web-Token")
        self.Token = response.json()["token"]
        self.Id = response.json()["id"]
        return self

    @retry(tries=20)
    def Identification_codes(self):
        url = "http://110.41.40.215:8044/ocr"
        params = {"captcha": self.captcha}
        self.res = requests.get(url, params=params).text
        return self

    @retry(tries=20)
    def Submit_302_1(self):
        max_retries = 10  # 设置最大重试次数
        retries = 0  # 初始化重试计数器
        while retries < max_retries:
            try:
                cookies = {
                    "idclient": "web",
                    "dslang": "CN-ZH",
                    "site": "CHN",
                    "geo": "CN",
                    "ifssp": self.ifssp,
                    "X-Apple-I-Web-Token": self.x_apple_i_web_token_2,
                }
                headers = {
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json",
                    "Origin": "https://iforgot.apple.com",
                    "Pragma": "no-cache",
                    "Referer": "https://iforgot.apple.com/",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"Fla44j1e3NlY5BNlY5BSmHACVZXnNA9cedFWv9AqururJhBR.uMp4UdHz13NlejV2pNk0ug9WJ3uJsjMm_UWujme5BNlY5CGWY5BOgkLT0XxU..0ch"}',
                    "X-Requested-With": "XMLHttpRequest",
                    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sstt": quote(self.sstt),
                }
                json_data = {
                    "id": self.username,
                    "captcha": {
                        "id": self.Id,
                        "answer": self.res,
                        "token": self.Token,
                    },
                }
                response = requests.post(
                    "https://iforgot.apple.com/password/verify/appleid",
                    cookies=cookies,
                    headers=headers,
                    json=json_data,
                    allow_redirects=False,
                )
                self.sstt_2 = unquote(response.headers["Sstt"])
                self.x_apple_i_web_token_3 = response.cookies.get("X-Apple-I-Web-Token")
                return self
            except Exception:
                retries += 1
                if retries < max_retries:
                    self.get_verification_code()
                    self.Identification_codes()
                    print("Submit_302_1 failed.")
                else:
                    print("Max retries reached. Submit_302_1 failed.")

    @retry(tries=20)
    def Five(self):
        cookies = {
            "pltvcid": "undefined",
            "idclient": "web",
            "dslang": "CN-ZH",
            "site": "CHN",
            "geo": "CN",
            "pldfltcid": "9d562bc73d6f4a3e8623983cd00792dc047",
            "ifssp": self.ifssp,
            "X-Apple-I-Web-Token": self.x_apple_i_web_token_3,
        }

        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "DNT": "1",
            "Pragma": "no-cache",
            "Referer": "https://iforgot.apple.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"sda44j1e3NlY5BNlY5BSmHACVZXnNA9d8Hka9c3A6Lu_dYV6Hycfx9MsFY5CKw.Tf5.EKWJ9VbSIij__UWujyVNlY5BNp55BNlan0Os5Apw.8gh"}',
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sstt": quote(self.sstt),
        }

        params = {
            "sstt": self.sstt_2,
        }
        response = requests.get(
            "https://iforgot.apple.com/password/verify/phone",
            params=params,
            cookies=cookies,
            headers=headers,
        )
        self.x_apple_i_web_token_4 = response.cookies.get("X-Apple-I-Web-Token")
        self.sstt_3 = response.headers["sstt"]
        # print(response.text)
        return self

    @retry(tries=20)
    def Six(self):
        cookies = {
            "pltvcid": "undefined",
            "idclient": "web",
            "dslang": "CN-ZH",
            "site": "CHN",
            "geo": "CN",
            "pldfltcid": "9d562bc73d6f4a3e8623983cd00792dc047",
            "ifssp": self.ifssp,
            "X-Apple-I-Web-Token": self.x_apple_i_web_token_4,
        }

        headers = {
            "Accept": "text/html;format=fragmented",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "DNT": "1",
            "Pragma": "no-cache",
            "Referer": "https://iforgot.apple.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":".la44j1e3NlY5BNlY5BSmHACVZXnNA9d8Hx39Y5ururJhBR.uMp4UdHz13NlejV2pNk0ug9WJ3veSpwjKy_AxHWY5BNlYJNNlY5QB4bVNjMk.1LI"}',
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sstt": self.sstt_3,
        }

        response = requests.get(
            "https://iforgot.apple.com/password/verify/phone",
            cookies=cookies,
            headers=headers,
        )
        # print(response.text)
        self.x_apple_i_web_token_5 = response.cookies.get("X-Apple-I-Web-Token")
        self.sstt_2 = re.search(r'"sstt":"([^"]+)"', response.text).group(1)
        return self

    @retry(tries=20)
    def Seven(self):
        cookies = {
            "pltvcid": "undefined",
            "idclient": "web",
            "dslang": "CN-ZH",
            "site": "CHN",
            "geo": "CN",
            "pldfltcid": "9d562bc73d6f4a3e8623983cd00792dc047",
            "ifssp": self.ifssp,
            "X-Apple-I-Web-Token": self.x_apple_i_web_token_5,
        }

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "DNT": "1",
            "Origin": "https://iforgot.apple.com",
            "Pragma": "no-cache",
            "Referer": "https://iforgot.apple.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9d8HaH6gMhpjpidPNs0oje9zH_y37lYIU.6elV2pNK1c8rJvftTny6gzWv25BNlY5cklY5BqNAE.lTjV.7J8"}',
            "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "Sstt": quote(self.sstt_2),
        }

        response = requests.post(
            "https://iforgot.apple.com/password/verify/phone/unenrollment",
            cookies=cookies,
            headers=headers,
        )
        self.x_apple_i_web_token_6 = response.cookies.get("X-Apple-I-Web-Token")
        self.sstt_3 = response.headers["sstt"]
        self.location = response.headers["location"]
        # print(response.headers)
        return self

    @retry(tries=20)
    def Eight(self):
        cookies = {
            "pltvcid": "undefined",
            "idclient": "web",
            "dslang": "CN-ZH",
            "site": "CHN",
            "geo": "CN",
            "pldfltcid": "9d562bc73d6f4a3e8623983cd00792dc047",
            "ifssp": self.ifssp,
            "X-Apple-I-Web-Token": self.x_apple_i_web_token_6,
        }

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "DNT": "1",
            "Pragma": "no-cache",
            "Referer": "https://iforgot.apple.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9d8HaH6gMhpjpidPNs0oje9zH_y37lYIU.6elV2pNK1c8rJvftTny6gzWv25BNlY5cklY5BqNAE.lTjV.7J8"}',
            "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sstt": self.sstt_2,
        }

        response = requests.get(
            f"https://iforgot.apple.com{self.location}",
            cookies=cookies,
            headers=headers,
        )
        self.x_apple_i_web_token_7 = response.cookies.get("X-Apple-I-Web-Token")
        self.sstt_4 = response.headers["sstt"]
        return self

    @retry(tries=20)
    def Nine(self):
        cookies = {
            "pltvcid": "undefined",
            "pldfltcid": "9d562bc73d6f4a3e8623983cd00792dc047",
            "idclient": "web",
            "dslang": "CN-ZH",
            "site": "CHN",
            "ifssp": self.ifssp,
            "geo": "CN",
            "X-Apple-I-Web-Token": self.x_apple_i_web_token_7,
        }

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "DNT": "1",
            "Origin": "https://iforgot.apple.com",
            "Pragma": "no-cache",
            "Referer": "https://iforgot.apple.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"sda44j1e3NlY5BNlY5BSmHACVZXnNA9d8OFd_Kq9lpidPNs0oje9zH_y37lYIU.6elV2pNK1c8rJvhtHjyWyOFlY5BNleBBNlYCa1nkBMfs.20l"}',
            "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sstt": self.sstt_3,
        }

        json_data = {
            "monthOfYear": "05",
            "dayOfMonth": "25",
            "year": "1993",
        }

        response = requests.post(
            "https://iforgot.apple.com/unenrollment/verify/birthday",
            cookies=cookies,
            headers=headers,
            json=json_data,
            allow_redirects=False,
        )
        self.x_apple_i_web_token_8 = response.cookies.get("X-Apple-I-Web-Token")
        self.sstt_5 = response.headers["sstt"]
        self.location_2 = response.headers["location"]
        # print(response.headers)
        return self

    @retry(tries=20)  # 密保问题
    def Ten(self):
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "DNT": "1",
            "Origin": "https://iforgot.apple.com",
            "Pragma": "no-cache",
            "Referer": "https://iforgot.apple.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"sda44j1e3NlY5BNlY5BSmHACVZXnNA9d8OFd_Kq9lpidPNs0oje9zH_y37lYIU.6elV2pNK1c8rJvhtHjyWyOFlY5BNleBBNlYCa1nkBMfs.20l"}',
            "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "Sstt": self.sstt_5,
        }
        cookies = {
            "pltvcid": "undefined",
            "pldfltcid": "9d562bc73d6f4a3e8623983cd00792dc047",
            "idclient": "web",
            "dslang": "CN-ZH",
            "site": "CHN",
            "ifssp": self.ifssp,
            "geo": "CN",
            "X-Apple-I-Web-Token": self.x_apple_i_web_token_8,
        }
        url = f"https://iforgot.apple.com{self.location_2}"

        response = requests.get(url, headers=headers, cookies=cookies)
        self.x_apple_i_web_token_20 = response.cookies.get("X-Apple-I-Web-Token")
        self.sstt_20 = response.headers["sstt"]
        print(response.text)
        # print(response.headers)
        return self

    @retry(tries=20)
    def Eleven(self):
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "189",
            "Content-Type": "application/json",
            "Cookie": f"pltvcid=undefined; pldfltcid=9d562bc73d6f4a3e8623983cd00792dc047; idclient=web; dslang=CN-ZH; site=CHN; ifssp={self.ifssp}; geo=CN; X-Apple-I-Web-Token={self.x_apple_i_web_token_20}",
            "DNT": "1",
            "Host": "iforgot.apple.com",
            "Origin": "https://iforgot.apple.com",
            "Pragma": "no-cache",
            "Referer": "https://iforgot.apple.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9d8TmTrJkDlQxQeLaD.SAuXjodUW1BNork0ugN.xL4Fe1SpDvTJ2wrOy3klY5BNleBBNlYCa1nkBMfs.2fd"}',
            "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sstt": quote(self.sstt_20),
        }

        json_data = {
            "questions": [
                {
                    "answer": "gz1234",
                    "id": 136,
                    "number": 2,
                    "question": "你的理想工作是什么？",
                },
                {
                    "answer": "fm1234",
                    "id": 142,
                    "number": 3,
                    "question": "你的父母是在哪里认识的？",
                },
            ]
        }

        response = requests.post(
            "https://iforgot.apple.com/unenrollment/verify/questions",
            headers=headers,
            json=json_data,
            # allow_redirects=False,
        )
        print(response.headers)
        print(response.status_code)

    # @retry(tries=20)
    # def Twelve(self):
    #     cookies = {
    #         'pltvcid': 'undefined',
    #         'pldfltcid': '9d562bc73d6f4a3e8623983cd00792dc047',
    #         'idclient': 'web',
    #         'dslang': 'CN-ZH',
    #         'site': 'CHN',
    #         'geo': 'CN',
    #         'ifssp': self.ifssp,
    #         'X-Apple-I-Web-Token': self.x_apple_i_web_token_9,
    #     }

    #     headers = {
    #         'Accept': 'application/json, text/plain, */*',
    #         'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    #         'Cache-Control': 'no-cache',
    #         'Connection': 'keep-alive',
    #         'DNT': '1',
    #         'Pragma': 'no-cache',
    #         'Referer': 'https://iforgot.apple.com/',
    #         'Sec-Fetch-Dest': 'empty',
    #         'Sec-Fetch-Mode': 'cors',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    #         'X-Apple-I-FD-Client-Info': '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":".la44j1e3NlY5BNlY5BSmHACVZXnNA9d8Tg9OTrMcjpidPNs0oje9zH_y37lYKU.6elV2pNK1c8rJvhtJjmeUav25BNlY5cklY5BqNAE.lTjV.98I"}',
    #         'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    #         'sec-ch-ua-mobile': '?0',
    #         'sec-ch-ua-platform': '"Windows"',
    #         'sstt': self.sstt_6,
    #     }

    #     params = {
    #         'sstt': self.sstt_6,
    #     }

    #     response = requests.get('https://iforgot.apple.com/unenrollment', params=params, cookies=cookies, headers=headers)
    #     print(response.text)


if __name__ == "__main__":

    def start_process(
        username,
        password,
        year_item,
        monthOfYear_item,
        dayOfMonth_item,
        question_one,
        answer_one,
        question_two,
        answer_two,
        question_three,
        answer_three,
    ):
        apple = APPLE(
            username=username,
            password=password,
            year_item=year_item,
            monthOfYear_item=monthOfYear_item,
            dayOfMonth_item=dayOfMonth_item,
            Question_one=question_one,
            Answer_one=answer_one,
            Question_two=question_two,
            Answer_two=answer_two,
            Question_three=question_three,
            Answer_three=answer_three,
        )

        apple.Get_sstt()
        apple.get_verification_code()
        apple.Identification_codes()
        apple.Submit_302_1()
        apple.Five()
        apple.Six()
        apple.Seven()
        apple.Eight()
        apple.Nine()
        apple.Ten()
        apple.Eleven()
        # apple.Twelve()
        return apple

    # 使用示例
    result = start_process(
        username="antbpibailey@hotmail.com",
        password="Aa147369",
        year_item="1993",
        monthOfYear_item="05",
        dayOfMonth_item="25",
        question_one="你少年时代最好的朋友叫什么名字？",
        answer_one="py1234",
        question_two="你的理想工作是什么？",
        answer_two="gz1234",
        question_three="你的父母是在哪里认识的？",
        answer_three="fm1234",
    )
    print(result)
