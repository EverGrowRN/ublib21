"""
CCTS Core Component Type Schema Module
"""

from ublib21.base import UBLParseableObject

class AmountType(UBLParseableObject):
    """
    A number of monetary units specified in a currency where the unit of the 
    currency is explicit or implied.
    """

    tag = 'Amount'
    attr_names_mapping = {
        'currency_id': 'currencyID',
        'currency_code_list_version_id': 'currencyCodeListVersionID'
    }

    def __init__(self, value:float, currency_id:str=None, 
                 currency_code_list_version_id:str=None):
        """
        :param float value: The amount itself.
        :param str currency_id: The currency of the amount
        :param str currency_code_list_version_id: The VersionID of the 
        UN/ECE Rec9 code list
        """
        super().__init__(value)
        # TODO: Validate attributes
        self.currency_id = currency_id
        self.currency_code_list_version_id = currency_code_list_version_id
    

class BinaryObjectType(UBLParseableObject):
    """
    A set of finite-length sequences of binary octets.
    """
    tag = 'BinaryObject'

    attr_names_mapping = {
        "format": "format",
        "mime_code": "mimeCode",
        "encoding_code": "encodingCode",
        "character_set_code": "characterSetCode",
        "uri": "uri",
        "filename": "filename"
    }

    def __init__(self, value, format_=None, mime_code=None, encoding=None, 
                 character_set_code=None, uri=None, filename=None):
        super().__init__(value)
        # TODO: Validate attributes
        self.format = format_
        self.mime_code = mime_code
        self.encoding_code = encoding
        self.character_set_code = character_set_code
        self.uri = uri
        self.filename = filename


class CodeType(UBLParseableObject):
    """
    A character string (letters, figures, or symbols) that for brevity and/or 
    languange independence may be used to represent or replace a definitive value 
    or text of an attribute together with relevant supplementary information.
    """

    tag = 'Code'

    attr_names_mapping = {
        "list_id": "listID",
        "list_agency_id": "listAgencyID",
        "list_agency_name": "listAgencyName",
        "list_name": "listName",
        "list_version_id": "listVersionID",
        "name": "name",
        "language_id": "languageID",
        "list_uri": "listURI",
        "list_scheme_uri": "listSchemeURI"
    }

    def __init__(self,value, list_id=None, list_agency_id=None, list_agency_name=None,list_name=None, 
                 list_version_id=None,name=None,language_id=None, list_uri=None, list_scheme_uri=None):
        super().__init__(value)
      
        self.list_id =  list_id
        self.list_agency_id = list_agency_id
        self.list_agency_name = list_agency_name
        self.list_name = list_name
        self.list_name = list_name
        self.list_version_id = list_version_id
        self.name = name
        self.language_id = language_id
        self.list_uri = list_uri
        self.list_scheme_uri = list_scheme_uri
