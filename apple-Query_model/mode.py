import httpx
import json
import re

import requests

url = "https://www.apple.com/xc/us/vieworder/W1413294852/tlotdxdd@hotmail.com?e=true"

payload={}
headers = {
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Accept': '*/*',
   'Host': 'www.apple.com',
   'Connection': 'keep-alive',
#    'Cookie': 'dssid2=fba12486-0717-470a-a39e-120115db4bc8; dssf=1; as_pcts=KWjMHQLge-HkVf1UTw_gt1k-nybx8mm2:YY0CDA187JC+Qtvk_IiRkICLXBUDydqxs-v0VD1_aPeYGpEKqKNIfvF; as_dc=ucp3',
   'Referer': 'https://www.apple.com/xc/us/vieworder/W1413294852/tlotdxdd@hotmail.com?e=true'
}

response = requests.request("GET", url, headers=headers, data=payload).text

# print(response)


modo = r'"productName"\s*:\s*"([^"]+)"'
time = r'"orderPlacedDate"\s*:\s*"([^"]+)"'
dd = r'/shop/order/detail/\d+/([^"/]+)'
status = r'"deliveryDate"\s*:\s*"([^"]+)"'
MODO = re.search(modo, response)
TIME = re.search(time, response)
DD = re.search(dd, response)
status = re.search(status, response)
modo = MODO.group(1)
TIME = TIME.group(1)
DD = DD.group(1)
status = status.group(1)

if MODO:
    print(modo)
    print(status)  # 输出 productName 的值
  # 输出 productName 的值
else:
    print('productName 未找到')