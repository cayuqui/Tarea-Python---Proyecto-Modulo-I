import streamlit as st

def mostrar_home():
    # --- Título del proyecto ---
    st.title("🚀 Sistema Integrado de Gestión Financiera")
    # --- Contenido Principal ---
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### 🎓 Información del Estudiante")
        col_label, col_data = st.columns([1, 2])
        # Usamos columnas para que las etiquetas estén a la izquierda y el contenido a la derecha
        with col_label:
            st.write("**Estudiante:**")
            st.write("**Curso:**")
            st.write("**Año:**")

        with col_data:
            st.write("Carmen Yuli Quispe Huaman")
            st.write("Especialización en Python for Analytics")
            st.write("2026")
        
        st.subheader("Descripción del Proyecto")
        descripcion = """
        Este proyecto es una aplicación interactiva desarrollada para gestionar y analizar 
        actividades financieras de manera eficiente. El objetivo principal es aplicar conceptos 
        fundamentales de Python, como el manejo de variables, estructuras de datos y 
        Programación Orientada a Objetos (POO).
        """
        st.markdown(f'<div style="text-align: justify;">{descripcion}</div>', unsafe_allow_html=True)
        st.write("A través de los diferentes módulos, el usuario podrá validar presupuestos, registrar gastos y visualizar reportes detallados.")

    with col2:
        # mi logo
        st.image("https://cdn-icons-png.flaticon.com/512/2622/2622113.png", width=150)

    st.divider()

    # --- Tecnologías Utilizadas ---
    st.subheader("🛠️ Tecnologías Utilizadas")
    
    # Usamos st.markdown para una lista con estilo
    st.markdown("""
    * **Python:** Lenguaje base para la lógica de programación.
    * **Streamlit:** Framework para la creación de la interfaz web interactiva.
    * **Pandas:** Manipulación y estructuración de datos en tablas.
    * **Programación Orientada a Objetos (POO):** Para la arquitectura del sistema.
    """)

    # Pie de página simple
    st.info("Utilice el menú lateral para navegar entre los ejercicios del proyecto.")