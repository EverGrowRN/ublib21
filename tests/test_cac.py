from ublib21.common.cbc import AcceptedVariantsDescription

class TestAcceptedVariantsDescription:

    def test_value(self):
        a = AcceptedVariantsDescription("HOLAS", "es")
        assert str(a) == '<AcceptedVariantsDescription languageID="es">HOLAS</AcceptedVariantsDescription>'