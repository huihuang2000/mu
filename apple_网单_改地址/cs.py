import requests

cookies = {
    'dssid2': '2831cb99-bac8-4f9a-847a-1d01848126e5',
    'dssf': '1',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'pxro': '1',
    'as_dc': 'ucp5',
    's_fid': '05BD90C97D09DACB-0E981AE8E5C89EE3',
    's_vi': '[CS]v1|332FB030F1DF1F6E-40001050081DBF4C[CE]',
    'as_pcts': 'R:8tGpf187I:o9KOkfnutY169q9Y7bLD7cV0v6ZRYCRXfAK-mzTp_89QdYyzzgrFNdY-QKXnc8x55MW5EqB+3_PBjhf8H2BeNp2xgLRV0LKD+alrGcK-5HWvglITbj14EwK0sZNVFB3lUZhnVdN9:ec6asJSA2+MVQFofjtf4uCrkUHYN4U38UNk',
    's_cc': 'true',
    'as_rumid': 'c643af2b-2aef-467f-b089-295dd3aa3fbc',
    'dslang': 'US-EN',
    'site': 'USA',
    'geo': 'CN',
    'as_cn': '~ABE5M1_eyIVWy5JqKVhJ-FJstBKzA_lw8iPk8JQHGxI=',
    'as_disa': 'AAAjAAABtQk42s9PFb7aNkkPk54TvT2ktvX3XjwxveqJVIgUlxUAAgFDUMXqOfgzJl4mR1saALED4p36U_I_kuHKBBsAbEus7A==',
    'as_rec': 'b80c98cde40c9d152ad6ed42b06fe34f0e75de19bebecd3d42d640f1661e61224377592a20ebeec6926e7c6ed0be3c0dea5f0e533a45ab9d66874469e076dd096afd384b6b7e8380466627e58e5ce92c',
    'as_ltn_us': 'AAQEAMHd19vvg4jZFr57qCXF7A19IJ1I_dXGEF12EvUxBEDCMUe4c26VeuELC7Pkmeiq31BSzo_pO5c00mlgkwaepXgqKBbe71A',
    's_sq': 'applestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253DAOS%25253A%252520orders%25252Forder_detail%2526link%253Dedit%252520%252528inner%252520text%252529%252520%25257C%252520no%252520href%252520%25257C%252520body%2526region%253Dbody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DAOS%25253A%252520orders%25252Forder_detail%2526pidt%253D1%2526oid%253Dfunctionkd%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DBUTTON',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    # 'content-length': '0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'dssid2=2831cb99-bac8-4f9a-847a-1d01848126e5; dssf=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; as_dc=ucp5; s_fid=05BD90C97D09DACB-0E981AE8E5C89EE3; s_vi=[CS]v1|332FB030F1DF1F6E-40001050081DBF4C[CE]; as_pcts=R:8tGpf187I:o9KOkfnutY169q9Y7bLD7cV0v6ZRYCRXfAK-mzTp_89QdYyzzgrFNdY-QKXnc8x55MW5EqB+3_PBjhf8H2BeNp2xgLRV0LKD+alrGcK-5HWvglITbj14EwK0sZNVFB3lUZhnVdN9:ec6asJSA2+MVQFofjtf4uCrkUHYN4U38UNk; s_cc=true; as_rumid=c643af2b-2aef-467f-b089-295dd3aa3fbc; dslang=US-EN; site=USA; geo=CN; as_cn=~ABE5M1_eyIVWy5JqKVhJ-FJstBKzA_lw8iPk8JQHGxI=; as_disa=AAAjAAABtQk42s9PFb7aNkkPk54TvT2ktvX3XjwxveqJVIgUlxUAAgFDUMXqOfgzJl4mR1saALED4p36U_I_kuHKBBsAbEus7A==; as_rec=b80c98cde40c9d152ad6ed42b06fe34f0e75de19bebecd3d42d640f1661e61224377592a20ebeec6926e7c6ed0be3c0dea5f0e533a45ab9d66874469e076dd096afd384b6b7e8380466627e58e5ce92c; as_ltn_us=AAQEAMHd19vvg4jZFr57qCXF7A19IJ1I_dXGEF12EvUxBEDCMUe4c26VeuELC7Pkmeiq31BSzo_pO5c00mlgkwaepXgqKBbe71A; s_sq=applestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253DAOS%25253A%252520orders%25252Forder_detail%2526link%253Dedit%252520%252528inner%252520text%252529%252520%25257C%252520no%252520href%252520%25257C%252520body%2526region%253Dbody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DAOS%25253A%252520orders%25252Forder_detail%2526pidt%253D1%2526oid%253Dfunctionkd%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DBUTTON',
    'dnt': '1',
    'modelversion': 'v2',
    'origin': 'https://secure8.store.apple.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://secure8.store.apple.com/shop/order/detail/10078/W1047001362',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'syntax': 'graviton',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'x-aos-model-page': 'OrderStatusDetail',
    'x-aos-stk': '915696b4c808c283f87adeb45f83de6cbc9e506ef7e10a6063d8a61a6ae966ec',
    'x-requested-with': 'Fetch',
}

params = {
    '_a': 'editShippingAddress',
    '_m': 'orderDetail.orderItems.orderItem-0000101.shippingInfo',
}

response = requests.post(
'https://secure8.store.apple.com/shop/order/detailx/10078/W1047001362',
    params=params,
    cookies=cookies,
    headers=headers,
)
print(response.text)