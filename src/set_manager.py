import glob
from typing import Iterator
from .set_reader import Brickset

class MergedList():
    def __init__(self, goallist:list, datalist:list):
        self.goallist = goallist
        self.datalist = datalist
    
    def update_list(self):
        for new_item in self.datalist:
            found = False
            for item in self.goallist:
                if item['PartID'] == new_item['PartID']:
                    found = True
                    if item['Quantity'] < new_item['Quantity']:         
                        # Add the big value
                        item['Quantity'] = new_item['Quantity']
            # Add a new item            
            if found == False:
                self.goallist.append(new_item)
        return self.goallist


class LegoManager():
    # import necessary libraries
    def __init__(self, source_path):
        self.path = source_path + f'**/*.csv'
        self.csv_files = Iterator
        self.bricksetGoal = []

    def search_csv_files(self):
        # use glob to get all the csv files 
        # in the path
        self.csv_files = glob.iglob(self.path, recursive=True)

    def read_data(self):
        self.search_csv_files()
        # # loop over the list of csv files
        for file in self.csv_files:
            brickset = Brickset()
            brickset.read_data_set(file)
            new_brickset = brickset.extract()
            merger = MergedList(self.bricksetGoal, new_brickset)
            self.bricksetGoal = merger.update_list()
            self.sort_goallist()

    def print_goallist(self):
        print(self.bricksetGoal)

    def sort_goallist(self):
        self.bricksetGoal = sorted(self.bricksetGoal, key=lambda k: k['PartID']) 
    
