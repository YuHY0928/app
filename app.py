import streamlit as st
from PIL import Image
from clf import predict

st.set_option('deprecation.showfileUploaderEncoding', False)

st.title("图像识别")
st.write("")

file_up = st.file_uploader("上传一张图像", type="jpg")

if file_up is not None:
    image = Image.open(file_up)
    st.image(image, caption='上传的图像', use_column_width=True)
    st.write("")
    st.write("正在加载中...")
    labels = predict(file_up)

    # print out the top 5 prediction labels with scores
    for i in labels:
        st.write("识别结果：", i[0], ",   相似度: ", i[1])
