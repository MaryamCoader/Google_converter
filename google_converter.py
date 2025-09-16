# Unit Converter App
# This app allows users to convert between different units of measurement
# for Length, Temperature, Weight, and Time.


import streamlit as st

st.set_page_config(page_title="Unit Converter", layout="centered")

st.title("🔄 Google Style Unit Converter")
st.write("Convert between Length, Temperature, Weight and Time")

# Choose category
category = st.selectbox("Select Conversion Category", ["Length", "Temperature", "Weight", "Time"])

# Define units for each category
units = {
    "Length": ["Meters", "Kilometers", "Miles", "Feet"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Weight": ["Kilograms", "Grams", "Pounds"],
    "Time": ["Seconds", "Minutes", "Hours"]
}

from_unit = st.selectbox("From", units[category])
to_unit = st.selectbox("To", units[category])
value = st.number_input("Enter value", format="%.4f")

def convert(category, from_unit, to_unit, value):
    if category == "Length":
        conversion = {
            "Meters": 1,
            "Kilometers": 1000,
            "Miles": 1609.34,
            "Feet": 0.3048
        }
        return value * conversion[from_unit] / conversion[to_unit]

    elif category == "Temperature":
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return value * 9/5 + 32
            elif to_unit == "Kelvin":
                return value + 273.15
            return value
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
            return value
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
            return value

    elif category == "Weight":
        conversion = {
            "Kilograms": 1,
            "Grams": 0.001,
            "Pounds": 0.453592
        }
        return value * conversion[from_unit] / conversion[to_unit]

    elif category == "Time":
        conversion = {
            "Seconds": 1,
            "Minutes": 60,
            "Hours": 3600
        }
        return value * conversion[from_unit] / conversion[to_unit]

# Show result
if st.button("Convert"):
    if from_unit == to_unit:
        st.success(f"Result: {value} {to_unit}")
    else:
        result = convert(category, from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")


        