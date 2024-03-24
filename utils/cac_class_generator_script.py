"""
Script
"""
import re

from lxml import etree

def camel_to_snake(camelcase_str):
    snakecase_str = re.sub(r'(?<=[a-z0-9])([A-Z])', r'_\1', camelcase_str)
    snakecase_str = snakecase_str.lower()
    return snakecase_str


def complex_type_encoder(obj):
    """
    Complex Type to json
    """
    if isinstance(obj, ComplexType):
        return {
            # '__complex_type__': True,
            'name': obj.name,
            'cbc': obj.required,
            'cac': obj.not_required
        }
    raise TypeError(
        f"Object of type {type(obj).__name__} is not JSON serializable")


class Attribute:

    def __init__(self, name: str, min: str, max: str) -> None:
        # cbc = 'cbc:ID' ---> self.name = 'id'
        self.required = False
        self.name = camel_to_snake(name[4:])
        self.param, self.validation = self.get_constructor_param(
            name, min, max)

    def get_constructor_param(self, name: str, min: str, max: str):
        # cbc = 'cbc:SupplyChainActivityTypeCode'
        # cac = 'cac:BuyerCustomerParty'
        class_name = f"{name.replace(':','.')}" if name.startswith(
            'cbc') else f"'{name[4:]}'"
        param_name = camel_to_snake(name[4:])
        validation = ''
        if min == '1' and max == '1':
            self.required = True
            return f"{param_name}:{class_name}", validation
        elif min == '0' and max == '1':
            return f"{param_name}:{class_name}=None", validation
        elif min == '0' and max == 'unbounded':
            return f"{param_name}:List[{class_name}]=None", validation
        elif min == '1' and max == 'unbounded':
            validation = f"\tif not {param_name}:\n\t\t\traise ListMustNotBeEmptyException('{param_name}')"
            return f"{param_name}:List[{class_name}]=None", validation
        else:
            raise Exception("Invalid minOccurs, maxOccurs combination")

    @property
    def assignation(self):
        return f"self.{self.name} = {self.name}"

    def __str__(self) -> str:
        return f"{self.name}\n{self.assignation}\n{self.param}\n{self.validation}"


class ComplexType:
    """
    Represents the complexType XML tag in the UBL-CommonAggregateComponents-2.1.xsd
    It's kind of recursive structure because each element (cac) has a relationship with
    one complexType and each complexType could be related to 0 or more elements (cacs)
    """

    def __init__(self, ct_name) -> None:
        self.name = ct_name
        self.required = []
        self.not_required = []
        self.order_list = []

    def depends_on_cac(self):
        return len(self.not_required) != 0

    def add_attribute(self, attr: Attribute):
        self.order_list.append(attr.name)
        if attr.required:
            self.required.append(attr)
        else:
            self.not_required.append(attr)


# Load the XML file
cac_schema = '../schemes/common/UBL-CommonAggregateComponents-2.1.xsd'
tree = etree.parse(cac_schema)
nsmap = {'xsd': 'http://www.w3.org/2001/XMLSchema'}

xml_elements = tree.xpath("/xsd:schema/xsd:element", namespaces=nsmap)
xml_complex_types = tree.xpath("/xsd:schema/xsd:complexType", namespaces=nsmap)

element_type_mapping = dict()

for xml_element in xml_elements:
    element_type_mapping[xml_element.attrib['name']
                         ] = xml_element.attrib['type']


non_cac_dependant_complex_types = list()
complex_types_dict = dict()

for xml_complex_type in xml_complex_types:
    complex_type = ComplexType(xml_complex_type.attrib['name'])
    for xml_sequence in xml_complex_type.iterchildren():
        for xml_element in xml_sequence.iterchildren():
            name = xml_element.attrib['ref']
            minOccurs = xml_element.attrib['minOccurs']
            maxOccurs = xml_element.attrib['maxOccurs']
            complex_type.add_attribute(Attribute(name, minOccurs, maxOccurs))
    complex_types_dict[complex_type.name] = complex_type

code = "from typing import List\n"
code += "from ublib21.common import cbc\n"
code += "from ublib21.common.cac import *\n"
code += "from ublib21.base import ComplexXMLParseableObject\n\n"
code += "class ListMustNotBeEmptyException(Exception):\n\tpass\n"
for complex_type in complex_types_dict.values():
    code += f"class __{complex_type.name}(ComplexXMLParseableObject):\n"
    for req_attr in complex_type.required:
        code += f"\t{req_attr.name} = None\n"
    for req_attr in complex_type.not_required:
        code += f"\t{req_attr.name} = None\n"
    code += "\torder_list = [\n"
    for element in complex_type.order_list:
        code += f"\t\t'{element}',\n"
    code += "\t]\n"
        
    code += "\tdef __init__(self,"
    for i, req_attr in enumerate(complex_type.required):
        code += f"\t\t{req_attr.param}{',' if (not i==(len(complex_type.required)-1)) or (len(complex_type.not_required)!=0) else '):'}\n"
    for i, req_attr in enumerate(complex_type.not_required):
        code += f"\t\t{req_attr.param}{',' if (not i==(len(complex_type.not_required)-1)) else '):'}\n"

    for req_attr in complex_type.required:
        if req_attr.validation != '':
            code += f"\t{req_attr.validation}\n"
    for req_attr in complex_type.not_required:
        if req_attr.validation != '':
            code += f"\t{req_attr.validation}\n"

    for req_attr in complex_type.required:
        code += f"\t\tself.{req_attr.name} = {req_attr.name}\n"
    for req_attr in complex_type.not_required:
        code += f"\t\tself.{req_attr.name} = {req_attr.name}\n"
    code += '\n'

with open('cac_types.py', "w") as file:
    file.write(code)

code = "from ublib21.common import cac_types\n\n"
for element, complex_type in element_type_mapping.items():
    code += f"class {element}(cac_types.__{complex_type}):\n\tpass\n"

with open('cac.py', "w") as file:
    file.write(code)