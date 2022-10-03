from enum import Enum
import pandas as pd

class Status(Enum):
    ok = 'ok'
    fail = 'fail'

class Brickset(object):

    def __init__(self):
        self.status = Status.ok
        self.table = pd.DataFrame

    def read_data_set(self, path_file:str):
        """ Read a lego dataset 

        Args:
            path (str): path to csv file.
        """
        try:
            self.table = pd.read_csv(path_file, sep=",")
            self.status = Status.ok
        except:
            self.status = Status.fail

    def extract(self)-> list:
        """ Extract BrickSet

        Returns:
            dict: brickSet [{PartId:XX, Quantity:XX},...]
        """
        brickset = pd.DataFrame(self.table, columns = ['PartID','Quantity','PartName'])
        return brickset.to_dict('records')

