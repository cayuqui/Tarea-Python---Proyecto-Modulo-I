import streamlit as st
# IMPORTAMOS el archivo que acabamos de crear
import home
import ejercicio1 
import ejercicio2
import ejercicio3
import ejercicio4


st.sidebar.title("Menú de Navegación")
opcion = st.sidebar.selectbox(
    "Selecciona una sección:",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

if opcion == "Home":
    st.title("🏠 Página de Inicio")
    st.write("Bienvenido a mi proyecto de clase.")
    st.sidebar.markdown("---")    
    st.sidebar.write("© 2026 - Proyecto de Clase") 
    st.sidebar.caption("Desarrollado por Carmen Quispe Huaman")
    home.mostrar_home()  # Llamamos a la función del archivo home.py

elif opcion == "Ejercicio 1":  
    ejercicio1.mostrar_ejercicio_1()

elif opcion == "Ejercicio 2":
    ejercicio2.mostrar_ejercicio_2()
    
elif opcion == "Ejercicio 3":
    ejercicio3.mostrar_ejercicio_3()

elif opcion == "Ejercicio 4":
    ejercicio4.mostrar_ejercicio_4()