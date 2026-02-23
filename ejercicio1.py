import streamlit as st

def mostrar_ejercicio_1():
    st.title("💰 Ejercicio 1 – Variables y Condicionales")
    
    
    st.markdown("---")
    st.subheader("Control de Presupuesto")
    # 1 y 2. Entradas de números
    presupuesto = st.number_input("Ingresa tu presupuesto:", min_value=0.0, step=100.0)
    gasto = st.number_input("Ingresa el gasto:", min_value=0.0, step=10.0)

    # 3. Botón para ejecutar
    if st.button("Evaluar Presupuesto"):
        diferencia = presupuesto - gasto
        
        # 4 y 5. Lógica de condicionales
        if gasto <= presupuesto:
            st.success("✅ ¡Felicidades! El gasto no exede el presupuesto.")
        else:
            st.warning("⚠️ ¡Cuidado! El presupuesto se excedio.")
        
        # 6. Mostrar diferencia
        st.write(f"La diferencia entre presupuesto y gasto es: **${diferencia:,.2f}**")