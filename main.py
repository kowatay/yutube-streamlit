import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('ぶれぐすばーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!'

st.write('2カラム表示')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button :
    right_column.write('ここは右カラム')


st.write('EXPANDER')

expander1 = st.expander('問い合わせ１')
expander1.write('問い合わせ１の回答')
expander2 = st.expander('問い合わせ２')
expander2.write('問い合わせ２の回答')
expander3 = st.expander('問い合わせ３')
expander3.write('問い合わせ３の回答')

st.write('SIDEBAR')

text = st.sidebar.text_input('あなたの趣味を教えてください。',key = 'x1')
'あなたの趣味：', text

condition = st.sidebar.slider('あなたの今の調子は？', 0 , 100 , 50 )
'コンディション：', condition

st.write('TEXT BOX')

text2 = st.text_input('あなたの趣味を教えてください。',key = 'x2')
'あなたの趣味：', text2

condition2 = st.slider('あなたの今の調子は？', 0 , 100 , 50 ,key = 'y1')
'コンディション：', condition2

st.write(' SELECT BOX')
option = st.selectbox(
    'あなたの好きな数字を教えてください。',
    list(range(1,11))
)
'あなたの好きな数字は、', option , 'です。'

st.write('Display Image')

if st.checkbox('Show Image' ) :
    img = Image.open('栂池2.jpg')
    st.image(img,caption='Kohei Imanishi', use_column_width=True)

st.write('DataFram')

df = pd.DataFrame({
    '1劣目':[1, 2, 3, 4],
    '2劣目':[10, 20, 30, 40]
})

st.write( df )
st.dataframe(df.style.highlight_max(axis=0),width=400 )

df1 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a','b','c']
)

st.line_chart(df1)
st.area_chart(df1)
st.bar_chart(df1)

df2 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70] ,
    columns=['lat','lon']
)
st.map(df2)