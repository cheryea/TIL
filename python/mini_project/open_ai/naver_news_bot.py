import os
import requests
import json
from dotenv import load_dotenv
from pprint import pprint

from openai import OpenAI


load_dotenv()

NAVER_CLIENT_ID = os.getenv('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = os.getenv('NAVER_CLIENT_SECRET')
TMDB_API_KEY = os.getenv('TMDB_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

model = 'gpt-4o-mini'

# 네이버 뉴스 API 함수
def get_naver_news(query, display=5, sort="date"):
    url = "https://openapi.naver.com/v1/search/news.json"

    params = {
        "query": query,
        "display": display,
        "sort": sort
    }

    headers = {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET
    }

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    data = response.json()
    return data.get("items", [])
    
    

# # 사용 예시
# if __name__ == "__main__":
#     news_list = get_naver_news("Python")
#     for news in news_list:
#         print(news["title"], "-", news["link"])


tools = [
    {
        "type": "function",
        "name": "get_naver_news",
        "description": "네이버 뉴스 검색 API를 사용해 뉴스 목록을 가져옵니다.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "검색어 (예: 미국 금리, AI 반도체, 테슬라 등)"
                },
                "display": {
                    "type": "integer",
                    "description": "뉴스 개수 (기본 5)"
                },
                "sort": {
                    "type": "string",
                    "description": "정렬 방식: sim(정확도순), date(최신순)"
                }
            },
            "required": ["query"]
        }
    }
]


# 사용자 질문
# → LLM이 질문 이해
# → "이런 함수 써야겠다" 판단
# → 네이버 뉴스 API 호출
# → 결과를 다시 LLM에게 전달
# → LLM이 요약/응답


def run_conversation(user_prompt):
    input_list = [{"role": "user", "content": user_prompt}]

    # 1차 LLM 호출 (함수 호출 판단)
    response = client.responses.create(
        model=model,
        input=input_list,
        tools=tools
    )

    input_list += response.output

    # 함수 호출 실행
    for item in response.output:
        if item.type == "function_call":
            if item.name == "get_naver_news":
                args = json.loads(item.arguments)
                result = get_naver_news(**args)

                input_list.append({
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": json.dumps({"result": result})
                })

    # 2차 LLM 호출 (결과 요약)
    response = client.responses.create(
        model=model,
        instructions="뉴스 제목과 핵심 내용을 간단히 정리해서 한국어로 답변하세요.",
        input=input_list,
        tools=tools
    )

    return response.output_text

    

# 실행 예시
print(run_conversation("윤석열 관련 뉴스 뽑아줘"))
