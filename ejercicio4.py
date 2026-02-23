import streamlit as st

# 1. Definir la clase Actividad con su constructor
class Actividad:
    def __init__(self, nombre, tipo, presupuesto, gasto_real):
        self.nombre = nombre
        self.tipo = tipo
        self.presupuesto = presupuesto
        self.gasto_real = gasto_real

    # 2. Método para evaluar presupuesto
    def esta_en_presupuesto(self):
        return self.gasto_real <= self.presupuesto

    # 3. Método para devolver un resumen de la actividad
    def mostrar_info(self):
        return f"Actividad: **{self.nombre}** | Categoría: *{self.tipo}*"

def mostrar_ejercicio_4():
    st.title("🏗️ Ejercicio 4 – Programación Orientada a Objetos")
    st.subheader("Gestión de Objetos Financieros")

    # Verificamos si hay datos del Ejercicio 2 para convertirlos en Objetos
    if 'lista_actividades' in st.session_state and len(st.session_state.lista_actividades) > 0:
        
        st.write("A continuación se presentan los registros convertidos en **Objetos de la clase Actividad**:")
        st.divider()

        # 4. Convertir los registros (diccionarios) en Objetos y mostrarlos
        for idx, datos in enumerate(st.session_state.lista_actividades):
            # Instanciamos la clase
            obj_actividad = Actividad(
                datos['nombre'], 
                datos['tipo'], 
                datos['presupuesto'], 
                datos['gasto_real']
            )

            # 5. Mostrar la información usando los métodos de la clase
            st.markdown(f"### Registro #{idx + 1}")
            st.write(obj_actividad.mostrar_info()) # Llamada al método mostrar_info()
            
            diferencia = obj_actividad.presupuesto - obj_actividad.gasto_real

            # Evaluación mediante el método esta_en_presupuesto()
            if obj_actividad.esta_en_presupuesto():
                st.success(f"Estado: Dentro del presupuesto (Ahorro: ${diferencia:,.2f})")
            else:
                st.warning(f"Estado: Presupuesto excedido (Déficit: ${abs(diferencia):,.2f})")
            
            st.divider()
    else:
        st.info("No hay datos para procesar. Por favor, registra actividades en el **Ejercicio 2**.")