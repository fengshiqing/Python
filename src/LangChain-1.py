import os
import sys

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

# 第一步：和 大模型对话

# agent = create_agent(
#     model="open:gpt-4o",
#     tools=[search_tool, weather_tool],
#     system_prompt="你是一个乐于助人的研究助手"
# )

llm = ChatOpenAI(
    model="deepseek-v4-flash",
    base_url="https://api.deepseek.com/",
    api_key=os.environ.get('deepseek_api_key'),
    temperature=0)

response = llm.invoke("请告诉我美国有几个州")
print(response)
