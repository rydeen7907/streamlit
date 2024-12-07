import streamlit as st
from PIL import Image

st.title("ずんだもんのショーフロク")
st.write("とりまテスト段階😊")

image = Image.open("./image/kitakata.jpg")

st.subheader("プロフィール")
st.text("1971年 山形県真室川町出身 高卒プロンプトエンジニア")
st.text("＜ 取得資格 ＞")
st.text("Google AIエッセンシャルズ")
st.text ("Google データアナリティクスプロフェッショナル認定")
st.text("日本化粧品検定協会 化粧品検定3級")
st.text("8t限定中型自動車運転免許")
st.text("無線従事者技士免許(アマチュア無線3級) [ JQI3AA ]")