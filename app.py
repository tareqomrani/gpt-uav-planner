import streamlit as st

st.set_page_config(page_title="UAV Battery Efficiency Estimator", layout="centered")

st.title("UAV Battery Efficiency Estimator")

with st.form("uav_form"):
    st.subheader("Flight Parameters")
    drone_model = st.selectbox("Drone Model", ["Generic Quad", "DJI Phantom", "Custom Build"])
    battery_capacity_wh = st.number_input("Battery Capacity (Wh)", min_value=1.0, value=50.0)
    payload_weight_g = st.number_input("Payload Weight (g)", min_value=0, value=500)
    flight_speed_kmh = st.number_input("Flight Speed (km/h)", min_value=0.0, value=30.0)
    wind_speed_kmh = st.number_input("Wind Speed (km/h)", min_value=0.0, value=10.0)
    temperature_c = st.number_input("Temperature (°C)", value=25.0)
    flight_mode = st.selectbox("Flight Mode", ["Hover", "Forward Flight", "Waypoint Mission"])

    submitted = st.form_submit_button("Estimate")

if submitted:
    if flight_mode in ["Forward Flight", "Waypoint Mission"] and flight_speed_kmh == 0:
        st.warning("Forward flight selected, but speed is 0 km/h. Please enter a valid flight speed.")
    else:
        base_draw = 15  # Base power draw in W
        payload_factor = 0.01  # W per gram
        wind_penalty = 0.2  # W per km/h wind
        drag_factor = 0.005  # W per (km/h)^2 (simplified aerodynamic drag)

        # Calculate drag power if in forward flight
        if flight_mode in ["Forward Flight", "Waypoint Mission"]:
            drag_draw = drag_factor * (flight_speed_kmh ** 2)
        else:
            drag_draw = 0

        total_draw = base_draw + (payload_factor * payload_weight_g) + (wind_penalty * wind_speed_kmh) + drag_draw

        # Prevent division by zero or negative power draw
        if total_draw <= 0:
            st.error("Calculated power draw is non-positive. Please check your inputs.")
        else:
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