
# Please install OpenAI SDK first: `pip3 install openai`
import os
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool

# 第二步：添加 agent

model = ChatOpenAI(
    model="deepseek-v4-pro", # deepseek-v4-flash 便宜， deepseek-v4-pro 贵
    base_url="https://api.deepseek.com/",
    api_key=os.environ.get('deepseek_api_key'),
    # disable_thinking=True,  # 禁用思考模式
    temperature=0
)

# @tool
# def search(query: str) -> str:
#     """根据输入的查询，返回搜索结果"""
#     return f"搜索结果：{query}"


# @tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="你是一个乐于助人的生活助手"
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result)
