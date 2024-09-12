import streamlit as st


def calculate_sum(p,t):
    return p*t

st.subheader("The Used Energy is calculated by multiplying the power by the elapsed time:")

p = st.number_input ("Power (W)")
t = st.number_input("Time in seconds (s)")

if st.button("Calculate Used Energy"):
    st.write("Used Energy W is : "+ str(calculate_sum(p,t)))


st.subheader("Calculate the power with the following formula:P=V*I")

def calculate_sum(v,i):
    return v*i

v = st.number_input("Voltage in Volt(V)")
i = st.number_input("Current in ampère (A)")

if st.button("Calculate Power P"):
    st.write("Power P is : "+ str(calculate_sum(v,i)))
