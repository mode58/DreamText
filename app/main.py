import google.generativeai as genai
import os
import sys
from dotenv import load_dotenv
from datetime import datetime


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
interpretation = response.text #解釈結果のテキストを取得

today = datetime.now() #今日の日付取得
format_today = today.strftime("%Y年%m月%d日 %H:%M")  #日付だけにする

try:
    with open('Dream_log.txt', 'a', encoding='utf-8') as f:
        f.write(f"{format_today}\n--- 夢の記録 ---\n")
        f.write(f"夢の内容: {dreamcontent}\n")
        f.write(f"解釈結果:\n{interpretation}\n")
        print("\n--- 夢をファイルに記録しました ---")
except Exception as e:
    print(f"ファイルに書き込めませんでした。{e}")
    sys.exit()

print(interpretation)