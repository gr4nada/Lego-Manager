import sys
sys.path.append("..")

from src.set_reader import Brickset, Status

filepath_steam_park = "F:\\Lego\\4. Steam Park\\Brickset-inventory-45024-Steam Park.csv"
filepath_steam_park_wrong = "F:\\Lego\\Steam Park\\Brickset-inventory-45024-Steam Park.csv"

def test_read_data_set():
    steam_park = Brickset()
    steam_park.read_data_set(filepath_steam_park)
    assert steam_park.status == Status.ok

def test_read_data_set_fail():
    steam_park = Brickset()
    steam_park.read_data_set(filepath_steam_park_wrong)
    assert steam_park.status == Status.fail

def test_load_brickset():
    brickset={}
    steam_park = Brickset()
    steam_park.read_data_set(filepath_steam_park)
    brickset = steam_park.extract()
    assert brickset 

