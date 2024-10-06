import streamlit as st
import pickle
from PIL import Image

# Define mappings for categorical features based on the data you provided
make_mapping = {
    'Suzuki': 1,
    'Honda': 2,
    'Toyota': 3,
    'Daihatsu': 4,
    'Hyundai': 5,
    'Mitsubishi': 6,
    'KIA': 7,
    'Changan': 8,
    'FAW': 9,
    'Chevrolet': 10,
    'Mercedes': 11
}

model_mapping = {
    'City IVTEC': 1,
    'Alto': 2,
    'Bolan': 3,
    'Cuore': 4,
    'Corolla GLI': 5,
    'Mehran VXR': 6,
    'Mira': 7,
    'Santro': 8,
    'Wagon R': 9,
    'Civic Prosmetic': 10,
    'Corolla XLI': 11,
    'Swift': 12,
    'Cultus VXR': 13,
    'City Aspire': 14,
    'Corrolla Altis': 15,
    'Yaris': 16,
    'Hijet': 17,
    'Every': 18,
    'City IDSI': 19,
    'Passo': 20,
    'Civic Oriel': 21,
    'Move': 22,
    'Baleno': 23,
    'Lancer': 24,
    'Altis Grande': 25,
    'City Vario': 26,
    'Picanto': 27,
    'Karvaan': 28,
    'Alsvin': 29,
    'Ravi': 30,
    'X-PV': 31,
    'Classic': 32,
    'Ek Wagon': 33,
    'V2': 34,
    'Terios Kid': 35,
    'Joy': 36,
    'Pajero Mini': 37,
    'Spectra': 38,
    'Exclusive': 39,
    'Sportage': 40,
    'C Class': 41,
    'E Class': 42,
    'Minica': 43,
    'Minicab Bravo': 44,
    'Civic EXi': 45,
    'Mehran VX': 46,
    'Corolla Assista': 47,
    'Civic VTi': 48,
    'Cervo': 49,
    'Corolla Axio': 50,
    'Every Wagon': 51,
    'Liana': 52,
    'Surf': 53,
    'Civic VTi Oriel': 54,
    'Khyber': 55,
    'Cultus VXL': 56,
    'Prius': 57,
    'ISIS': 58
}

fuel_mapping = {
    'Petrol': 1,
    'CNG': 2,
    'Hybrid': 3,
    'Diesel': 4
}

car_documents_mapping = {
    'Original': 1,
    'Duplicate': 2
}

assembly_mapping = {
    'Local': 1,
    'Imported': 2
}

transmission_mapping = {
    'Manual': 1,
    'Automatic': 2
}

condition_mapping = {
    'Used': 1  # Only one condition present
}

def main():
    st.title(":car: OLX Car Price Prediction System")
    image = Image.open("image.jpeg")  # Make sure this image file exists in your directory
    st.image(image, width=800)

    # Load the saved model
    model = pickle.load(open('model.sav', 'rb'))

    # Get user input for each feature
    car_name_input = st.text_input(":blue[Car Name]", "Type here")
    make_input = st.selectbox(":blue[Make]", list(make_mapping.keys()))
    model_input = st.selectbox(":blue[Model]", list(model_mapping.keys()))
    fuel_input = st.selectbox(":blue[Fuel Type]", list(fuel_mapping.keys()))
    car_documents_input = st.selectbox(":blue[Car Documents]", list(car_documents_mapping.keys()))
    assembly_input = st.selectbox(":blue[Assembly]", list(assembly_mapping.keys()))
    transmission_input = st.selectbox(":blue[Transmission]", list(transmission_mapping.keys()))
    condition_input = st.selectbox(":blue[Condition]", list(condition_mapping.keys()))

    year_input = st.number_input(":blue[Year]", min_value=1990, max_value=2024, step=1)
    kms_input = st.number_input(":blue[Kilometers Driven]", min_value=0)

    # Convert categorical inputs to numerical values using mappings
    car_name_num = 0  # Car Name was not included in mappings, need to add it if it's a feature
    make_num = make_mapping.get(make_input, 0)
    model_num = model_mapping.get(model_input, 0)
    fuel_num = fuel_mapping.get(fuel_input, 0)
    car_documents_num = car_documents_mapping.get(car_documents_input, 0)
    assembly_num = assembly_mapping.get(assembly_input, 0)
    transmission_num = transmission_mapping.get(transmission_input, 0)
    condition_num = condition_mapping.get(condition_input, 0)

    # Create the input feature array with all numerical features
    features = [car_name_num, make_num, model_num, year_input, kms_input, fuel_num, 
                car_documents_num, assembly_num, transmission_num, condition_num]

    if st.button("Predict Price"):
        features = [features]  # Model expects a 2D array
        predicted_price = model.predict(features)
        st.write(f"Predicted Price: ₹{predicted_price[0]:,.2f}")

if __name__ == '__main__':
    main()
