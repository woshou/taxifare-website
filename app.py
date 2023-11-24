import streamlit as st
import requests
'''
# TaxiFareModel front
'''
st.title("Taxi Fare Prediction")
st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

'''
# User input section
date_time = st.text_input("Date and Time", "2023-11-24 12:00:00")
pickup_longitude = st.number_input("Pickup Longitude", value=0.0)
pickup_latitude = st.number_input("Pickup Latitude", value=0.0)
dropoff_longitude = st.number_input("Dropoff Longitude", value=0.0)
dropoff_latitude = st.number_input("Dropoff Latitude", value=0.0)
passenger_count = st.number_input("Passenger Count", value=1, min_value=1)


url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')
if st.button("Predict Fare"):
    # Build the input parameters dictionary
    params = {
        "pickup_datetime": date_time,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count,
    }

    # Call the API
    response = requests.get("https://taxifare.lewagon.ai/predict", params=params)

 # Display the full response for debugging purposes
    # Check for successful response
if response.status_code == 200:
        try:
            # Extract and display the prediction
            prediction = response.json().get("prediction")
            if prediction is not None:
                st.success(f"Predicted Taxi Fare: ${prediction:.2f}")
        except Exception as e:
            st.error(f"Error extracting prediction: {e}")
        else:
            st.text(response.text)