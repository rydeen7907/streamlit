import streamlit as st
from PIL import Image

st.title("ずんだもんのショーフロク")
st.write("とりまテスト段階😊")

st.subheader(" ＜ 自己紹介 ＞")
st.text("AIとPythonを使ったコードをYoutubeで公開しています。")
st.markdown("[Youtube：ずんだもんのショーフロク](https://www.youtube.com/@dalakkuma610)")


image = Image.open("./image/kitakata.jpg")
st.image(image)

st.subheader("プロフィール")
st.write("1971年 山形県真室川町出身 高卒プロンプトエンジニア")
st.text("＜ 取得資格 ＞")
st.write("Google AIエッセンシャルズ\n"
        "Google データアナリティクスプロフェッショナル認定\n"
        "日本化粧品検定協会 化粧品検定3級\n"
        "8t限定 中型自動車運転免許\n"
        "無線従事者技士(アマチュア無線3級) [ JQI3AA ]")
