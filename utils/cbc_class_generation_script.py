from lxml import etree

cbc_schema = '../schemes/common/UBL-CommonBasicComponents-2.1.xsd'
cbc_python_filename = 'cbc.py'
cbc_tree = etree.parse(cbc_schema)

nsmap = {'xsd': 'http://www.w3.org/2001/XMLSchema'}

complex_type_elements = cbc_tree.xpath('//xsd:complexType', namespaces=nsmap)
extension_elements = cbc_tree.xpath('//xsd:extension', namespaces=nsmap)
file_content = "from ublib21.common.udt import *\n\n"

for i in range(len(complex_type_elements)):
    class_name = complex_type_elements[i].attrib['name'][:-4]
    base_class_name = extension_elements[i].attrib['base'].replace('udt:','')
    file_content += f"class {class_name}({base_class_name}):\n\tpass\n\n\n"

with open(cbc_python_filename, "w") as file:
    file.write(file_content)
