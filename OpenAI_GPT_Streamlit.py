import streamlit as st
import openai
from datetime import datetime
from streamlit.components.v1 import html

st.set_page_config(page_title="GPT Response Generator")

html_temp = """
                <div style="background-color:{};padding:1px">
                
                </div>
                """
with st.sidebar:
    st.markdown("""
    ## About 
    GPT Response Generator is an easy-to-use tool that quickly generates meaningful responses to any given topic. 
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    
    st.markdown("""
    ## How does it work?
    Simply enter the topic of interest into the text field and the GPT algorithm will use its vast knowledge of language to generate relevant responses.
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    
    st.markdown("""
    ## Options 
    """)
    model = st.selectbox('Model:', ('gpt-4', 'gpt-3.5-turbo'))
    temperature = st.slider('Temperature:', min_value=0.0, max_value=2.0, value=1.0, step=0.1)
    top_p = st.slider('Top P:', min_value=0.0, max_value=1.0, value=1.0, step=0.1)
    max_tokens = st.slider('Max Tokens:', min_value=100, max_value=4096, value=200, step=50)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    
    st.markdown("""
    Created to Raymond Ng, Forked by KC
    """,
    unsafe_allow_html=True,
    )


input_text = None
apikey = None

st.markdown("""
# GPT Response Generator
""")

apikey = st.text_input("Your API Key", disabled=False, type="password", placeholder="API Key?")
input_text = st.text_area("Topic of interest (press Ctrl-Enter once you have completed your inquiry)", disabled=False, placeholder="What topic you would like to ask?")

if input_text:
    messages = [
      {"role": "user", "content": str(input_text)}
    ] 
    if messages:
        if st.button('Submit'):
            openai.api_key = apikey
            response = openai.ChatCompletion.create(model=model, messages=messages, temperature=temperature, max_tokens=max_tokens, top_p=top_p)
            output = response['choices'][0]['message']['content']
            today = datetime.today().strftime('%Y-%m-%d')
            topic = input_text+"\n@Date: "+str(today)+"\n"+output
        
            st.info(output)
            filename = "Response_"+str(today)+".txt"
            btn = st.download_button(
                label="Download Text",
                data=topic,
                file_name=filename
            )

#####################################################
# Parameters for the Completion
#####################################################
# engine: text-davinci-003 (default)
#         text-davinci-002
#         text-davinci-001
#         text-curie-001
#         text-babbage-001
#         text-ada-001
# 
# temperature: 0 to 2 (default to 1)
# max_tokens: 100 to 4096 (default to 2048)
# top_p: 0 to 1 (default to 0.5)
# frequency_penalty: -2.0 to 2.0 (default to 0.0)
# presence_penalty: -2.0 to 2.0 (default to 0.0)
# stop: (default to "###")





