from lxml import etree

# from ublib21.exceptions import ImproperlyConfiguredException

class ImproperlyConfiguredException(Exception):
    pass


class BaseStringValidator:
    schema_file = None
    
    @classmethod
    def validate(cls, xml):
        if cls.schema_file is None:
            raise ImproperlyConfiguredException("Missing schema file configuration")
        try:
            # Parse XML string
            xml_tree = etree.fromstring(xml)
            
            # Load XSD schema
            with open(cls.schema_file, 'rb') as xsd_file:
                xsd_tree = etree.parse(xsd_file)
            
            # Create XML schema validator
            xml_validator = etree.XMLSchema(xsd_tree)
            
            # Validate XML against XSD
            is_valid = xml_validator.validate(xml_tree)
            
            if is_valid:
                print("XML is valid against the XSD schema.")
            else:
                print("XML is NOT valid against the XSD schema.")
                print(xml_validator.error_log)
        
        except etree.XMLSyntaxError as e:
            print(f"XML syntax error: {e}")
        except etree.XMLSchemaParseError as e:
            print(f"XSD schema parse error: {e}")
        except etree.XMLSchemaValidateError as e:
            print(f"XML validation error: {e}")


class InvoiceValidator(BaseStringValidator):
    schema_file = "./schemes/maindoc/UBL-Invoice-2.1.xsd"

xml_string = '<StockAvailabilityReportLine xmlns="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"><cbc:ID>SHIP_123</cbc:ID><cbc:Quantity>5</cbc:Quantity><Item></Item></StockAvailabilityReportLine>'

BaseStringValidator.validate(xml_string)