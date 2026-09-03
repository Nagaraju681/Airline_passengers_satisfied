import streamlit as st
import pandas as pd
import joblib

# ---------------- LOAD MODEL ----------------
model = joblib.load("knn_model.pkl")


# ---------------- TITLE ----------------
st.title("✈️ Airline Passenger Satisfaction Prediction")


# ---------------- NUMERICAL INPUTS ----------------
st.header("Numerical Features")

Age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=30
)

Flight_Distance = st.number_input(
    "Flight Distance",
    min_value=0,
    value=1000
)

Departure_Delay = st.number_input(
    "Departure Delay",
    min_value=0,
    value=0
)

Departure_Arrival_Time_Convenience = st.number_input(
    "Departure and Arrival Time Convenience",
    min_value=0,
    max_value=5,
    value=3
)

Ease_Online_Booking = st.number_input(
    "Ease of Online Booking",
    min_value=0,
    max_value=5,
    value=3
)

Check_in_Service = st.number_input(
    "Check-in Service",
    min_value=0,
    max_value=5,
    value=3
)

Online_Boarding = st.number_input(
    "Online Boarding",
    min_value=0,
    max_value=5,
    value=3
)

Gate_Location = st.number_input(
    "Gate Location",
    min_value=0,
    max_value=5,
    value=3
)

On_board_Service = st.number_input(
    "On-board Service",
    min_value=0,
    max_value=5,
    value=3
)

Seat_Comfort = st.number_input(
    "Seat Comfort",
    min_value=0,
    max_value=5,
    value=3
)

Leg_Room_Service = st.number_input(
    "Leg Room Service",
    min_value=0,
    max_value=5,
    value=3
)

Cleanliness = st.number_input(
    "Cleanliness",
    min_value=0,
    max_value=5,
    value=3
)

Food_and_Drink = st.number_input(
    "Food and Drink",
    min_value=0,
    max_value=5,
    value=3
)

In_flight_Service = st.number_input(
    "In-flight Service",
    min_value=0,
    max_value=5,
    value=3
)

In_flight_Wifi_Service = st.number_input(
    "In-flight Wifi Service",
    min_value=0,
    max_value=5,
    value=3
)

In_flight_Entertainment = st.number_input(
    "In-flight Entertainment",
    min_value=0,
    max_value=5,
    value=3
)

Baggage_Handling = st.number_input(
    "Baggage Handling",
    min_value=0,
    max_value=5,
    value=3
)


# ---------------- CATEGORICAL INPUTS ----------------
st.header("Categorical Features")

Gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

Customer_Type = st.selectbox(
    "Customer Type",
    ["First-time", "Returning"]
)

Type_of_Travel = st.selectbox(
    "Type of Travel",
    ["Business travel", "Personal Travel"]
)

Class = st.selectbox(
    "Class",
    ["Business", "Economy", "Economy Plus"]
)

Age_Group = st.selectbox(
    "Age Group",
    ["Young", "Adult", "Middle Age", "Senior"]
)

Seat_Comfort_Group = st.selectbox(
    "Seat Comfort Group",
    ["Poor", "Average", "Good", "Excellent"]
)

Distance_Group = st.selectbox(
    "Distance Group",
    ["Short", "Medium", "Long"]
)


# ---------------- CREATE INPUT DATAFRAME ----------------
input_data = pd.DataFrame({

    "Age": [Age],
    "Flight Distance": [Flight_Distance],
    "Departure Delay": [Departure_Delay],

    "Departure and Arrival Time Convenience":
        [Departure_Arrival_Time_Convenience],

    "Ease of Online Booking":
        [Ease_Online_Booking],

    "Check-in Service":
        [Check_in_Service],

    "Online Boarding":
        [Online_Boarding],

    "Gate Location":
        [Gate_Location],

    "On-board Service":
        [On_board_Service],

    "Seat Comfort":
        [Seat_Comfort],

    "Leg Room Service":
        [Leg_Room_Service],

    "Cleanliness":
        [Cleanliness],

    "Food and Drink":
        [Food_and_Drink],

    "In-flight Service":
        [In_flight_Service],

    "In-flight Wifi Service":
        [In_flight_Wifi_Service],

    "In-flight Entertainment":
        [In_flight_Entertainment],

    "Baggage Handling":
        [Baggage_Handling],

    "Gender":
        [Gender],

    "Customer Type":
        [Customer_Type],

    "Type of Travel":
        [Type_of_Travel],

    "Class":
        [Class],

    "Age_Group":
        [Age_Group],

    "Seat_Comfort_Group":
        [Seat_Comfort_Group],

    "Distance_Group":
        [Distance_Group]
})


# ---------------- PREDICTION ----------------
if st.button("Predict Passenger Satisfaction"):

    prediction = model.predict(input_data)

    st.write("Prediction:", prediction[0])

    if prediction[0] in [1, "1", "satisfied", "Satisfied"]:
        st.success("😊 Passenger is Satisfied")
    else:
        st.error("😞 Passenger is Neutral/Dissatisfied")