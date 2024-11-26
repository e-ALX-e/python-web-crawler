import requests
import time

# 爬取页数
page_sum = 1
# URL
url = 'https://www.cqvip.com/website/advanceSearch'

params = {
    "types": [1, 2, 3, 5, 6, 18],
    "page": 4,
    "size": 20,
    "yearStart": "",
    "yearEnd": "",
    "isCore": None,
    "isOA": None,
    "pdf": None,
    "sort": "",
    "order": False,
    "language": "zh",
    "ags": False,
    "openForceTranslate": True,
    "indexSearch": True,
    "resultField": [
        "newspaperInfo",
        "mediaName",
        "providerSource",
        "appNo",
        "pubNo",
        "otherOrganInfo",
        "cqvipIsOa"
    ],
    "thesis": None,
    "standard": None,
    "conditions": [
        {
            "content": "国内航天材料",
            "logicalOperator": "AND",
            "searchField": "U",
            "exact": False,
            "field": "U"
        }
    ],
    "aggsParams": {},
    "agsList": [
        {"code": "type", "size": 15},
        {"code": "conferenceLevel", "size": 10},
        {"code": "thesisType", "size": 10},
        {"code": "standardType", "size": 10},
        {"code": "language", "size": 10},
        {"code": "HQLXY", "size": 10},
        {"code": "Y", "size": 5},
        {"code": "C", "size": 5},
        {"code": "range", "size": 5, "params": ["SCIE", "SSCI", "ESCI", "AHCI", "EI", "CAS", "IEEE", "NATURE", "PUBMED", "BDHX", "CSCD", "CSSCI", "EAPJ", "JCR", "ZKYM"]},
        {"code": "S", "size": 0},
        {"code": "J", "size": 0},
        {"code": "A", "size": 0},
        {"code": "LO", "size": 0}
    ]
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',  # 如果需要授权，请添加
    'Cookie':'_ga=GA1.2.2012846155.1717160616; duid=lthvPliI; Hm_lvt_a38af0f77bbdf5fd378df4a59b720f89=1721741914; Hm_lvt_7d5147872a02e6f213641cbe78729d3a=1721741914; Hm_lvt_0efb33febb4e366c6fae786b1d386e42=1721741914; __root_domain_v=.cqvip.com; _qddaz=QD.295921741914942; lastSE=baidu; _ga_JC4E5X0YMM=GS1.2.1729090268.7.1.1729090525.0.0.0; cqvipenv=zs; _webtracing_session_id=s_134da7a7-a5ab82d5-6ba4ceb66adf3fab; Hm_lvt_1c945aa1031a2d1265a3b70eb20fa06c=1729090155,1729244238; HMACCOUNT=E1F2AA59B3F53A36; Hm_lvt_18d48281ea2a34e00ecc554e90c8ed31=1729090154,1729244238; _webtracing_device_id=t_134da7a7-a5ab9bec-b71573c486af3415; vip-auth-token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOjE4NDcyMTA4MDY4MjgyMDgxMjksInV2IjoiMTcyOTI0NDM1MDY0OCIsInJvbGUiOlsiIl0sImR1aWQiOiJsdGh2UGxpSSIsInRrIjoiNDIxM2I4MDY3YmFkNGMxODllYWJjMGJhYTAxNmFlOTciLCJ0aW1lIjoxNzI5MjQ0MzUwNjQ4LCJhaWQiOjB9.YhTcGHZTVIc_ubibvtRvfErBs8yH_qynQ-e-fokzxqM; _qdda=3-1.1nmo93; _qddab=3-zcqopd.m2ejx9sc; Hm_lpvt_1c945aa1031a2d1265a3b70eb20fa06c=1729245269; Hm_lpvt_18d48281ea2a34e00ecc554e90c8ed31=1729245269; ali-code=%257B%2522a%2522%253A%2522FFFF0N0000000000B14C%2522%252C%2522c%2522%253A%2522FFFF0N0000000000B14C%253Anvc_other%253A1729245269477%253A0.9019198855630934%2522%252C%2522d%2522%253A%2522nvc_other%2522%252C%2522j%2522%253A%257B%2522test%2522%253A1%257D%252C%2522h%2522%253A%257B%2522umidToken%2522%253A%2522T2gAax9mDDpPY4EQ33vSkseQ4dBhWg0JNOC5dz4UeESQX6f8ifil0XlOGUG7rskVpyk%253D%2522%257D%252C%2522b%2522%253A%2522231!tY%252B3v4mUlAk%252Bjol%252B6rpC5k8FVXolRTJob%252BvClIbcpsKTbS8ErrJgBV%252B1HpRbhiJCEhFJMkR38W%252Fc45w7miotDDYOsQVgiH%252FJavBSKM3hGmZW4fOw1q2SpIDQw5uA3ssW47YURJDBxPw6Fyv8eT%252Fe6CasnRHaO%252Bgm6h3kOT9jNBavtiD%252BUu8e%252BZd%252B%252B6WF1cGDh%252BtRHJBh%252B%252B%252Bj%252BygU3%252BjOFGzIRx%252BdFkk3k6D6yMsaqjjMfGKXjvlE4WJ3Ko2FfHi9qLCcYHeqLtAqXRWow8U3jREZDj8KAhweuUJmj80vUs%252Fqde4imrYHdUAT3RrnjnKtqhT9kTfMuTkLAzMvUbL%252FuZrNSG%252BBY7ZdybLgRtvdgHPfv%252FTkzR16C7B210UuN%252FNF528SDlgPED6VfvCno9iUb4FczypxroQ7HMT4TvW%252FnSJpSNNTxqW0utQm%252Bvt7OYeopYIAcaT%252BMJyuivyW%252BbHicPhmsudRlUeOl2dT84hQz8J5kYRFsVpVTKO0NJVoTPBJMb%252FOWht11cZldHe4XxWTImgMl9FW7Rfv2G1Zubv4Ydj2GJLjAgFfeG8i1UD1mhvd4Ybq%252BhV1zjsXks4axa8rNBFmJ9xBGJOzisWBdUZn0nxKE9Z4jRg05uw2Sqy9DF8VM9HgIH3OyPQpGxdQ1b%252Fkx273tumAeZK%252B%252Fv2UALpSGS2obHxY6Scyg5WoBjid6zkVeZftXEYI7XasvR1JHk64tqfhJ2PrCHoecTVkVmK6%252BPOsYTlwemGDdFgIcOSqF5gTjikY8MNpe3UKmUf9vYR0UM4mqIzMz3yolGVCti90jmq0nb68SIGoGuG6Tzuwid9syRttN5zgIw5HA3pPtNUuwnDAgf4sS%252BqbHx34LDXC56CBW880GYINacGFKrS44kps1AZX4vknuNIQLbmG%252B%252FeK0Mt251SrwFqEiJx7lWmLA6EqOmMwEwRpA8HSwVewtiOIWer7fuJdwa07xtJmW9gxBXHlSsKfNxmR0gQNmzY2yZbsbsNBMErt4JmRdHKab6KIpxDXI9ZMouSGIuyvFDFZgE62Cz4ihJpVZ39%252BAOJaXEiMBilkCoTJzjY7%252FU1TrOvvPGNVt0%252BMEkWgsTBQB4lyWDtE%252FhXnQrByqrNl5MOaDfG%252BoNpUPv6KOtoif%252FOIso2bmRzzqtzSxQOQy2jVvbDku8wpjPuUFlAV06JgX7rbIRf5gX3CGT1V%252Fo0QZDjlFrzRsR7wlfIe3x1qSlRWA9bf%252FO4vyDwvHI08LKstiRiQGit4pgpXan%252BFfVqlkX3%252Ft3p6ssyyjohYn5m8KLx3RVazofUTNy8COsR%252Fo3JzoMq0qFrFnKhYB31d3zm%252F86XfQ6M%252BuXKcJtBWywhA0EvaP5jlBcgX2zMfJFNTgjxoP%252ByBVNflzcvTulSRzinj%252Fx3614kB%252FHdSYV5D7mRBzcIBb24RhXVEAUG8E2H09cl2BveoqkLIWbY1nntfD1jhQOuYFFTKW8I7xsF0V9gKxR%252F3exuTEuFdtK3A7JXtCW%252FuruR%253D%2522%257D; tfstk=gx_nNzZLPM-BjOm6F58QqlTnU3E9jXTWbT3JeUpzbdJspv3daLYPi9vJ4JTdrOfPnWO8dahCftCqJwEBy4YBPUyYHrUy96TWz7VS4jcB7IRm4zKE8P5QmUeHlrUAO6Pz4WX0kwKp799XUU-e4CzwCIGeTT-EQCJ6NQkea2PG_d9Z44JeUclwiIcezUWP_5AIHPoeHaSV7JavCaS6kyjptHvVTp5d0NoycD12INbO5Bb3Z6vM6CQMtMv2X7CJdwWOawQBf-D2P1IcEgW7DcThaM8eM6anSE5FXaAOy7nkL9_G_N-iMqLlY9jycG4jcH-kKG7ejbuP1Ujw0gX3KD9FvOxX_hlulCBvQ6_Fj7MNTtpH8C-TuSfw4GQBcweZ-ESf9eIPFon6-_SeSgW-bm-8c4OawNoSVHR6tKEaKwhftW5a85ViD_te1I9Ys5mSVHR6sKFgsmCWYCOXH'
}
for page in range(1, page_sum + 1):
    params['page'] = page
    response = requests.post(url=url, json=params, headers=headers)
    print(f"Page {page} Response: {response.status_code}")
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Failed to fetch data for page {page}: {response.text}")
    time.sleep(1)  # 增加延迟，避免频率限制