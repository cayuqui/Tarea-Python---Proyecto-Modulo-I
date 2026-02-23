import streamlit as st
import pandas as pd

def mostrar_ejercicio_2():
    st.title("📊 Ejercicio 2 – Listas y Diccionarios")
    st.subheader("Registro de Actividades Financieras")

    # 1. Crear la lista en el "estado de la sesión" si no existe (la memoria de la app)
    if 'lista_actividades' not in st.session_state:
        st.session_state.lista_actividades = []

    # --- FORMULARIO DE ENTRADA ---
    st.markdown("### Registrar Nueva Actividad")
    
    # 2. Solicitar los datos mediante inputs
    nombre = st.text_input("Nombre de la actividad:", placeholder="Ej: Compra de insumos")
    tipo = st.selectbox("Tipo de actividad:", ["Alimentos", "Cuidado Personal", "Educación","Seguros","Servicios basicos", "Otros"])
    presupuesto = st.number_input("Presupuesto asignado:", min_value=0.0, step=100.0)
    gasto_real = st.number_input("Gasto real ejecutado:", min_value=0.0, step=100.0)
    estado = presupuesto-gasto_real

    # 3. Al presionar "Agregar", guardar como diccionario en la lista
    if st.button("Agregar Actividad"):
        if nombre: # Validación simple de que el nombre no esté vacío
            nueva_actividad = {
                "nombre": nombre,
                "tipo": tipo,
                "presupuesto": presupuesto,
                "gasto_real": gasto_real,
                "estado" : estado
            }
            st.session_state.lista_actividades.append(nueva_actividad)
            st.success(f"Actividad '{nombre}' agregada con éxito.")
        else:
            st.error("Por favor, ingresa un nombre para la actividad.")

    st.divider()

    # --- VISUALIZACIÓN Y LÓGICA ---
    if st.session_state.lista_actividades:
        st.subheader("Lista de Actividades")
        
        # 4. Mostrar la lista en formato tabla (usando DataFrame para que se vea pro)
        df = pd.DataFrame(st.session_state.lista_actividades)
        st.dataframe(df, use_container_width=True)

        st.subheader("Evaluación de Estado")
        
        # 5. Recorrer la lista con un bucle
        for idx, act in enumerate(st.session_state.lista_actividades):
            # 6. Evaluar cada actividad
            diferencia = act['presupuesto'] - act['gasto_real']
            
            if act['gasto_real'] <= act['presupuesto']:
                estado = "✅ DENTRO DEL PRESUPUESTO"
                color = "green"
            else:
                estado = "❌ EXCEDIDO"
                color = "red"
            
            # 7. Mostrar el estado de cada actividad
            st.markdown(f"**{idx + 1}. {act['nombre']}** ({act['tipo']}): "
                        f":{color}[{estado}] | Diferencia: ${diferencia:,.2f}")
    else:
        st.info("Aún no hay actividades registradas. Usa el formulario de arriba.")