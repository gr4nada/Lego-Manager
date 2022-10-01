from src.set_manager import LegoManager

def main():
    manager = LegoManager('F:\\Lego\\')
    manager.read_data()
    manager.print_goallist()

if __name__ == '__main__':
    main()
