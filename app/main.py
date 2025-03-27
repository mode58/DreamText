import google.generativeai as genai
import os
from dotenv import load_dotenv
import sys

# .envファイルから環境変数を読み込む
load_dotenv()

# APIキーを設定
api_key=os.environ.get("GOOGLE_API_KEY")
if not api_key:
    print("APIキーが見つかりません")
    sys.exit()


genai.configure(api_key = api_key)

# モデルを選択
model = genai.GenerativeModel(model_name='gemini-1.5-pro-002')

#dreamcontent = "地面を掘っている夢を見ました"
dreamcontent = input("見た夢の内容を教えてください: ")
Preface = "夢を分析して心理状態を測ってください"
prompt = Preface + dreamcontent

response = model.generate_content(prompt)

with open('Dream_log.txt', 'a', encoding='utf-8') as f:
    f.write(response.text) #書き込み

print(response.text)