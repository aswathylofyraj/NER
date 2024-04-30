import streamlit as st
import spacy
from spacy import displacy
from newspaper import Article

st.title("NER DEMO")
nlp = spacy.load("en_core_web_sm")

text_input = st.text_area("Enter a paragraph")
url_input = st.text_input("OR Enter a URL")

if st.button("Analyze"):
    if text_input:
        doc = nlp(text_input)
        ent_html = displacy.render(doc, style="ent", jupyter=False)
        st.markdown(ent_html, unsafe_allow_html=True)
    elif url_input:
        article = Article(url_input)
        article.download()
        article.parse()
        doc = nlp(article.text)
        ent_html = displacy.render(doc, style="ent", jupyter=False)
        st.markdown(ent_html, unsafe_allow_html=True)
    else:
        st.warning("Please enter a paragraph or a URL.")
        
