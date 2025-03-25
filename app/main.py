import google.generativeai as genai
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# APIキーが読み込まれているか確認 (デバッグ用)
print(os.environ.get("GOOGLE_API_KEY"))

# APIキーを設定
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# 利用可能なモデルを確認 (この部分は確認が終わったらコメントアウトしてOK)
# for m in genai.list_models():
#     print(m)

# モデルを選択 (利用可能なモデルの中から選ぶ)
model = genai.GenerativeModel(model_name='gemini-1.5-pro-002')

# 簡単なテキスト生成を試す
prompt = "日本の首都はどこですか？"
response = model.generate_content(prompt)

print(response.text)