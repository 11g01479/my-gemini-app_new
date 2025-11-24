import streamlit as st
import google.generativeai as genai

# タイトル
st.title("私のGeminiアプリ 🤖")

# サイドバーに説明を入れる
st.sidebar.header("設定")
st.sidebar.write("これはGemini APIを使ったサンプルアプリです。")

# APIキーの設定（StreamlitのSecretsから読み込む安全な方法）
# まだ設定していない場合のエラー回避
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("APIキーが設定されていません。StreamlitのSecrets設定を確認してください。")
    st.stop()

# モデルの準備
model = genai.GenerativeModel('gemini-1.5-flash')

# ユーザーの入力エリア
user_input = st.text_input("Geminiに聞きたいことを入力してください", placeholder="例: Pythonの勉強方法を教えて")

# ボタンが押されたら実行
if st.button("送信"):
    if user_input:
        with st.spinner("考え中..."):
            try:
                # AIに回答を生成させる
                response = model.generate_content(user_input)
                st.success("完了！")
                st.write(response.text)
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")
    else:
        st.warning("文字を入力してください。")
