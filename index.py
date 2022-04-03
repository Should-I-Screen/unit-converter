import streamlit as st

query_params = st.experimental_get_query_params()
language = "en"
if "lan" in query_params:
    language =  query_params["lan"][0]


ui_language_dict = {
    "en": {},
    "es": {},
    "zh-TW": {
        "title": '單位換算',
        # height
        "height_label": "身高",
        "height_prompt": "請輸入你的身高 (公分)",
        "height_placeholder": "輸入身高並按 Enter 進行轉換",
        "height_result_original": "你的身高 (公制):",
        "height_result_original_unit":"公分",
        "height_result_converted": '你的身高 (英制)',
        "height_result_converted_ft": "英尺",
        "height_result_converted_in": "英吋",
        # weight
        "weight_label": "體重",
        "weight_prompt": "請輸入你的體重 (公斤)",
        "weight_placeholder": "輸入體重並按 Enter 進行轉換",
        "weight_result_original": "你的體重 (公制):",
        "weight_result_original_unit":"公斤",
        "weight_result_converted": '你的體重 (英制)',
        "weight_result_converted_unit": "磅"

    },
    "zh-CN": {
        
    }
}

st.title(ui_language_dict[language]["title"])


col1, col2 = st.columns(2)

with col1:
    st.header(ui_language_dict[language]["height_label"])
    height_cm =  int(st.text_input(ui_language_dict[language]["height_prompt"], value='160', placeholder=ui_language_dict[language]["height_placeholder"]))
    st.write(ui_language_dict[language]["height_result_original"], height_cm, ui_language_dict[language]["height_result_original_unit"])
    height_ft = height_cm //30.48
    height_in = height_cm//2.54 - height_ft * 12

    st.write(ui_language_dict[language]["height_result_converted"], height_ft, ui_language_dict[language]["height_result_converted_ft"], height_in, ui_language_dict[language]["height_result_converted_in"])

with col2:
    st.header(ui_language_dict[language]["weight_label"])
    weight_kg =  float(st.text_input(ui_language_dict[language]["weight_prompt"], '70', placeholder=ui_language_dict[language]["weight_placeholder"]))
    st.write(ui_language_dict[language]["weight_result_original"], weight_kg, ui_language_dict[language]["weight_result_original_unit"])
    weight_lbs = weight_kg * 2.20462

    st.write(ui_language_dict[language]["weight_result_converted"], weight_lbs, ui_language_dict[language]["weight_result_converted_unit"])

# st.write(language)




