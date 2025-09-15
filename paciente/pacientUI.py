import streamlit as st
from datetime import datetime
from pacient import Paciente

class PacienteUI:
    def main():
        st.header("Dados do paciente")
        nome = st.text_input("Digite o nome: ")
        cpf = st.text_input("Digite o CPF: ")
        tel = st.text_input("Digite o número de telefone: ")
        nasc = st.date_input("Digitea data de nascimento: ")
        if st.button("Idade"):
            paciente = Paciente(nome, cpf, tel, nasc)
            st.write(paciente)
            st.write(paciente.idade())