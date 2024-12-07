import streamlit as st
import av

st.title("ずんだもんのショーフロク")
st.write("まだまだ開発中🚫")

# 動画ファイルのパス
video_file = "./image/rirakkuma_ramen_1.mp4"

# 動画を再生する
st.video(video_file)

# または、動画をストリーミングする
# with open(video_file, 'rb') as f:
#   video_bytes = f.read()
# st.video(video_bytes)

# または、av ライブラリを使用して動画をストリーミングする
# with open(video_file, "rb") as f:
#   container = av.open(f)
#   for frame in container.decode(video=0):
#     st.image(frame.to_image())