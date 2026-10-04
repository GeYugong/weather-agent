import os

import requests
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)


def get_location(city):
    """把城市名称转换成经纬度"""

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "zh",
        "format": "json"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if not data.get("results"):
        raise ValueError(f"找不到城市：{city}")

    location = data["results"][0]

    return {
        "name": location["name"],
        "latitude": location["latitude"],
        "longitude": location["longitude"]
    }


def get_weather(city):
    """查询指定城市未来天气"""
    

    location = get_location(city)

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "daily": [
            "weather_code",
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_probability_max"
        ],
        "timezone": "auto",
        "forecast_days": 3
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    return {
        "city": location["name"],
        "daily": data["daily"]
    }

def ask_llm(question):
    """向 DeepSeek 提问"""

    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {
                "role": "system",
                "content": "你是一个简洁、友好的中文助手。"
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    answer = ask_llm("你好，请用一句话介绍你自己。")
    print(answer)