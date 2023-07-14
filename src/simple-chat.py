import openai
import os
from dotenv import load_dotenv


def ask_gpt(prompt):
    '''与AI进行对话的聊天历史'''

    load_dotenv()
    openai.api_key = os.getenv('OPENAI_API_KEY')
    chat_history = [
        {'role': 'system', 'content': 'You are a helpful assistant.'},
    ]
    chat_history.append({'role': 'user', 'content': prompt})

    # 设置参数
    parameters = {
        'model': 'gpt-3.5-turbo',
        'messages': chat_history,
        'max_tokens': 100
    }
    # 调用ChatCompletion.create方法
    response = openai.ChatCompletion.create(**parameters)
    # 提取AI生成的回复
    answer = response.choices[0].message['content']
    return answer


print("你好！欢迎来到ChatGPT。输入'退出'以结束对话。")

while True:
    user_input = input('你： ')
    if user_input.lower() == '退出':
        break
    response = ask_gpt(user_input)
    print(response)
