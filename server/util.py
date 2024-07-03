import json
import pickle
import numpy as np
import pandas as pd

__region = None
__data_columns = None
__model = None
__scaler = None

def get_estimated_price(region,area,bhk):
    try:
        loc_index = __data_columns.index(region.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))

    x[0] = bhk
    x[1] = area

    if loc_index >= 0:
        x[loc_index] = 1

    x_df = pd.DataFrame([x], columns=__data_columns)
    x_df = x_df[__data_columns] 
    x_scaled = __scaler.transform(x_df)

    return round(__model.predict(x_scaled)[0],2)


def get_location_names():
    return __region

def load_asset():
    print("Loading Started")
    global __data_columns
    global __region

    with open("./assets/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __region = __data_columns[2:]

    global __model
    with open("./assets/mumbai_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("Loading Saved")

    global __scaler
    with open("./assets/scaler.pickle", 'rb') as f:
        __scaler = pickle.load(f)


if __name__ == '__main__':
    load_asset()
    # print(get_location_names())
    # print(get_estimated_price('Bandra East',800,2))
    # print(get_estimated_price('Bandra East',500,1))
    # print(get_estimated_price('chembur',800,2))
    # print(get_estimated_price('colaba',1000,3))