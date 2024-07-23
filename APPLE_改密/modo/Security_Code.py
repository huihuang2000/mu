import requests, re, ddddocr
from urllib.parse import unquote, quote

ocr = ddddocr.DdddOcr(
    det=False,
    show_ad=False,
    ocr=False,
    import_onnx_path="APPLE_改密/modo/A1.onnx",
    charsets_path="APPLE_改密/modo/charsets.json",
)


class APPLE:
    def __init__(self) -> None:
        self.password = "Aa147369"
        self.username = "maverickke05y@outlook.com"
        self.year_item = "1993"
        self.monthOfYear_item = "05"
        self.dayOfMonth_item = "25"
        self.question_one = "你少年时代最好的朋友叫什么名字？"
        self.answer_one = "py123456"
        self.question_two = "你的理想工作是什么？"
        self.answer_two = "gz123456"
        self.question_three = "你的父母是在哪里认识的？"
        self.answer_three = "fm132456"
        self.pass_1 = "py123456"
        self.pass_2 = "gz123456"
        self.pass_3 = "fm123456"

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

    def Identification_codes(self):
        self.res = ocr.classification(self.captcha)
        return self

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

    def Change_password(self):
        cookies = {
            "idclient": "web",
            "dslang": "CN-ZH",
            "site": "CHN",
            "ifssp": self.ifssp,
            "geo": "CN",
            "X-Apple-I-Web-Token": self.x_apple_i_web_token_3,
        }

        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://iforgot.apple.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9cedH1Zd9PzLu_dYV6Hycfx9MsFY5Bhw.Tf5.EKWJ9VbHb4uyL4yZnxHGY5BNlYJNNlY5QB4bVNjMk..Dc"}',
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sstt": self.sstt,
        }

        params = {
            "sstt": self.sstt_2,
        }

        response = requests.get(
            "https://iforgot.apple.com/recovery/options",
            params=params,
            cookies=cookies,
            headers=headers,
        )
        self.x_apple_i_web_token_4 = response.cookies.get("X-Apple-I-Web-Token")
        self.sstt_3 = response.json()["sstt"]
        return self

    def Convert(self):
        cookies = {
            "idclient": "web",
            "dslang": "CN-ZH",
            "site": "CHN",
            "geo": "CN",
            "ifssp": self.ifssp,
            "X-Apple-I-Web-Token": self.x_apple_i_web_token_4,
        }

        headers = {
            "Accept": "text/html;format=fragmented",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Pragma": "no-cache",
            "Referer": "https://iforgot.apple.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9ceidTojLJ26Lu_dYV6Hycfx9MsFY5CKw.Tf5.EKWJ9VbHb4uyKAwmbticlY5BNleBBNlYCa1nkBMfs.2IE"}',
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sstt": self.sstt_3,
        }

        response = requests.get(
            "https://iforgot.apple.com/recovery/options",
            cookies=cookies,
            headers=headers,
        )
        self.x_apple_i_web_token_5 = response.cookies.get("X-Apple-I-Web-Token")
        return self

    def Passed_302_2(self):
        headers = {
            "Host": "iforgot.apple.com",
            "Connection": "keep-alive",
            "Content-Length": "35",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sstt": quote(self.sstt_3),
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9ceieFSOTjGUfSHolk2dUJKy_Aw7GY5ey.EKY.6eke4FIdIXxU94ycfxJclY5BNleBBNlYCa1nkBMfs.0VE"}',
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua-platform": '"Windows"',
            "Origin": "https://iforgot.apple.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://iforgot.apple.com/",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; geo=CN; ifssp={self.ifssp}; X-Apple-I-Web-Token={self.x_apple_i_web_token_5}",
        }
        json_data = {"recoveryOption": "reset_questions"}
        response = requests.post(
            "https://iforgot.apple.com/recovery/options",
            headers=headers,
            json=json_data,
            allow_redirects=False,
        )
        self.x_apple_i_web_token_6 = response.cookies.get("X-Apple-I-Web-Token")
        self.sstt_4 = unquote(response.headers["sstt"])
        return self

    def Show_brief_information(self):
        cookies = {
            "idclient": "web",
            "dslang": "CN-ZH",
            "site": "CHN",
            "geo": "CN",
            "ifssp": self.ifssp,
            "X-Apple-I-Web-Token": self.x_apple_i_web_token_6,
        }

        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://iforgot.apple.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9ceOHe_W74jpidPNs0oje9zH_y37lYKU.6elV2pNK1c8odlTr_1z1KyL3NlY5BNp55BNlan0Os5Apw.D96"}',
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sstt": quote(self.sstt_3),
        }

        params = {
            "sstt": self.sstt_4,
        }

        response = requests.get(
            "https://iforgot.apple.com/questions/verify/password",
            params=params,
            cookies=cookies,
            headers=headers,
        )
        self.sstt_5 = response.json()["sstt"]
        self.x_apple_i_web_token_7 = response.cookies.get("X-Apple-I-Web-Token")
        return self

    def passed_302_3(self):
        cookies = {
            "idclient": "web",
            "dslang": "CN-ZH",
            "site": "CHN",
            "geo": "CN",
            "ifssp": self.ifssp,
            "X-Apple-I-Web-Token": self.x_apple_i_web_token_7,
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
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"Fla44j1e3NlY5BNlY5BSmHACVZXnNA9ceOHeudv9CUfSHolk2dUJKy_Aw7GY5ey.EKY.6eke4FIdIXxj94y3fxHGY5BNlYJNNlY5QB4bVNjMk.01e"}',
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sstt": quote(self.sstt_5),
        }

        json_data = {
            "password": self.password,
        }

        response = requests.post(
            "https://iforgot.apple.com/questions/verify/password",
            cookies=cookies,
            headers=headers,
            json=json_data,
            allow_redirects=False,
        )
        self.sstt_6 = unquote(response.headers["sstt"])
        self.x_apple_i_web_token_8 = response.cookies.get("X-Apple-I-Web-Token")
        return self

    def passed_302_4(self):
        cookies = {
            "idclient": "web",
            "dslang": "CN-ZH",
            "site": "CHN",
            "geo": "CN",
            "ifssp": self.ifssp,
            "X-Apple-I-Web-Token": self.x_apple_i_web_token_8,
        }

        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://iforgot.apple.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"Fla44j1e3NlY5BNlY5BSmHACVZXnNA9ceOHeudv9CUfSHolk2dUJKy_Aw7GY5ey.EKY.6eke4FIdIXxj94y3fxHGY5BNlYJNNlY5QB4bVNjMk.01e"}',
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sstt": quote(self.sstt_5),
        }

        params = {
            "sstt": self.sstt_6,
        }
        response = requests.get(
            "https://iforgot.apple.com/questions/reset/options",
            params=params,
            cookies=cookies,
            headers=headers,
            allow_redirects=False,
        )
        self.sstt_7 = unquote(response.headers["sstt"])
        self.x_apple_i_web_token_9 = response.cookies.get("X-Apple-I-Web-Token")
        return self

    def three_factor_authentication(self):
        cookies = {
            "idclient": "web",
            "dslang": "CN-ZH",
            "site": "CHN",
            "geo": "CN",
            "ifssp": self.ifssp,
            "X-Apple-I-Web-Token": self.x_apple_i_web_token_9,
        }

        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://iforgot.apple.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"Fla44j1e3NlY5BNlY5BSmHACVZXnNA9ceOHeudv9CUfSHolk2dUJKy_Aw7GY5ey.EKY.6eke4FIdIXxj94y3fxHGY5BNlYJNNlY5QB4bVNjMk.01e"}',
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sstt": quote(self.sstt_5),
        }

        params = {
            "sstt": self.sstt_7,
        }

        response = requests.get(
            "https://iforgot.apple.com/questions/verify/questions",
            params=params,
            cookies=cookies,
            headers=headers,
        )
        self.sstt_8 = response.json()["sstt"]
        self.x_apple_i_web_token_10 = response.cookies.get("X-Apple-I-Web-Token")
        self.three_times = response.json()
        print(response.text)
        return self

    def passed_302_5(self):
        cookies = {
            "idclient": "web",
            "dslang": "CN-ZH",
            "site": "CHN",
            "geo": "CN",
            "ifssp": self.ifssp,
            "X-Apple-I-Web-Token": self.x_apple_i_web_token_10,
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
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9ceOHd750qjpidPNs0oje9zH_y37lYKU.6elV2pNK1c8odlTr_1z1Ky3clY5BNleBBNlYCa1nkBMfs.76k"}',
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sstt": quote(self.sstt_8),
        }

        questions_answers = {
            self.question_one: self.answer_one,
            self.question_two: self.answer_two,
            self.question_three: self.answer_three,
        }

        answers = []
        questions = self.three_times["questions"]
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
                    "id": question["id"],
                    "number": question["number"],
                }
            )

        json_data = {"questions": [answers[0]]}
        # json_data = {"questions":[{"question":"你少年时代最好的朋友叫什么名字？","answer":"py1234","id":130,"number":1}]}
        response = requests.post(
            "https://iforgot.apple.com/questions/verify/questions",
            cookies=cookies,
            headers=headers,
            json=json_data,
            allow_redirects=False,
        )
        self.sstt_9 = unquote(response.headers["sstt"])
        self.x_apple_i_web_token_11 = response.cookies.get("X-Apple-I-Web-Token")
        return self

    def all_security_information(self):
        cookies = {
            "idclient": "web",
            "dslang": "CN-ZH",
            "site": "CHN",
            "geo": "CN",
            "ifssp": self.ifssp,
            "X-Apple-I-Web-Token": self.x_apple_i_web_token_11,
        }

        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://iforgot.apple.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9ceOHd750qjpidPNs0oje9zH_y37lYKU.6elV2pNK1c8odlTr_1z1Ky3clY5BNleBBNlYCa1nkBMfs.76k"}',
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sstt": quote(self.sstt_8),
        }

        params = {
            "sstt": self.sstt_9,
        }

        response = requests.get(
            "https://iforgot.apple.com/questions/reset",
            params=params,
            cookies=cookies,
            headers=headers,
        )
        self.sstt_10 = response.json()["sstt"]
        self.x_apple_i_web_token_12 = response.cookies.get("X-Apple-I-Web-Token")
        self.available = response.json()
        return self

    def change_security_settings(self):
        cookies = {
            "idclient": "web",
            "dslang": "CN-ZH",
            "site": "CHN",
            "geo": "CN",
            "ifssp": self.ifssp,
            "X-Apple-I-Web-Token": self.x_apple_i_web_token_12,
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
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9ceTdHW9JWUfSHolk2dUJKy_Aw7GY5ey.EKY.6eke4FIdIXxjA9zJOy3clY5BNleBBNlYCa1nkBMfs.ChB"}',
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sstt": quote(self.sstt_10),
        }

        selected_questions = []
        answers = [self.pass_1, self.pass_2, self.pass_3]
        question_number = 1

        question_texts = [
            question["question"] for question in self.three_times["questions"]
        ]
        available_question_ids = {
            question["question"]: question["id"]
            for group in self.available["availableQuestions"]
            for question in group
        }

        for question_text in question_texts:
            question_id = available_question_ids[question_text]
            answer = answers.pop(0)
            selected_questions.append(
                {
                    "id": str(question_id),
                    "question": question_text,
                    "answer": answer,
                    "number": question_number,
                }
            )
            question_number += 1

        json_data = {"selectedQuestions": selected_questions}

        response = requests.post(
            "https://iforgot.apple.com/questions/reset",
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        print(response.text)


if __name__ == "__main__":
    apple = APPLE()
    apple.Get_sstt().get_verification_code().Identification_codes().Submit_302_1().Change_password().Convert().Passed_302_2().Show_brief_information().passed_302_3().passed_302_4().three_factor_authentication().passed_302_5().all_security_information().change_security_settings()
