import streamlit as st
from PIL import Image

st.title("ずんだもんのショーフロク")
st.write("とりまテスト段階😊")

st.subheader(" ＜ コメント ＞")
st.text("AIとPythonを使ったコードをYoutubeで公開しています。")
st.markdown("[Youtube：ずんだもんのショーフロク](https://www.youtube.com/@dalakkuma610/)")
st.markdown("[GitHub](https://github.com/rydeen7907/)")
st.text("プライベート的なことは👉")
st.markdown("[instagram：rydeen7907](https://www.instagram.com/rydeen7907/)")
st.markdown("[X (旧twitter)：JQI3AA](https://x.com/jr4853/)")


# 画像を表示
image = Image.open("./image/kitakata.jpg")
st.image(image)

# サイドバーに画像を表示
# st.sidebar.image("path_to_your_image.jpg", caption="Sidebar image")

st.subheader("プロフィール")
st.write("1971年 山形県真室川町出身 高卒プロンプトエンジニア")
st.text("＜ 取得資格 ＞")
st.text("Google AIエッセンシャルズ\n"
        "Google データアナリティクスプロフェッショナル認定\n"
        "日本化粧品検定協会 化粧品検定3級\n"
        "8t限定 中型自動車運転免許\n"
        "無線従事者技士(アマチュア無線3級) [ JQI3AA ]")

# 動画を表示
st.write("リラックマ、ラーメン🍜を食べる…")
# 動画ファイルのパス
video_file = open("./image/rirakkuma_ramen_1.mp4", "rb")
# 動画を再生する
video_bytes = video_file.read()
st.video(video_bytes)
