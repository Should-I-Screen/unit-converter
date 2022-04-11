import streamlit as st

query_params = st.experimental_get_query_params()
language = "en"

language_list = ["en", "zh-TW", "zh-CN"]

if "lan" in query_params and query_params["lan"][0] in language_list:
    language =  query_params["lan"][0]




ui_language_dict = {
    "en": {
        "title": 'Height and Weight - Metric to English System Unit Converter',
        # height
        "height_label": "Height",
        "height_prompt": "Please enter your height (cm)",
        "height_placeholder": "Enter height and press Enter to convert",
        "height_result_original": "Height (Metric system):",
        "height_result_original_unit":"centimeters (cm)",
        "height_result_converted": 'Height (English system):',
        "height_result_converted_ft": "feet (ft)",
        "height_result_converted_in": "inches (in)",
        # weight
        "weight_label": "Weight",
        "weight_prompt": "Please enter your weight (kg)",
        "weight_placeholder": "Enter weight and press Enter to convert",
        "weight_result_original": "Weight (Metric system):",
        "weight_result_original_unit":"kilograms (kg)",
        "weight_result_converted": 'Weight (English system):',
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
        "weight_result_converted": 'Your weight (English system):',
        "weight_result_converted_unit": "pounds (lbs)"
    },
    "zh-TW": {
        "title": '身高體重公制轉英制單位換算',
        # height
        "height_label": "身高",
        "height_prompt": "請輸入你的身高 (公分)",
        "height_placeholder": "輸入身高並按 Enter 進行轉換",
        "height_result_original": "身高 (公制):",
        "height_result_original_unit":"公分 (cm)",
        "height_result_converted": '身高 (英制)',
        "height_result_converted_ft": "英尺 (ft or feet)",
        "height_result_converted_in": "英吋 (in or inches)",
        # weight
        "weight_label": "體重",
        "weight_prompt": "請輸入你的體重 (公斤)",
        "weight_placeholder": "輸入體重並按 Enter 進行轉換",
        "weight_result_original": "體重 (公制):",
        "weight_result_original_unit":"公斤 (kg)",
        "weight_result_converted": '體重 (英制)',
        "weight_result_converted_unit": "磅 (pounds or lbs)"
    },
    "zh-CN": {
        "title": '身高体重公制转英制单位换算',
        # height
        "height_label": "身高",
        "height_prompt": "请输入你的身高 (公分)",
        "height_placeholder": "输入身高并按 Enter 进行转换",
        "height_result_original": "身高 (公制):",
        "height_result_original_unit":"公分",
        "height_result_converted": '身高 (英制)',
        "height_result_converted_ft": "英尺 (ft or feet)",
        "height_result_converted_in": "英吋 (in or inches)",
        # weight
        "weight_label": "体重",
        "weight_prompt": "请输入你的体重 (公斤)",
        "weight_placeholder": "输入体重并按 Enter 进行转换",
        "weight_result_original": "体重 (公制):",
        "weight_result_original_unit":"公斤 (kg)",
        "weight_result_converted": '体重 (英制)',
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

    st.subheader("{}".format(ui_language_dict[language]["height_prompt"]))

    height_cm = st.number_input("", min_value=0, max_value=None, value=160, step=1, format="%d", help=ui_language_dict[language]["height_placeholder"], on_change=None, args=None, kwargs=None, disabled=False)
    #height_cm =  int(st.text_input(ui_language_dict[language]["height_prompt"], value='160', placeholder=ui_language_dict[language]["height_placeholder"]))


    st.subheader("{} {} {}".format(ui_language_dict[language]["height_result_original"], height_cm, ui_language_dict[language]["height_result_original_unit"]))

    #st.write(ui_language_dict[language]["height_result_original"], height_cm, ui_language_dict[language]["height_result_original_unit"])

    height_ft = height_cm //30.48
    height_in = height_cm//2.54 - height_ft * 12

    #st.write(ui_language_dict[language]["height_result_converted"], height_ft, ui_language_dict[language]["height_result_converted_ft"], height_in, ui_language_dict[language]["height_result_converted_in"])

    st.subheader(ui_language_dict[language]["height_result_converted"])
    #st.write(ui_language_dict[language]["height_result_converted"])

    st.metric(label="", value="{:.0f} {}".format(height_ft, ui_language_dict[language]["height_result_converted_ft"]))
    
    st.metric(label="", value="{:.0f} {}".format(height_in, ui_language_dict[language]["height_result_converted_in"]))

with col2:
    st.header(ui_language_dict[language]["weight_label"])

    st.subheader("{}".format(ui_language_dict[language]["weight_prompt"]))

    weight_kg = st.number_input("", min_value=0.0, max_value=None, value=70.0, step=0.5, format="%f", help=ui_language_dict[language]["weight_placeholder"], on_change=None, args=None, kwargs=None, disabled=False)

    #weight_kg =  float(st.text_input(ui_language_dict[language]["weight_prompt"], '70', placeholder=ui_language_dict[language]["weight_placeholder"]))

    st.subheader("{} {} {}".format(ui_language_dict[language]["weight_result_original"], weight_kg, ui_language_dict[language]["weight_result_original_unit"]))
    #st.write(ui_language_dict[language]["weight_result_original"], weight_kg, ui_language_dict[language]["weight_result_original_unit"])


    weight_lbs = weight_kg * 2.20462


    st.subheader(ui_language_dict[language]["weight_result_converted"])
    #st.write(ui_language_dict[language]["weight_result_converted"])

    #st.write(ui_language_dict[language]["weight_result_converted"], weight_lbs, ui_language_dict[language]["weight_result_converted_unit"])

    st.metric(label="", value="{:.2f}".format(weight_lbs))

    st.metric(label="", value="{}".format(ui_language_dict[language]["weight_result_converted_unit"]))

    #st.write(ui_language_dict[language]["weight_result_converted_unit"])

# st.write(language)




