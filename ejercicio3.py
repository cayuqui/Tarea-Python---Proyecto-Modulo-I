import streamlit as st

# 1. Definir la función calcular_retorno
def calcular_retorno(presupuesto, tasa, meses):
    """
    Calcula el retorno basado en la fórmula: Presupuesto * Tasa * Meses
    """
    return presupuesto * tasa * meses

def mostrar_ejercicio_3():
    st.title("⚡ Ejercicio 3 – Funciones y Programación Funcional")
    st.subheader("Cálculo de Retorno Esperado")

    # Verificar si existen datos del Ejercicio 2
    if 'lista_actividades' in st.session_state and len(st.session_state.lista_actividades) > 0:
        
        st.markdown("""
        En este módulo calculamos el retorno proyectado de inversión para cada actividad registrada 
        utilizando funciones de orden superior (`map` y `lambda`).
        """)

        # 2. Obtener la tasa y los meses mediante inputs
        col1, col2 = st.columns(2)
        with col1:
            tasa = st.slider("Seleccione la tasa de retorno", min_value=1.0, max_value=10.0, value=5.0, step=0.5)
        with col2:
            meses = st.number_input("Cantidad de meses:", min_value=1, max_value=12, value=6)

        # 3. Al presionar el botón, ejecutar el cálculo funcional
        if st.button("Calcular Retornos Proyectados"):
            st.divider()
            
            # Extraemos solo los presupuestos de nuestra lista de diccionarios
            presupuestos = [act['presupuesto'] for act in st.session_state.lista_actividades]
            nombres = [act['nombre'] for act in st.session_state.lista_actividades]

            # Aplicamos map y lambda para calcular los retornos            
            resultados = list(map(lambda p: calcular_retorno(p, tasa, meses), presupuestos))

            # 4. Mostrar el retorno esperado por cada actividad
            st.markdown("### 📈 Resultados del Análisis")
            
            # Combinamos nombres y resultados para mostrar
            for nombre, retorno in zip(nombres, resultados):
                col_a, col_b = st.columns([2, 1])
                col_a.write(f"**Actividad:** {nombre}")
                col_b.write(f"**Retorno:** :green[${retorno:,.2f}]")
            
            st.success(f"Cálculo completado exitosamente para {len(resultados)} actividades.")
            
    else:
        st.warning("⚠️ No hay datos registrados.")
        st.info("Por favor, ingresa actividades en el **Ejercicio 2** para poder realizar este cálculo.")