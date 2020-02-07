import xml.etree.ElementTree as ET
from quik import FileLoader

def gen():
    xmlTree = ET.parse('../UserFiles/hw_conf.xml')
    root = xmlTree.getroot()
    number_of_node = int(root[1][0].text) * int(root[1][1].text)

    i = 0
    for i in range(number_of_node):
        loader = FileLoader('')
        template = loader.load_template('Templates/makefile')
        with open('../packet_transaction_lib/inc/header_' + str(i) + '/makefile', 'w',
                  encoding='utf-8') as f:
            f.write(template.render(locals()))