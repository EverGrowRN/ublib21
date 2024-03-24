"""
UBL Implementation Common Classes
"""


from ublib21.exceptions import MissingAttributeNamesMappingException


class BasicXMLParseableObject:
    prefix = None
    tag = None
    attr_names_mapping = None

    def __init__(self, value) -> None:
        self.value = value
        if self.attr_names_mapping is None:
            raise MissingAttributeNamesMappingException(
                f"{self.__class__.__name__}")

    def __str__(self):
        attrs = self.build_attr_string()
        tag = self.get_tag()
        xml = f"<{tag}{attrs}>{self.get_value()}</{tag}>"
        return xml

    def get_value(self):
        return self.value

    def build_attr_string(self):
        attr_string = ''
        for attr, string_attr in self.attr_names_mapping.items():
            value = getattr(self, attr, '')
            attr_string += value and f' {string_attr}="{value}"' or ''
        return attr_string

    def get_name(self):
        # If a tag was set, return that
        if self.tag is not None:
            return self.tag
        # Otherwise, build a tag from class name
        if self.__class__.__name__.endswith('Type'):
            # Removes 'Type' from class name
            return self.__class__.__name__[:-4]

        return self.__class__.__name__

    def get_tag(self):
        return f'{self.prefix}:{self.get_name()}' if self.prefix else f'{self.get_name()}'


class ComplexXMLParseableObject:
    prefix = None
    tag = None
    order_list = []

    def __str__(self):
        tag = self.get_tag()
        xml = f"<{tag}>{self.get_value()}</{tag}>"
        return xml

    def get_name(self):
        # If a tag was set, return that
        if self.tag is not None:
            return self.tag
        # Otherwise, build a tag from class name
        if self.__class__.__name__.endswith('Type'):
            # Removes 'Type' from class name
            return self.__class__.__name__[:-4]

        return self.__class__.__name__

    def get_tag(self):
        return f'{self.prefix}:{self.get_name()}' if self.prefix else f'{self.get_name()}'

    def get_value(self):
        xml = ''
        attrs = vars(self)

        for attr in self.order_list:
            value = attrs[attr]
            if value is not None:
                xml += f"{value}"
        return xml
