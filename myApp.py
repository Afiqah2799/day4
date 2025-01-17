import streamlit as st

st.write('This is write')
st.header('This is header')
st.subheader('This is subheader')
st.caption('This is caption')


st.markdown("*Streamlit* is **really** ***cool***.")

st.markdown(''' :red[Streamlit] :orange[is] :green[fun] ''')

st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")


st.success("good")
st.warning("bad")
st.info("info")
st.error("Error!")

###Advanced font
st.write('**Advanced font**')
new_title = '<p style="font-family:sans-serif;\
    color:cyan; font-size: 35px;">This is advanced font \
    manipulation!</p>'

st.markdown(new_title, unsafe_allow_html=True)
st.write('')

###Selection box
st.write('**Selection box**')
select1= st.selectbox("Kuala Lumpur is located at",
['Malaysia', 'Thailand', 'UK'])
st.write('You have selected:' , select1)
st.write('')

select2 = st.multiselect("Select 2 states",
['Selangor','Johor','Kedah'])
st.write('You have selected:' , select2)
st.write('')

###Buttons
st.write('**Buttons**')
b1 = st.button("Click Here to Proceed")
if b1:
    st.write('Days:')
    st.slider("Select the length of stay", 1,10, value=3)
st.write('')

###Input Box
number = st.number_input("Insert a number", \
                         value=None, placeholder="Type a number...")

st.write("The current number is ", f'{number:.4f}')
st.write('')

###Insert graphics
st.write('**Insert Graphics**')
from PIL import Image
im = Image.open('shrdc_logo.png')
st.image(im, width=250 )
st.write('')

###Dataframe
st.write('**Dataframe**')
import pandas as pd
df = pd.read_excel('sampleData.xlsx')
st.dataframe(df.tail(3))
 ###Bar Chart
st.bar_chart(df, x="Location", y="Income")
st.line_chart(df, x="Household", y="Income")
st.scatter_chart(df, x="Household", y="Income", color='Month Fees')

#Tabpage
st.write('**Multi-tabpage**')
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

#Multi-column
st.write('**Multi-columns**')
col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

st.header("")

st.subheader("How to center item")
colu1, colu2, colu3 = st.columns(3)

with colu1:
    st.write('')
with colu2:
    from PIL import Image
    im = Image.open('shrdc_logo.png')
    st.image(im, width=250 )
with colu3:
    st.header("")