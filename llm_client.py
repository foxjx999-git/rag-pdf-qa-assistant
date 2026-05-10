import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("没有找到 OPENAI_API_KEY，请检查 .env 文件是否配置正确。")


client = OpenAI(api_key=api_key)

def ask_llm(prompt):
    try:
        response = client.responses.create(
            model="gpt-5.4",          
            input=prompt,
            temperature=0
        )

        return response.output_text
    except Exception as e:
        raise RuntimeError(f"AI 调用失败：{e}")

