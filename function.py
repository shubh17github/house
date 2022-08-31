
import pickle
import json
import config
import numpy as np

class house():

    def __init__(self,area_type, bath, balcony, size, total_sqft, site_location):
        """ ___init___ method are used for acceptiong the user input"""
        self.area_type=area_type
        self.bath=bath
        self.balcony=balcony
        self.size=size
        self.total_sqft=total_sqft
        self.site_location=site_location


    def load_model(self):

        with open(config.model_file_path,'rb') as file:
            self.model=pickle.load(file)

        with open(config.col_dict_path,'r') as file:
            self.col_dict=json.load(file)

    def predict(self):

        self.load_model()

        array=np.zeros(len(self.col_dict['column']))

        array[0]=self.area_type
        array[1]=self.bath
        array[2]=self.balcony
        array[3]=self.size
        array[4]=self.total_sqft
        array[5]=self.site_location

       

        result =self.model.predict([array])
        return result[0]


# if __name__=='__main__':
#     area_type=4
#     bath=5
#     balcony=1.58
#     size=4
#     total_sqft=1519
#     site_location=67

#     price=house(area_type,bath,balcony,size,total_sqft,site_location)

#     res=price.predict()
#     print(res)








    



