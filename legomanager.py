from src.set_manager import LegoManager
import pandas as pd

def get_images(bricks):
    for brick in bricks:
        brick['image'] = f'https://www.lego.com/cdn/product-assets/element.img.lod5photo.192x192/{brick["PartID"]}.jpg'

def path_to_image_html(path):
    return "<img src='"+ path + "' width='192'>"

def create_html_table(bricks):
    bricks_table = pd.DataFrame.from_records(bricks)
    html = bricks_table.to_html(escape=False ,formatters=dict(image=path_to_image_html))
    html = "<html>"+ html + "</html>"
    return html

def create_html_file_output(html):
    file = open("output\\index.html", "w")
    file.write(html)
    file.close()

def main():
    # csv Brickset inventories folder
    manager = LegoManager('F:\\Lego\\')
    manager.read_data()
    bricks = manager.get_bricksetGoal()
    get_images(bricks)
    html = create_html_table(bricks)
    create_html_file_output(html)

if __name__ == '__main__':
    main()
