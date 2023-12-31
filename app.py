import streamlit as st
from PIL import Image
import cloudpickle


# load model using cloudpickle
with open("ai-machine-human-tfidf-rf.pkl", 'rb') as file:
    model = cloudpickle.load(file)


# title
st.markdown("# AI or Human?")


# image
# we cache the image so we don't have to reload it every time we make a prediction
@st.cache_data
def get_image():
    image = Image.open('images/human-vs-ai_orig.png')
    return image


img = get_image()
st.image(img, width=500)


# clears text from text area
def clear_text():
    st.session_state["text"] = ""


# when submit button is clicked, do this
def submit():
    # get what is in the text area with key=text
    i = st.session_state["text"]
    print("submit:", i)
    # send the text in the text area to the model for prediction
    inference = model.predict(i)
    # see the inference returned in the console
    print("inference:", inference)
    # start output section (after prediction)
    st.markdown("**:blue[Text entered:]**")
    # output original text
    st.write(i)
    # output 1 = AI
    # output 0 = Human
    # if inference is 1
    if inference[0] == 1:
        st.markdown("**:blue[This was written by AI!]**")
    else:
        st.markdown("**:blue[A human wrote this.]**")
    # clear text area
    clear_text()


# create text area and capture the text inputted there in a variable called st.session_state["text"]
st.text_area(label="Enter your text to determine if it was generated by AI or Human", key="text")

# create columns to display buttons side by side
col1, col2 = st.columns([.3, 1])
# submit button - calls submit() method
with col1:
    st.button(label="Submit Text", on_click=submit)
# clear text button - clears inference output and text area
with col2:
    st.button(label="Clear Text", on_click=clear_text)

