import streamlit as st

st.title("🌌 Unit Converter App")

st.markdown(
    """
    <style>
    body{
        color:white;
    }
    .stApp{
        padding:30px;
        border-radius:15px;
        box-shadow:0px 10px 30px rgba(0,0,0,0.3)
    }
    h1{
        text-align:center;
        font-size:36px;
    }
    .stButton>button{
        background:linear-gradient(45deg, #0b5394, #351c75);
        font-size:18px;
        padding:10px 20px;
        transition:0.3s;
        color:white;
        
    }
    .stButton>button:hover{
        transform: scale(1.05);
        background:linear-gradient(45deg, #92fe9d, #00c9ff);
        color:black;
    }
    .footer{
        text-align:center;
        margin-top:30px;
        font-size:20px;
        color:white;
    }
    .footer1{
        text-align:center;
        margin-top:10px;
        font-size:20px;
        color:white;
    }
    </style>
    """,
    unsafe_allow_html=True)
st.markdown("### Convert Length, Weight, Time Instantly")

st.write("Welcome to the Unit Converter App. Enter the value and select the unit to convert it to another unit.")

category = st.selectbox("Select Category", ["Length", "Weight", "Time"])

def convert_units(category,value, unit):
    if category == "Length":
        if unit== "Kilometers to Centimeters":
            return value *100000
        elif unit == "Kilometers to Meters":
            return value *1000
        elif unit == "Kilometers to Feet":
            return value *3280.84
        elif unit == "Centimeters to Kilometers":
            return value /100000
        elif unit == "Centimeters to Meters":
            return value /100
        elif unit == "Centimeters to Feet":
            return value /30.48
        elif unit == "Meters to Kilometers":
            return value /1000
        elif unit == "Meters to Centimeters":
            return value *100
        elif unit == "Meters to Feet":
            return value *3.28084  
        elif unit == "Feet to Kilometers":
            return value /3280.84
        elif unit == "Feet to Centimeters":
            return value *30.48 
        elif unit == "Feet to Meters":
            return value /3.28084
    elif category == "Weight":
            if unit == "Kilograms to Pounds":
                return value *2.20462
            elif unit == "Kilograms to Grams":
                return value *1000
            elif unit == "Kilograms to Ounces":
                return value *35.274
            elif unit == "Pounds to Kilograms":
                return value /2.20462
            elif unit == "Pounds to Grams":
                return value /0.00220462
            elif unit == "Pounds to Ounces":
                return value *16
            elif unit == "Grams to Kilograms":
                return value /1000
            elif unit == "Grams to Pounds":
                return value *0.00220462
            elif unit == "Grams to Ounces":
                return value /28.3495
            elif unit == "Ounces to Kilograms":
                return value /35.274
            elif unit == "Ounces to Pounds":
                return value /16
            elif unit == "Ounces to Grams":
                return value *28.3495
            
    elif category == "Time":
            if unit == "Hours to Minutes":
                return value *60
            elif unit == "Hours to Seconds":
                return value * 3600
            elif unit == "Hours to Days":
                return value /24
            elif unit == "Minutes to Hours":
                return value / 60
            elif unit == "Minutes to seconds":
                return value *60
            elif unit == "Minutes to Days":
                return value /1440
            elif unit == "Seconds to Hours":
                return value / 3600
            elif unit == "Seconds to Days":
                return value /86400
            elif unit == "Seconds to Minutes":
                return value /60
            elif unit == "Days to Hours":
                return value *24
            elif unit == "Days to Minutes":
                return value *1440
            elif unit == "Days to Seconds":
                return value *86400
if category =="Length":
    unit = st.selectbox("📏Select Conversation", ["Kilometers to Centimeters", "Kilometers to Meters", "Kilometers to Feet", "Centimeters to Kilometers", "Centimeters to Meters", "Centimeters to Feet", "Meters to Kilometers", "Meters to Centimeters", "Meters to Feet", "Feet to Kilometers", "Feet to Centimeters", "Feet to Meters"])
elif category =="Weight":
    unit = st.selectbox("⚖️Select Conversation", ["Kilograms to Pounds", "Kilograms to Grams", "Kilograms to Ounces", "Pounds to Kilograms", "Pounds to Grams", "Pounds to Ounces", "Grams to Kilograms", "Grams to Pounds", "Grams to Ounces", "Ounces to Kilograms", "Ounces to Pounds", "Ounces to Grams"])
elif category == "Time":
    unit = st.selectbox("⏰Select Conversation", ["Hours to Minutes", "Hours to Seconds", "Hours to Days", "Minutes to Hours", "Minutes to seconds", "Minutes to Days", "Seconds to Hours", "Seconds to Days", "Seconds to Minutes", "Days to Hours", "Days to Minutes", "Days to Seconds"])
value = st.number_input("Enter Value Here To Convert ")
if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.write(f"Converted Value is {result:.2f} ")
st.markdown("<div class='footer'>Copyright © 2021. All rights reserved</div>", unsafe_allow_html=True)
st.markdown("<div class='footer1'>Made with ❤️ by Areeba</div>",unsafe_allow_html=True)
            
            