import xml.etree.ElementTree as XML

path_string = "./ns0:Document:ns0Folder/ns0:Placemark/ns0:Point/ns0:coordinates"

def row_iter_kml(file_obj):
    ns_map = {
        "ns0": "http://www.opengis.net/kml/2.2",
        "ns1": "http://www.google.com/kml/ext/2.2",
    }
    doc = XML.parse(file_obj)
    print(f'type(doc) - {type(doc)}')
    return (comma_split(coordtinates.text)
           for coordinates in doc.findall(path_string, ns_map))


