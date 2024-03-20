"""
UBL Implementation Common Classes
"""


class MissingAttributeNamesMappingException(Exception):
    pass


class UBLParseableObject:
    prefix = None
    tag = ''
    attr_names_mapping = None

    def __init__(self, value) -> None:
        self.value = value
        if self.attr_names_mapping is None:
            raise MissingAttributeNamesMappingException(f"{self.__class__.__name__}")

    def __str__(self):
        attrs = self.build_attr_string()
        tag = self.get_tag()
        xml = f"<{tag}{attrs}>{self.value}</{tag}>"
        return xml

    def build_attr_string(self):
        attr_string = ''
        for attr, string_attr in self.attr_names_mapping.items():
            value = getattr(self,attr,'')
            attr_string += value and f' {string_attr}={value}' or ''
        return attr_string
    
    def get_tag(self):
        return f'{self.prefix}:{self.tag}' if self.prefix else f'{self.tag}'
