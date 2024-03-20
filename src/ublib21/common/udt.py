"""
This schema fragment implements UBL unqualified datatypes using core
component types with all supplementary components as described in
CCTS 2.01 http://www.unece.org/cefact/ebxml/CCTS_V2-01_Final.pdf tables
8-1, 8-2 and 8-3.
"""

from ublib21.common.ccts_cct import AmountType as AmountType_
from ublib21.common.ccts_cct import BinaryObjectType as BinaryObjectType_

class AmountType(AmountType_):
    """
    A number of monetary units specified using a given unit of currency.
    """
    def __init__(self, value: float, currency_id: str, currency_code_list_version_id: str = None):
        super().__init__(value, currency_id, currency_code_list_version_id)


class BinaryObjectType(BinaryObjectType_):
    """
    A set of finite-length sequences of binary octets.
    """
    def __init__(self, value, mime_code, format_=None, encoding=None, 
                 character_set_code=None, uri=None, filename=None):
        super().__init__(value, mime_code, format_,  encoding, character_set_code, uri, filename)


class GraphicType(BinaryObjectType):
    """
    A diagram, graph, mathematical curve, or similar representation.
    """
    pass
