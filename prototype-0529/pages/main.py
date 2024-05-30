from sysmov import path
path.create_path()

import streamlit as st
from create import image as img_module
from create import text
from create import templates as temp
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# from langchain.llms import OpenAI
from langchain_community.llms import OpenAI
import io
import time
import requests
import os


# 로그인 상태 확인 및 초기화
if 'login_nickname' not in st.session_state:
    st.session_state['login_nickname'] = 'Unknown'

if 'login_successful' not in st.session_state:
    st.session_state['login_successful'] = False

login_nickname = st.session_state.login_nickname
login_successful = st.session_state.login_successful



# Template 
prompt_template_pexel = PromptTemplate.from_template(
"""
You are the AI that chooses number. 
Please print out the number that ["1", "2", "3", "4"]

text: {text}

If it's related to school, 1.
If it's related to nature 2.
If it's related to computers, 3.
If it's related to people, 4.

Print out one of the integers 1 to 4 that match the text above. Just print out the numbers, not say anything else.

"""
)
llm = OpenAI(temperature=0)

def template_num(input_text):
    result = llm(prompt_template_pexel.format(text=input_text))
    return result



def main():
    if login_successful:
        st.title('Infographic Generator :frame_with_picture:')
        st.write('Welcome! ' + login_nickname)
        st.text("<www.pexels.com> Background Photos provided by pexels")
        st.divider()

        if 'slides' not in st.session_state:
            st.session_state['slides'] = []

        if 'button_clicked' not in st.session_state:
            st.session_state.button_clicked = {}

        # Input form
        inputform()

        ## 하늘님
        # for i in range(len(st.session_state.slides)):
        #     if(st.session_state.slides[i]['query']):
        #         image = img_module.overlay_image(st.session_state.slides[i]['query'], st.session_state.slides[i]['text'])
        #         st.image(image, width=600)
        #         st.download_button(f"다운로드{i+1}", data=image, file_name=f"image{i+1}.jpg")


        # Display slides
        ## 형남님
        for i in range(len(st.session_state.slides)):
            slide = st.session_state.slides[i]
            if slide['query']:
                try:
                    # slide_image = img_module.overlay_image(slide['query'], slide['text'])
                    # overlay_image = temp.temp1()
                    
                    # 사용자가 템플릿을 선택할 수 있도록 선택지를 제공
                    
                    # template_option = st.selectbox(
                    #     f"슬라이드 {i+1} 템플릿 선택", 
                    #     options=['temp1', 'temp2', 'temp3', 'temp4'], 
                    #     key=f"template_option_{i}"
                    # )
                    
                    selected_template = template_num(slide['query'])
                    st.write(selected_template)

                    
                    # 선택된 템플릿에 따라 overlay_image를 생성
                    overlay_image = None
                    if '1' in selected_template :
                        overlay_image = temp.temp1()
                    elif '2' in selected_template :
                        overlay_image = temp.temp2()
                    elif '3' in selected_template :
                        overlay_image = temp.temp3()
                    elif '4' in selected_template :
                        overlay_image = temp.temp4()
                    
                    if overlay_image:  # None이 아닌 경우에만 이미지를 표시
                        image_byte_array = overlay_image.save("output.jpg")
                        st.image(image_byte_array)
                        #삭제버튼
                        delete_button = st.button(label="삭제", key=i)
                        if delete_button:
                            del st.session_state.slides[i]
                            st.rerun()
                        
                        #다운로드 버튼
                        image_byte_array = io.BytesIO()
                        overlay_image.image.save(image_byte_array, format='JPEG')
                        image_data = image_byte_array.getvalue()
                        st.download_button(label=f"다운로드 {i+1}", data=image_data, file_name=f"image_{i+1}.jpg")
                        # st.download_button(f"다운로드{i+1}", data=overlay_image, file_name=f"image{i+1}.jpg")
                except KeyError as e:
                    st.error(f"An error occurred: {str(e)}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                    
    else:
        st.error('You have to login first!')

def inputform():
    add_input = st.button("추가")
    if 'num_inputs' not in st.session_state:
        st.session_state.num_inputs = 0

    if add_input:
        st.session_state.num_inputs += 1

    with st.form("form"):
        for i in range(st.session_state.num_inputs):
            query = st.text_input(f"슬라이드 {i+1} 이미지", key=f"image_keyword_{i}")
            slide_text = st.text_input(f"슬라이드 {i+1} 문장", key=f"text_{i}")

            if i < len(st.session_state.slides):
                st.session_state.slides[i] = {'query': query, 'text': slide_text}
            else:
                st.session_state.slides.append({'query': query, 'text': slide_text})

        submit = st.form_submit_button("생성")
        if submit:
            with st.spinner('Wait for it...'):
                time.sleep(5)

if __name__ == "__main__":
    main()

def download(overlay_image, n):
    image_byte_array = io.BytesIO()
    overlay_image.image.save(image_byte_array, format='JPEG')
    image_data = image_byte_array.getvalue()
    st.download_button(label=f"다운로드 {n+1}", data=image_data, file_name=f"image_{n+1}.jpg")
