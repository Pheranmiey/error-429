# -*- coding: utf-8 -*-
"""help!.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LZrmomXMDi_elHnc6lv0dT9ekLVr_6jC
"""

!pip install --upgrade pytrends

from pytrends.request import TrendReq
import time
import requests.exceptions

def get_trending_searches(keyword, location, timeframe, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            pytrends = TrendReq(hl='en-US', tz=360)
            pytrends.build_payload([keyword], cat=0, timeframe=timeframe, geo=location, gprop='youtube')

            # Introduce a delay to avoid rate limiting issues
            time.sleep(10)

            trending_data = pytrends.related_queries()

            if trending_data is not None and keyword in trending_data and trending_data[keyword]['top'] is not None:
                top_trending = trending_data[keyword]['top'].head(10).reset_index(drop=True)

                # Add a date and time column for each row
                interest_over_time_data = pytrends.interest_over_time()
                if not interest_over_time_data.empty:
                    top_trending['datetime'] = interest_over_time_data.index.strftime('%Y-%m-%d %H:%M:%S').tolist()[0]
                else:
                    print(f"No interest over time data available for {keyword}")
                    return None

                return top_trending
            else:
                print(f"No top trending queries found for {keyword} in the specified timeframe and location.")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Request failed. Retrying... ({retries + 1}/{max_retries})")
            time.sleep(2 ** retries)  # Exponential backoff
            retries += 1

    print("Max retries reached. Unable to fetch data.")
    return None

# Example usage
top_trending_results = get_trending_searches('liverpool', 'US', 'today 1-m')

if top_trending_results:
    print(top_trending_results)

from pytrends.request import TrendReq as UTrendReq
GET_METHOD='get'

import requests

headers = {
    'authority': 'trends.google.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '__utma=10102256.344521759.1709276378.1709276411.1709276411.1; __utmc=10102256; __utmz=10102256.1709276411.1.1.utmcsr=trends.google.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; __utmb=10102256.14.9.1709276741239; SID=g.a000gwi_xA2Q93VJpJmLblUeoTXgIsCTm4OyroY_zZVYdq1WPAxpWDub5lMyBiVAojb9L_zrqgACgYKAZISAQASFQHGX2MipoCNey0h9V5SyMsj6TYkoxoVAUF8yKo7GqrAu6IrZMPhZsVnCT_d0076; __Secure-1PSID=g.a000gwi_xA2Q93VJpJmLblUeoTXgIsCTm4OyroY_zZVYdq1WPAxpdpr0xW-1RgdR48VUCu4UmAACgYKAfcSAQASFQHGX2MiG8WcS0ZvyDMhYbMUc_HcdRoVAUF8yKq3v1N0bOs7m-zm7sF7pS5X0076; __Secure-3PSID=g.a000gwi_xA2Q93VJpJmLblUeoTXgIsCTm4OyroY_zZVYdq1WPAxp-_JFH03yLtsi3I1EZfLmRgACgYKATASAQASFQHGX2Mi0uSbRjArvhoSFV-Jmva3dBoVAUF8yKpPQMhgwt7VSoDqTK0auGzf0076; HSID=AFz4N-rAN2NMqLwiQ; SSID=AM629nAx2Zw7ZMofU; APISID=-Ry7Xnk7l5ijrdAp/A55qmbuosPhhpw_HG; SAPISID=G3Oo1Lwa7GpP74cW/ABwE4bEPWeGSLBe11; __Secure-1PAPISID=G3Oo1Lwa7GpP74cW/ABwE4bEPWeGSLBe11; __Secure-3PAPISID=G3Oo1Lwa7GpP74cW/ABwE4bEPWeGSLBe11; 1P_JAR=2024-03-01-06; AEC=Ae3NU9N0TSFkftnsWn4K_Pk2OIrOv-fmJ7NOxvf298pnvPKrNzDVFk_aCg; __Secure-ENID=17.SE=DMGJjJ7Z7kqWnFkeQUd6srbnRi8zOOHYhubnvL2nw6HxlGwsWaCUEL-JsdWhE5sokAtwhI-n8pPxebHvl7w-3UsJm7qnKnLgpjussbWghgyNrS2sq6lQoRbNQOkUh4facIqoabZTY-Cv3JFY2kBcKRKjbPqQRuaQPksKOXnAmKpYoozut2TUhGI96QAAKDXL6O6iaKL_0F-kMUoS13MC5kG0lcB9qDf3ehEHJG61pSR4z1unjqUlVeQyVPI0kPjm2_AKkB2OY1AOhqI3AtEqlT1-aWhES40; NID=512=iowlySLtYUsDqUD5_VkUFbpdcmhlIWF96GHwKrn7IOh1GCXkpPxfH_bDn2TiG0P-tg3d1TLMewkWGWW3gdAXtTuOFTb7cRTtejc0tjsrMbOSoYjyAIIVspj_MwwGM0uCo17ehcMSjCkNcRLGtelkspplICk5xXYR22_uSFBgI5RWU9Gi2j86C41-kSMODaSpe5iZad68ARXbMhFsrjn35WJLCs9Pq2cm1RuoTfApr_V6HZXjSEI7WTI04COL3X8gV_Ucqv6jYupb810x86uuovoYKFvi2tgNFU29eg; _gid=GA1.3.1111626144.1709276391; OTZ=7449540_52_52__52_; _ga=GA1.3.344521759.1709276378; __Secure-1PSIDTS=sidts-CjEBYfD7Z3lo07eMvOXx8MTlMxvbOLP_Vk4XqQiT7ygMOb6CKp5dRDJqonjclJdqeZKhEAA; __Secure-3PSIDTS=sidts-CjEBYfD7Z3lo07eMvOXx8MTlMxvbOLP_Vk4XqQiT7ygMOb6CKp5dRDJqonjclJdqeZKhEAA; _gat_gtag_UA_4401283=1; _ga_VWZPXDNJJB=GS1.1.1709276378.1.1.1709276930.0.0.0; SIDCC=AKEyXzXT4Njgn3cUgFLzEIYZDKJ6F4TWeEYcBHBDt65FOl-c_c37Hr2x-DEvH5ApjsajosGZJA; __Secure-1PSIDCC=AKEyXzWyQGUNbo6g-igJtO9PsUwHwGj05w79Ygj08Fn5q0IuMc3a47Y5qEEWEqlQOiFaX7ZrSw; __Secure-3PSIDCC=AKEyXzWkg9mBhhjMIvEeVpwviIrE82aTxfrX_NYn8YvFp1HrE5jr7MIyBXEszQGfaAgU2e5uOjY',
    'referer': 'https://trends.google.com/trends/explore?date=now%201-d&geo=NG&gprop=youtube&q=Cristiano%20Ronaldo&hl=en',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"122.0.6261.94"',
    'sec-ch-ua-full-version-list': '"Chromium";v="122.0.6261.94", "Not(A:Brand";v="24.0.0.0", "Google Chrome";v="122.0.6261.94"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'x-client-data': 'CKu1yQEIirbJAQiktskBCKmdygEIgIfLAQiUocsBCIWgzQEI4O7NAQjN980BCID9zQEY9MnNARid+M0BGMn4zQE=',
}


class TrendReq(UTrendReq):
    def _get_data(self, url, method=GET_METHOD, trim_chars=0, **kwargs):

        return super()._get_data(url, method=GET_METHOD, trim_chars=trim_chars, headers=headers, **kwargs)

trial = TrendReq()
url = 'https://trends.google.com/trends/explore?date=now%201-d&geo=NG&gprop=youtube&q=ronaldo&hl=en'
trial._get_data(url)