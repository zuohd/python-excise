from xml.etree import ElementTree as ET
from xml.dom import minidom

root = ET.Element('level1', {"age": "1"})
son = ET.SubElement(root, "level2", {"age": "2"})
ET.SubElement(son, "level3", {"age": "3"})
# tree=ET.ElementTree(root)
# tree.write("abc.xml",encoding="utf-8",xml_declaration=True,short_empty_elements=False)

def pretify(root):
    rough_string=ET.tostring(root,"utf-8")
    reparsed=minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

new_str=pretify(root)
f=open("new_out.xml","w")
f.write(new_str)
f.close()
