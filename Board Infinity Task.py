import streamlit as st
import spacy
import spacy.displacy as dsp
import wikipediaapi

# Title of the streamlit app
st.title("Text Preprocessing before named entity recognition")


# scrapping the wikkipedia for a given name or title
wiki = wikipediaapi.Wikipedia(language='en',
                            extract_format=wikipediaapi.ExtractFormat.WIKI)
input = st.text_input("Input Some Name or Any Title", "America")
input_text = wiki.page(input).text

# getting the entity of the all words from the scrapped data
nlp = spacy.load("en_core_web_sm")
res = nlp(input_text)

html = dsp.render(res, style='ent', page=True)
st.markdown(html, unsafe_allow_html = True)
st.write("\n\n")
st.write("Invalid name, please try again with a valid Name and Title")
st.write("\n\n")
