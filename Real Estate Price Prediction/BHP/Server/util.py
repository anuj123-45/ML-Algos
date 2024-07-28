import json
import pickle

__locations=None
__model=None
__data_columns=None



def get_location_names():
    return __locations


def load_save_artifacts():
    print('loading saved artifacts started....')
    global __data_columns
    global __locations

    with open('./Artifacts/columns.json','r') as f:
        __data_columns=json.load(f)['data_columns']
        __locations=__data_columns[3:]

    with open('./Artifacts/bengaluru_house_prices_model.pickle','rb') as f:
        __model=pickle.load(f)
        print('loading saved artifacts done...')







if __name__ == '__main__':
    load_save_artifacts()
    print(get_location_names())