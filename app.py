import streamlit as st
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# .envファイルの読み込み
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# OpenAIの設定
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7, openai_api_key=api_key)

# 専門家のプロンプト
expert_prompts = {
    "心理カウンセラー": "あなたは信頼できる心理カウンセラーです。相手の気持ちを否定せず、やさしく共感しながら、前向きになれるようなアドバイスをしてください。",
    "恋愛マスター": "あなたは恋愛マスターです。相手の悩みに対して的確かつ情熱的なアドバイスを与え、背中を押すような前向きな回答を心がけてください。"
}

# Streamlit UI
st.title("専門家に相談できるLLMアプリ")
st.write("お悩みを入力し、相談したい専門家を選んでください。")

# 入力フォーム
expert = st.radio("相談相手を選んでください", list(expert_prompts.keys()))
user_input = st.text_input("あなたのお悩みを入力してください")

# 応答処理関数
def get_response(expert, text):
    system_msg = SystemMessage(content=expert_prompts[expert])
    user_msg = HumanMessage(content=text)
    response = llm([system_msg, user_msg])
    return response.content

# 回答を表示
if user_input:
    answer = get_response(expert, user_input)
    st.markdown("### 回答")
    st.write(answer)