# Mumbai House Price Prediction Project

## Overview

This project aims to predict house prices in Mumbai based on various features such as carpet area, BHK  configuration, and location. The project involves data processing, model building, and deployment to provide users with an estimate of house prices through a web application.

## Project Components

### 1. Data Collection and Preprocessing

- **Dataset**: The project uses a dataset containing information about Mumbai house prices, including features such as `area`, `BHK`, `location`, and `price`.
- **Preprocessing Steps**:
  - **Loading Data**: Imported the dataset using `pandas`.
  - **Filtering Relevant Columns**: Removed unnecessary columns and calculated `price_per_sqft`.
  - **Outlier Removal**: Implemented a function to remove outliers based on the price per square foot.
  - **Feature Engineering**: Converted categorical `region` data into numerical dummy variables and dropped redundant columns.

### 2. Model Building

- **Model Selection**: Used `Linear Regression` to predict house prices.
- **Data Splitting**: Divided the dataset into training and testing sets using `train_test_split`.
- **Feature Scaling**: Applied `StandardScaler` to normalize features.
- **Model Training**: Trained the `Linear Regression` model and evaluated its performance.
- **Model Evaluation**: Assessed the model’s performance using the test set.

### 3. Model Deployment

- **Backend**: Created a Flask backend with the following features:
  - **Endpoints**:
    - `GET /get_location_names`: Fetches available location names.
    - `POST /predict_home_prices`: Takes `area`, `bhk`, and `region` as inputs and returns the predicted house price.
  - **CORS Configuration**: Enabled cross-origin requests for frontend-backend communication.

- **Frontend**: Developed a responsive landing page with the following features:
  - **Background Image**: Aesthetic background with a blurred image of Mumbai.
  - **Form Elements**: Inputs for `area`, `bhk`, and `region`, with options to choose location, required Carpet Area and number of BHKs.
  - **Price Estimation**: A button to submit the form and display the predicted price.

### 4. Asset Management

- **Model and Scaler**: Saved the trained model and scaler objects using `pickle`.
- **Feature Columns**: Stored feature columns in a JSON file for consistency between frontend and backend.

### 5. Technologies Used

- **Programming Languages**: Python, HTML, CSS, JavaScript
- **Libraries and Frameworks**: 
  - **Data Processing**: `pandas`, `numpy`
  - **Modeling**: `scikit-learn`
  - **Web Development**: `Flask`, `Streamlit` (for model deployment), `AJAX` (for frontend-backend interaction)
- **Tools**: `Git`, `GitHub`, `Visual Studio Code`

  ## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/mumbai-house-prices-prediction.git
   ```
2. **Navigate to the Server Directory**:
   ```bash
   cd server
   ```
3. **Run the Server**:
   ```bash
   python server.py
   ```
4. **Navigate to Client Directory**:
   ```bash
   cd client
   ```
5. **Launch the Live Server**:
   ```bash
   Go Live
   ```
   
