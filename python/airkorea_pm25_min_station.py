import requests
from pprint import pprint

URL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
API_KEY = ""

params = {
    "serviceKey": API_KEY,
    "returnType": "json",
    "sidoName": "전국",
    "numOfRows": 1000,   # 전국 데이터 대비 넉넉히
    "pageNo": 1,
    "ver": "1.3"
}

try:
    response = requests.get(URL, params=params, timeout=5)
    response.raise_for_status()
    data = response.json()

    items = data.get("response", {}).get("body", {}).get("items", [])
    print(f"전체 측정소 개수: {len(items)}")

    def find_min_pm25(items, sido_name=None):
        filtered = [
            item for item in items
            if item.get("pm25Value") not in (None, "-", "")
            and (sido_name is None or item["sidoName"] == sido_name)
        ]

        if not filtered:
            return None

        return min(filtered, key=lambda x: float(x["pm25Value"]))
    
    def print_station(item):
        if not item:
            print("❌ 해당 지역 데이터 없음")
            return

        print("📍 시도:", item["sidoName"])
        print("📡 측정소:", item["stationName"])
        print("🌫 PM2.5:", item["pm25Value"])
        print("⏰ 시각:", item["dataTime"])

    
    print_station(find_min_pm25(items, "서울"))
    print_station(find_min_pm25(items, "제주"))


except requests.exceptions.Timeout:
    print("⏱ TIMEOUT")

except requests.exceptions.RequestException as e:
    print("❌ REQUEST ERROR:", e)

except ValueError:
    print("❌ JSON PARSE ERROR")


