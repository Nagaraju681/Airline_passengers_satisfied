import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="Airline Passenger Satisfaction",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ Airline Passenger Satisfaction Prediction")
st.write("Predict whether a passenger is Satisfied or Dissatisfied.")

model = joblib.load("rf_model_f.pkl")
transformer = joblib.load("transformer.pkl")

st.sidebar.header("Passenger Information")

ID = st.sidebar.number_input(
    "Passenger ID",
    min_value=1,
    value=1,
    step=1
)

Gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

Age = st.sidebar.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=30
)

Customer_Type = st.sidebar.selectbox(
    "Customer Type",
    ["First-time", "Returning"]
)

Type_of_Travel = st.sidebar.selectbox(
    "Type of Travel",
    ["Business", "Personal"]
)

Class = st.sidebar.selectbox(
    "Class",
    ["Business", "Economy", "Economy Plus"]
)

st.subheader("✈️ Flight Information")

col1, col2, col3 = st.columns(3)

with col1:
    Flight_Distance = st.number_input(
        "Flight Distance",
        min_value=0.0,
        value=1000.0
    )

with col2:
    Departure_Delay = st.number_input(
        "Departure Delay",
        min_value=0.0,
        value=0.0
    )

with col3:
    Departure_Arrival_Convenience = st.slider(
        "Departure and Arrival Time Convenience",
        0.0,
        5.0,
        3.0
    )

st.subheader("⭐ Service Ratings")

col1, col2, col3, col4 = st.columns(4)

with col1:
    Ease_Online_Booking = st.slider(
        "Ease of Online Booking",
        0.0,
        5.0,
        3.0
    )

with col2:
    Check_in_Service = st.slider(
        "Check-in Service",
        0.0,
        5.0,
        3.0
    )

with col3:
    Online_Boarding = st.slider(
        "Online Boarding",
        0.0,
        5.0,
        3.0
    )

with col4:
    Gate_Location = st.slider(
        "Gate Location",
        0.0,
        5.0,
        3.0
    )

col1, col2, col3, col4 = st.columns(4)

with col1:
    On_board_Service = st.slider(
        "On-board Service",
        0.0,
        5.0,
        3.0
    )

with col2:
    Seat_Comfort = st.slider(
        "Seat Comfort",
        0.0,
        5.0,
        3.0
    )

with col3:
    Leg_Room_Service = st.slider(
        "Leg Room Service",
        0.0,
        5.0,
        3.0
    )

with col4:
    Cleanliness = st.slider(
        "Cleanliness",
        0.0,
        5.0,
        3.0
    )

col1, col2, col3, col4 = st.columns(4)

with col1:
    Food_and_Drink = st.slider(
        "Food and Drink",
        0.0,
        5.0,
        3.0
    )

with col2:
    In_flight_Service = st.slider(
        "In-flight Service",
        0.0,
        5.0,
        3.0
    )

with col3:
    In_flight_Wifi_Service = st.slider(
        "In-flight Wifi Service",
        0.0,
        5.0,
        3.0
    )

with col4:
    In_flight_Entertainment = st.slider(
        "In-flight Entertainment",
        0.0,
        5.0,
        3.0
    )

Baggage_Handling = st.slider(
    "Baggage Handling",
    0.0,
    5.0,
    3.0
)

Age_Group = pd.cut(
    pd.Series([Age]),
    bins=[0, 18, 35, 55, np.inf],
    labels=[
        "Children",
        "Young Adults",
        "Middle Age",
        "Senior Citizens"
    ]
)[0]

Seat_Comfort_Group = pd.cut(
    pd.Series([Seat_Comfort]),
    bins=[0, 2, 3, 5],
    labels=[
        "Poor",
        "Average",
        "Good"
    ]
)[0]

Distance_Group = pd.cut(
    pd.Series([Flight_Distance]),
    bins=[0, 500, 1000, 2000, np.inf],
    labels=[
        "Short",
        "Medium",
        "Long",
        "Very Long"
    ]
)[0]

input_data = pd.DataFrame({
    "ID": [ID],
    "Gender": [Gender],
    "Age": [Age],
    "Customer Type": [Customer_Type],
    "Type of Travel": [Type_of_Travel],
    "Class": [Class],
    "Flight Distance": [Flight_Distance],
    "Departure Delay": [Departure_Delay],
    "Departure and Arrival Time Convenience": [Departure_Arrival_Convenience],
    "Ease of Online Booking": [Ease_Online_Booking],
    "Check-in Service": [Check_in_Service],
    "Online Boarding": [Online_Boarding],
    "Gate Location": [Gate_Location],
    "On-board Service": [On_board_Service],
    "Seat Comfort": [Seat_Comfort],
    "Leg Room Service": [Leg_Room_Service],
    "Cleanliness": [Cleanliness],
    "Food and Drink": [Food_and_Drink],
    "In-flight Service": [In_flight_Service],
    "In-flight Wifi Service": [In_flight_Wifi_Service],
    "In-flight Entertainment": [In_flight_Entertainment],
    "Baggage Handling": [Baggage_Handling],
    "Age_Group": pd.Series([Age_Group], dtype="category"),
    "Seat_Comfort_Group": pd.Series([Seat_Comfort_Group], dtype="category"),
    "Distance_Group": pd.Series([Distance_Group], dtype="category")
})

st.subheader("📋 Input Details")
st.dataframe(input_data, use_container_width=True)

if st.button("🔮 Predict Satisfaction"):

    transformed_data = transformer.transform(input_data)

    prediction = model.predict(transformed_data)[0]

    if prediction == 1:
        result = "Satisfied"
    else:
        result = "Dissatisfied"

    st.subheader("Prediction")

    if result == "Satisfied":
        st.success("😊 Passenger is Satisfied")
    else:
        st.error("😞 Passenger is Dissatisfied")

    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(transformed_data)[0]

        st.subheader("Prediction Probability")

        probability_df = pd.DataFrame({
            "Class": ["Dissatisfied", "Satisfied"],
            "Probability": probability
        })

        probability_df["Probability"] = (
            probability_df["Probability"] * 100
        ).round(2)

        st.dataframe(
            probability_df,
            use_container_width=True
        )

st.markdown("---")
st.caption("Machine Learning Model: Random Forest Classifier")
