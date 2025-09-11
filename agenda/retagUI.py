import streamlit as st
from retang import Retangulo

class RetanguloUI:
    def main():
        st.header("Cálculos com retângulo")
        base = st.text_input("Informe a base: ")
        altura = st.text_input("Informe a altura: ")
        if st.button("Calcular"):
            b = float(base)
            h = float(altura)
            r = Retangulo(b, h)
            st.write(r)
            st.write(r.calc_area())
            st.write(r.calc_diagonal())