# https://appleid.apple.com/
# {"账号": "aidenclrob@hotmail.com", "密码": "Aa147369"},
# {"账号": "my_hero.hero@softbank.ne.jp", "密码": "Aa147369"},
# {"账号": "yohtaydarv11@gmail.com", "密码": "Aa147369"},
# {"账号": "jacobgordon6s@hotmail.com", "密码": "Aa147369"},
# {"账号": "lovejessi06@gmail.com", "密码": "Aa147369"},
# {"账号": "sophiab2022@gmail.com", "密码": "Aa147369"},


import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
response = requests.get('https://appleid.apple.com/', headers=headers)
aidsp = response.cookies.get('aidsp')
print(aidsp)



cookies = {
    'aidsp': aidsp,
    'myacinfo': 'DAWTKNV323952cf8084a204fb20ab2508441a07d02d3bca5d3dce3d3e1a5538a8d7077fa7dc610ac745e7de2181a73562ebd8fa0bfd0f28241735566f885118047f7c0c61fa23c272c75603f134b2d60e1d40a8d20fbf2ce52613a81c2ff4483e394571aeb1f726bc461b85f79ef7d40e32b5ac718ca87ab4ddf1fc553e59ac38e1df7d44bb21a03e89a8173a4214359132ebd3d5cefaaca6b8fab65141e5b054f374d3162087ea4695d64fcf48fea74f7d0509ec253e5f2c720955b6fcf24cd164853bda8b6ab44a27760a423127571a8b891709656b6c032f6787991d33cc99d7b823dc599081e3ad80dfc0c30ce415e592c25c121fd58a792acf1e411ea1ec4e2874b8df690d2894ad3567ab0517616b7ed8718de857233acd279306fc222c83d4851c427a6327c515c803b2b58840dabe441be82f96a71c8ef1b3419b406cbea2e2e375b3d7c6401d1729e835384079174bd15d19760d0d28370436f8ec0def91d3055dab28aa7169259b37964c9600e4237f736db928db7ae418685b0def0e89fb79fe6925ff838ba466cebde4a8889655be092d44428c9f136c081e093eee400703f92c5bd47b90f5628259e0df5e7517cec28e1aaf58e615592b687467a19e18b8f3e51477ad1b30976b9896b5c551a99b4e381bcaeb2e4ae3564b6de662a6b5ab73e742e286c2b2e9d6b9aeb8a458bb377bdb2090e4e0003368063902cef7eed4633585a47V3',
}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
response = requests.get('https://appleid.apple.com/account/manage/gs/ws/token', cookies=cookies, headers=headers)
awat = response.cookies.get('awat')
print(awat)