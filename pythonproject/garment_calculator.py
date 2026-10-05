import streamlit as st_lit
def calculator_production_time(quantity,minutes_per_garment,workers,efficiency):
    total_work_minutes = quantity * minutes_per_garment
    theoritical_minutes = total_work_minutes /workers
    acutal_minutes =theoritical_minutes/(efficiency/100)
    hours =acutal_minutes /60
    return hours

st_lit.title("==Garment production Time predictor ==")
quantity = st_lit.number_input("quantity",min_value=0)
minutes=st_lit.number_input("minutes per garment",min_value=0.1)
workers=st_lit.number_input("workers: ",min_value=1)
efficiency=st_lit.number_input("efficiecny",min_value=0.1)

if st_lit.button("calculate production time"):
    calculated_hours = calculator_production_time(quantity,minutes,workers,efficiency)
    st_lit.write("Estimated production time:",round(calculated_hours,2))
