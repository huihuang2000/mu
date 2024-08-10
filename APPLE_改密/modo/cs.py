from email import header
from nturl2path import url2pathname
from uuid import RESERVED_FUTURE
from wsgiref import headers
import requests, re
from urllib.parse import unquote, quote
from retry import retry
from yarl import URL


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
        self.status = ""
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
            "sstt": self.sstt,
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
        if response.text == "{ }":
            self.status = "此号无密保"
        elif response.text != "{ }":
            self.x_apple_i_web_token_4 = response.cookies.get("X-Apple-I-Web-Token")
            self.sstt_3 = response.headers["Sstt"]
            return self

    @retry(tries=20)
    def Six(self):
        cookies = {
            "pltvcid": "undefined",
            "pldfltcid": "9d562bc73d6f4a3e8623983cd00792dc047",
            "idclient": "web",
            "dslang": "CN-ZH",
            "site": "CHN",
            "ifssp": self.ifssp,
            "geo": "CN",
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
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":".la44j1e3NlY5BNlY5BSmHACVZXnNA9d8TmTmOF5NurJhBR.uMp4UdHz13Nl_jV2pNk0ug9WJ3veSqwc6tifwoclY5BNleBBNlYCa1nkBMfs.C_z"}',
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
        self.x_apple_i_web_token_5 = response.cookies.get("X-Apple-I-Web-Token")
        self.sstt_4 = re.search(r'"sstt":"([^"]+)"', response.text).group(1)
        # print(response.headers)
        # print(response.text)
        return self

    @retry(tries=20)
    def Seven(self):
        cookies = {
            "pltvcid": "undefined",
            "pldfltcid": "9d562bc73d6f4a3e8623983cd00792dc047",
            "idclient": "web",
            "dslang": "CN-ZH",
            "site": "CHN",
            "ifssp": self.ifssp,
            "geo": "CN",
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
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9d8TmTliog8fxQeLaD.SAuXjodUW1BNork0ugN.xL4Fe1SpDvTJ2wrOyMgBNlY5BPY25BNnOVgw24uy.56Y"}',
            "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sstt": quote(self.sstt_4),
        }

        response = requests.post(
            "https://iforgot.apple.com/password/verify/phone/unenrollment",
            cookies=cookies,
            headers=headers,
            allow_redirects=False,
        )
        self.x_apple_i_web_token_6 = response.cookies.get("X-Apple-I-Web-Token")
        self.Location = response.headers["Location"]
        self.sstt_5 = response.headers["Sstt"]
        return self

    @retry(tries=20)
    def Eight(self):
        cookies = {
            "pltvcid": "undefined",
            "pldfltcid": "9d562bc73d6f4a3e8623983cd00792dc047",
            "idclient": "web",
            "dslang": "CN-ZH",
            "site": "CHN",
            "ifssp": self.ifssp,
            "geo": "CN",
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
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9d8TmTliog8fxQeLaD.SAuXjodUW1BNork0ugN.xL4Fe1SpDvTJ2wrOyMgBNlY5BPY25BNnOVgw24uy.56Y"}',
            "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sstt": quote(self.sstt_4),
        }
        response = requests.get(
            f"https://iforgot.apple.com{self.Location}",
            cookies=cookies,
            headers=headers,
        )
        self.x_apple_i_web_token_7 = response.cookies.get("X-Apple-I-Web-Token")
        self.sstt_6 = response.headers["Sstt"]
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
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9d8TmTk25WKUfSHolk2dUJKy_Aw7GY5ay.EKY.6eke4FIidrQmVUavEp55BNlY5CGWY5BOgkLT0XxU..42Z"}',
            "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sstt": self.sstt_6,
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
        self.Location_2 = response.headers["Location"]
        self.sstt_7 = response.headers["Sstt"]
        return self

    @retry(tries=20)
    def Ten(self):
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

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            # 'Cookie': 'pltvcid=undefined; pldfltcid=9d562bc73d6f4a3e8623983cd00792dc047; idclient=web; dslang=CN-ZH; site=CHN; ifssp=A769EB512342739EBF9CDEE4E63BEE61F02B98E272D259C8EBADA74F315C74FAEE4A44331F985A218A96E1E96A19810436EAE79D5BD496A6BD461ECE5FB71614231878DD669204867E00B4B7FB5B2AC3FF0BE6C7B705FA9F96140F77C81765B4780B4195E5FE5A1D18F447E09845AE159E07C0FB514F07AB; geo=CN; X-Apple-I-Web-Token=AAAAKzExfDNmNDk0ZjczNDlhMGYwZWEwNDU2YzkzYWE5ZTE0ODMzAAABkTZq+mr/V2uoJN9kIJfaMxRJ+jdV4u/knXmufheQKJ3zq0RLB7ch2KrTnR++hGkNdsIxi8EnCF03Q9q7h3e0vSKRtSglZSE4BAKpQi7drzMBczXTtVXkk/Fcfr21f4ezRhqZs2ToA+qG/SyCANZDILmS1Xjn3IIZ/aAbM4BybEgGcNarrWnoBCj9iD56WfgU1VNs8EwJ7P9GLZUngRBd9ZyHdWntpt+GKdkQN9mTit23a2iRWaAG0skfSAPsJ5476QKn6UAixBE5Gr5XsHe3WlPyTv8J4M/khtP4N0fDDTQbwdLYfqyLTh/AbisYnkDDIZoGKdMXjxHeQuYOPcwjl4aJBuxFRamI9GndP3/KtZe9F/tk+3Z4SB+7jBfMY1XJD4rlCk6OcDc+cKzK0zNGZzZguWukQ0junebuw4PwGJYxEo8nSZpG6m+X0UtUloFhupKCBzEPUz9iVdWEpAVhIXb4kwvEDFuDs6c3lYnLVVBoV8HdCBAf80v5z2gXf9pWlwGt4bAX9aTST6LvRzL1p8NqWzLY5r2/v8VsPQ005RNxg8K+uDplKxYeypGK5zTegza2XBCbwwnZcnqCplapk5Pk6bKScUgPqqINUwpShmpNKVwKu8OhtgkZvYOv9YgGJYnd8DHYEuHRPTFxPjMkHe45M2d6xQKfKy453Dv8Bj7NXb5k33jIBnac/uHL3R5uk9lKtXdiUU1UOFSlXr/8pcgPyI8KrYWQTNyRhduzVFheJtu1LTK/2+TOyfgPZkHQ+9LSquTSz7Fwu8TfAXqVCs91jFXiaK1xYhGD6RD0ZZE0GQq6DLCoPF8QYqTYnBujm6fxz6g66nZYyAfcjBDZ80EFmxrn0Ou/3n/6aQHFPHqsDRkFa3JaJpxqPPUlmpzGfTqAaH1XlK+MoRAbssOnk3MNvivl03KDkydCb9QT2VTSsn0v6Atohw8uS2z7wuiZtVySyCW3kq2+A22z80JzD7pYLLnTVBiLDe4F7Mkd3FLgdrrUtAAm4PVKgsHApYA54BwnoeZoIrqjAAuC2DZzcWotc71UAMk1SOiNkVw=',
            "DNT": "1",
            "Pragma": "no-cache",
            "Referer": "https://iforgot.apple.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9d8TmTk25WKUfSHolk2dUJKy_Aw7GY5ay.EKY.6eke4FIidrQmVUavEp55BNlY5CGWY5BOgkLT0XxU..42Z"}',
            "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sstt": self.sstt_7,
        }
        response = requests.get(
            f"https://iforgot.apple.com{self.Location_2}",
            cookies=cookies,
            headers=headers,
        )
        self.question = response.json()
        self.x_apple_i_web_token_9 = response.cookies.get("X-Apple-I-Web-Token")
        self.sstt_8 = response.headers["Sstt"]
        return self

    @retry(tries=20)
    def Eleven(self):
        cookies = {
            "pltvcid": "undefined",
            "pldfltcid": "9d562bc73d6f4a3e8623983cd00792dc047",
            "idclient": "web",
            "dslang": "CN-ZH",
            "site": "CHN",
            "ifssp": self.ifssp,
            "geo": "CN",
            "X-Apple-I-Web-Token": self.x_apple_i_web_token_9,
        }

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            # 'Cookie': 'pltvcid=undefined; pldfltcid=9d562bc73d6f4a3e8623983cd00792dc047; idclient=web; dslang=CN-ZH; site=CHN; ifssp=A769EB512342739EBF9CDEE4E63BEE61F02B98E272D259C8EBADA74F315C74FAEE4A44331F985A218A96E1E96A19810436EAE79D5BD496A6BD461ECE5FB71614231878DD669204867E00B4B7FB5B2AC3FF0BE6C7B705FA9F96140F77C81765B4780B4195E5FE5A1D18F447E09845AE159E07C0FB514F07AB; geo=CN; X-Apple-I-Web-Token=AAAAKzEyfDNmNDk0ZjczNDlhMGYwZWEwNDU2YzkzYWE5ZTE0ODMzAAABkTZq+4iBz9cIIWg9ve81PppzikzoXM6/6WnosgfCwq0Wt6WCiHTbiDOp0JSEN1uBD6Zl2jOD+xifkwWlgaOSACYGxZajh49gXwqxGeE/Qb/bMjREkMkWjpq2zwQvr9Jp05LI80IRQPkU+Y1c9yd4gkLuX01D2lben68ukp+RG/UMEVfraT4T72tWVa04m4Jbpt4SwLLyIXySwi19j+ltxb1Wv7BJLIUwlseFuV8HhATNTAh7/qkT/Itv6AB/NSHx/1YDwpEllQhA1q+/jxrJhJS1OcuzbZ/2cyIUMheFlzpFI/hu4f6dIYyv48QZWn/qBM67SjIpm+1aSjqHBwCuo6WaNxNRqHjQbAaJr4QxwC4M85AcUAYJH6ZKfasey8y2INxfb6EmRq+S9D8TnwMJQ1PrAtbDA02NYlZCmAWlnPBz+6JFFEmwu2/JK4nRL1oQPClmhCmtrdxurL8jGZoZB+/C3oRl3Lc8a/v6qm4pOpNJDcYwXlsA/JEo0VRoHbnQburKJnUHIoXTAAC2DkCkXKgFZMYbN0H5OkPhyZKVIUR6SjgE7HmXlEJphznoG8RghsBTZdc/K2FMu/QmrCGvfynnj2y7WX+w9U5ZYC8cvM0qAdaNSjawdnCntMeFM/jBNsiml00/35JqVD48bWz0U7yYzPxJJTjWsvnubsQESBniB5fxkGgpYJqbYdSqAxslJRoRQ55HFxxsdlppdinEX+jARxsBUtltuhDHDI0u/3ML4Tn2niSf2lqAQrbE8HTBEKc91zdMzkDqRuw4rqCKJzuubZVGkj5zhwR1p/B3NYIQk00Y5w15IoqceG8RXGmwhUNOdFGCSNnHRHPMUbCUWBMTVVlhIqpj7Sc6Oe3QVF4xumy7gNODAg6W8UPKp7kKhaF9EoAOrezRKvO8/cd8fMs61fMhvAEvww6RXB2dv/4XwCKePcrjVut/rHe8VHYsEMHAarH9z2jFUDioaWKLxIPAluN+yiOURgiEz0u7mhkSs/49KgAm4PVbjBs1pInC2HyLOVAawwNFdqDwUhtRgvcddvMrDhznHqY7Nns=',
            "DNT": "1",
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
            "sstt": self.sstt_8,
        }
        questions_answers = {
            self.question_one: self.answer_one,
            self.question_two: self.answer_two,
            self.question_three: self.answer_three,
        }

        answers = []
        questions = self.question["questions"]
        for question in questions:
            if question["question"] == self.question_one:
                answer = questions_answers.get(self.question_one)
            elif question["question"] == self.question_two:
                answer = questions_answers.get(self.question_two)
            elif question["question"] == self.question_three:
                answer = questions_answers.get(self.question_three)
            else:
                answer = ""

            answers.append(
                {
                    "question": question["question"],
                    "answer": answer,
                    "number": question["number"],
                    "id": question["id"],
                }
            )

        json_data = {
            "questions": answers,
        }

        response = requests.post(
            "https://iforgot.apple.com/unenrollment/verify/questions",
            cookies=cookies,
            headers=headers,
            json=json_data,
            allow_redirects=False,
        )
        # print(response.headers)
        # print(response.status_code)
        # print(response.text)
        self.x_apple_i_web_token_10 = response.cookies.get("X-Apple-I-Web-Token")
        self.Location_3 = response.headers["Location"]
        self.sstt_9 = response.headers["sstt"]
        return self

    @retry(tries=20)
    def Twelve(self):
        cookies = {
            "pltvcid": "undefined",
            "pldfltcid": "9d562bc73d6f4a3e8623983cd00792dc047",
            "idclient": "web",
            "dslang": "CN-ZH",
            "site": "CHN",
            "ifssp": self.ifssp,
            "geo": "CN",
            "X-Apple-I-Web-Token": self.x_apple_i_web_token_10,
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
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9d8TmTrNldHrurJhBR.uMp4UdHz13NlejV2pNk0ug9WJ3veSqwc6tinwlWY5BNlYJNNlY5QB4bVNjMk.1vC"}',
            "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sstt": self.sstt_9,
        }

        response = requests.get(
            f"https://iforgot.apple.com{self.Location_3}",
            cookies=cookies,
            headers=headers,
        )
        # print(response.text)
        # print(response.headers)
        # print(response.status_code)
        self.x_apple_i_web_token_11 = response.cookies.get("X-Apple-I-Web-Token")
        self.sstt_10 = response.headers["sstt"]
        return self

    @retry(tries=20)
    def thirteen(self):
        url = "https://iforgot.apple.com/unenrollment"
        headers = {
            "Host": "iforgot.apple.com",
            "Connection": "keep-alive",
            "Content-Length": "0",
            "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "Accept": "application/json, text/plain, */*",
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9d8NTlFke1azLu_dYV6Hycfx9MsFY5CKw.Tf5.EKWJ9VbSIij__UeBz21BNlY5BPY25BNnOVgw24uy.1hq"}',
            "sstt": self.sstt_10,
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            "sec-ch-ua-platform": '"Windows"',
            "Origin": "https://iforgot.apple.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://iforgot.apple.com/",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; geo=CN; pldfltcid=9d562bc73d6f4a3e8623983cd00792dc047; pltvcid=undefined; ifssp={self.ifssp}; X-Apple-I-Web-Token={self.x_apple_i_web_token_11}",
        }
        data = ""
        response = requests.post(
            url=url, headers=headers, data=data, allow_redirects=False
        )
        # print(response.headers)
        # print(response.status_code)
        self.Location_4 = response.headers["Location"]
        self.x_apple_i_web_token_12 = response.cookies.get("X-Apple-I-Web-Token")
        return self

    @retry(tries=20)
    def fourteen(self):
        url = f"https://iforgot.apple.com{self.Location_4}"
        headers = {
            "Host": "iforgot.apple.com",
            "Connection": "keep-alive",
            "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "Accept": "application/json, text/plain, */*",
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9d8NTlFke1azLu_dYV6Hycfx9MsFY5CKw.Tf5.EKWJ9VbSIij__UeBz21BNlY5BPY25BNnOVgw24uy.1hq"}',
            "sstt": self.sstt_10,
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            "sec-ch-ua-platform": '"Windows"',
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://iforgot.apple.com/",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; geo=CN; pldfltcid=9d562bc73d6f4a3e8623983cd00792dc047; pltvcid=undefined; ifssp={self.ifssp}; X-Apple-I-Web-Token={self.x_apple_i_web_token_12}",
        }
        response = requests.get(url=url, headers=headers)
        # print(response.text)
        self.sstt_11 = response.headers["sstt"]
        self.x_apple_i_web_token_13 = response.cookies.get("X-Apple-I-Web-Token")
        return self

    @retry(tries=20)
    def fifteen(self):
        url = "https://iforgot.apple.com/unenrollment/reset"
        headers = {
            "Host": "iforgot.apple.com",
            "Connection": "keep-alive",
            "Content-Length": "26",
            "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "sstt": self.sstt_11,
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":".la44j1e3NlY5BNlY5BSmHACVZXnNA9d8NTlI870jpidPNs0oje9zH_y37lYKU.6elV2pNK1c8rJvftOMuYEn85BNlY5CGWY5BOgkLT0XxU..0p9"}',
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
            "sec-ch-ua-platform": '"Windows"',
            "Origin": "https://iforgot.apple.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://iforgot.apple.com/",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; geo=CN; pldfltcid=9d562bc73d6f4a3e8623983cd00792dc047; pltvcid=undefined; ifssp={self.ifssp}; X-Apple-I-Web-Token={self.x_apple_i_web_token_13}",
        }
        json_data = {"password": self.password}
        response = requests.post(url=url, headers=headers, json=json_data)
        print(response.text)


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
        apple.Twelve()
        apple.thirteen()
        apple.fourteen()
        apple.fifteen()
        return apple

    # 使用示例
    result = start_process(
        # username="versity@mac.com",
        username="yohtaydarv11@gmail.com",
        password="Aa147369a1",
        year_item="1993",
        monthOfYear_item="05",
        dayOfMonth_item="25",
        question_one="你少年时代最好的朋友叫什么名字？",
        answer_one="py12345",
        question_two="你的理想工作是什么？",
        answer_two="gz12345",
        question_three="你的父母是在哪里认识的？",
        answer_three="fm12345",
    )
    print(result)
