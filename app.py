import streamlit as st

st.set_page_config(page_title="UAV Battery Efficiency Estimator", layout="centered")

st.title("UAV Battery Efficiency Estimator")

# Max lift capacity per drone model (grams)
MAX_LIFT_G = {
    "Generic Quad": 1000,
    "DJI Phantom": 1200,
    "Custom Build": 1500
}

with st.form("uav_form"):
    st.subheader("Flight Parameters")
    drone_model = st.selectbox("Drone Model", list(MAX_LIFT_G.keys()))
    st.caption(f"Maximum payload for this drone: {MAX_LIFT_G[drone_model]} g")

    battery_capacity_wh = st.number_input("Battery Capacity (Wh)", min_value=1.0, value=50.0)
    payload_weight_g = st.number_input("Payload Weight (g)", min_value=0, value=500)
    flight_speed_kmh = st.number_input("Flight Speed (km/h)", min_value=0.0, value=30.0)
    wind_speed_kmh = st.number_input("Wind Speed (km/h)", min_value=0.0, value=10.0)
    temperature_c = st.number_input("Temperature (°C)", value=25.0)
    flight_mode = st.selectbox("Flight Mode", ["Hover", "Forward Flight", "Waypoint Mission"])

    submitted = st.form_submit_button("Estimate")

if submitted:
    if payload_weight_g > MAX_LIFT_G[drone_model]:
        st.error("Payload exceeds lift capacity. The drone cannot take off with this configuration.")
        st.stop()

    base_draw = 15  # Base power draw in W
    payload_factor = 0.01  # W per gram
    wind_penalty = 0.2  # W per km/h wind
    drag_factor = 0.005  # W per (km/h)^2

    drag_draw = drag_factor * (flight_speed_kmh ** 2) if flight_mode in ["Forward Flight", "Waypoint Mission"] else 0

    total_draw = base_draw + (payload_factor * payload_weight_g) + (wind_penalty * wind_speed_kmh) + drag_draw
    flight_time_minutes = (battery_capacity_wh / total_draw) * 60

    st.metric("Estimated Flight Time", f"{flight_time_minutes:.1f} minutes")

    if flight_mode != "Hover":
        flight_distance_km = (flight_time_minutes / 60) * flight_speed_kmh
        st.metric("Estimated Max Distance", f"{flight_distance_km:.2f} km")

    st.subheader("AI Suggestions (Simulated GPT)")
    if payload_weight_g > 800:
        st.write("**Tip**: Reduce payload to under 800g to increase endurance.")
    if wind_speed_kmh > 15:
        st.write("**Tip**: High wind may significantly reduce flight time—consider postponing.")
    if battery_capacity_wh < 30:
        st.write("**Tip**: Increase battery size or reduce mission length.")
    if drag_draw > 10:
        st.write("**Tip**: High flight speed may be causing excessive aerodynamic drag. Consider slowing down.")

st.caption("Demo project by Tareq Omrani | AI Engineering + UAV | 2025")