import streamlit as st

query_params = st.experimental_get_query_params()
language = "en"

language_list = ["en", "zh-TW", "zh-CN"]

if "lan" in query_params and query_params["lan"][0] in language_list:
    language =  query_params["lan"][0]




ui_language_dict = {
    "en": {
        "title": 'Unit Converter',
        # height
        "height_label": "Height",
        "height_prompt": "Please enter your height (cm)",
        "height_placeholder": "Enter height and press Enter to convert",
        "height_result_original": "Your height (Metric system):",
        "height_result_original_unit":"centimeters (cm)",
        "height_result_converted": 'Your height (English system):',
        "height_result_converted_ft": "feet (ft)",
        "height_result_converted_in": "inches (in)",
        # weight
        "weight_label": "Weight",
        "weight_prompt": "Please enter your weight (kg)",
        "weight_placeholder": "Enter weight and press Enter to convert",
        "weight_result_original": "Your weight (Metric system):",
        "weight_result_original_unit":"kilograms (kg)",
        "weight_result_converted": 'Your weight (English system)',
        "weight_result_converted_unit": "pounds (lbs)"
    },
    "es": {
        "title": 'Unit Converter',
        # height
        "height_label": "Height",
        "height_prompt": "Please enter your height (cm)",
        "height_placeholder": "Enter height and press Enter to convert",
        "height_result_original": "Your height (Metric system):",
        "height_result_original_unit":"centimeters (cm)",
        "height_result_converted": 'Your height (English system):',
        "height_result_converted_ft": "feet (ft)",
        "height_result_converted_in": "inches (in)",
        # weight
        "weight_label": "Weight",
        "weight_prompt": "Please enter your weight (kg)",
        "weight_placeholder": "Enter weight and press Enter to convert",
        "weight_result_original": "Your weight (Metric system):",
        "weight_result_original_unit":"kilograms (kg)",
        "weight_result_converted": 'Your weight (English system)',
        "weight_result_converted_unit": "pounds (lbs)"
    },
    "zh-TW": {
        "title": '單位換算',
        # height
        "height_label": "身高",
        "height_prompt": "請輸入你的身高 (公分)",
        "height_placeholder": "輸入身高並按 Enter 進行轉換",
        "height_result_original": "你的身高 (公制):",
        "height_result_original_unit":"公分 (cm)",
        "height_result_converted": '你的身高 (英制)',
        "height_result_converted_ft": "英尺 (ft or feet)",
        "height_result_converted_in": "英吋 (in or inches)",
        # weight
        "weight_label": "體重",
        "weight_prompt": "請輸入你的體重 (公斤)",
        "weight_placeholder": "輸入體重並按 Enter 進行轉換",
        "weight_result_original": "你的體重 (公制):",
        "weight_result_original_unit":"公斤 (kg)",
        "weight_result_converted": '你的體重 (英制)',
        "weight_result_converted_unit": "磅 (pounds or lbs)"
    },
    "zh-CN": {
        "title": '单位换算',
        # height
        "height_label": "身高",
        "height_prompt": "请输入你的身高 (公分)",
        "height_placeholder": "输入身高并按 Enter 进行转换",
        "height_result_original": "你的身高 (公制):",
        "height_result_original_unit":"公分",
        "height_result_converted": '你的身高 (英制)',
        "height_result_converted_ft": "英尺 (ft or feet)",
        "height_result_converted_in": "英吋 (in or inches)",
        # weight
        "weight_label": "体重",
        "weight_prompt": "请输入你的体重 (公斤)",
        "weight_placeholder": "输入体重并按 Enter 进行转换",
        "weight_result_original": "你的体重 (公制):",
        "weight_result_original_unit":"公斤 (kg)",
        "weight_result_converted": '你的体重 (英制)',
        "weight_result_converted_unit": "磅 (pounds or lbs)"
    }
}

st.set_page_config(
     page_title=ui_language_dict[language]["title"]
 )


st.title(ui_language_dict[language]["title"])


col1, col2 = st.columns(2)

with col1:
    st.header(ui_language_dict[language]["height_label"])
    height_cm =  int(st.text_input(ui_language_dict[language]["height_prompt"], value='160', placeholder=ui_language_dict[language]["height_placeholder"]))
    st.write(ui_language_dict[language]["height_result_original"], height_cm, ui_language_dict[language]["height_result_original_unit"])
    height_ft = height_cm //30.48
    height_in = height_cm//2.54 - height_ft * 12

    st.write(ui_language_dict[language]["height_result_converted"], height_ft, ui_language_dict[language]["height_result_converted_ft"], height_in, ui_language_dict[language]["height_result_converted_in"])

    st.metric(label=ui_language_dict[language]["height_result_converted"], value=4)

with col2:
    st.header(ui_language_dict[language]["weight_label"])
    weight_kg =  float(st.text_input(ui_language_dict[language]["weight_prompt"], '70', placeholder=ui_language_dict[language]["weight_placeholder"]))
    st.write(ui_language_dict[language]["weight_result_original"], weight_kg, ui_language_dict[language]["weight_result_original_unit"])
    weight_lbs = weight_kg * 2.20462

    st.write(ui_language_dict[language]["weight_result_converted"], weight_lbs, ui_language_dict[language]["weight_result_converted_unit"])

# st.write(language)




