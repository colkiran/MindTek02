
import xml.etree.ElementTree as ET

def write_xml(filename, data):
    root = ET.Element('data')
    for item_data in data:
        item = ET.SubElement(root, "item")
        for key, value in item_data.items():
            element = ET.SubElement(item, key)
            element.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)

data = [
    {'name': 'Apple', 'count': 150, 'price': 5000},
    {'name': 'Banana', 'count': 200, 'price': 2350},
    {'name': 'Orange', 'count': 350, 'price': 3500}
]

write_xml("fruits.xml", data)

