import streamlit as st
import math

st.write("### Cálculo Ruído - Norma ANSI/AGMA 6025-E19")

potencia_redutor = st.number_input("Potência do motor (kW)", value=0.1, min_value=0.1, max_value=200.00, step=0.01, format="%.2f") # potencia de entrada do redutor

if potencia_redutor > 0:
    potencia_redutor = potencia_redutor * 1000
    constante_engrenagem = st.number_input("Alta qualidade / helicoidal: 55-60 -- Industrial comum: 60-65 -- Engrenagem reta / desgastado: 65-70", value=55.0, step=5.0, max_value=70.0, min_value=55.0, format="%.0f")
    logaritmo = math.log10(potencia_redutor)
    lw = constante_engrenagem + 10*logaritmo
    print(lw)
    if constante_engrenagem > 0:
        distancia = st.number_input("Distancia (m)", value=0.5, step=0.5, max_value=5.0, min_value=0.5, format="%.1f")
        if distancia > 0:
            logaritmo2 = math.log10(4*math.pi*(distancia**2))
            lp = lw - 10*logaritmo2
            print(lp)
            unidade = "dB"
            st.chat_message("assistant").write(f"Ruído de: {lp:.2f} {unidade}")