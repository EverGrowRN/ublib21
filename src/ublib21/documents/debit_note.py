from typing import List
from ublib21.base import ComplexXMLParseableObject
from ublib21.common import cac, cbc, ext
from ublib21.documents.base import Document

class Debit_note(Document, ComplexXMLParseableObject):
    # Required Attrs
    id = None
    issue_date = None
    accountingsupplier_party = None
    accounting_customer_party = None
    requested_monetary_total = None
    debit_note_line = None #List (at least 1)

    # Optional Attrs
    
    ubl_extensions = None
    ubl_version_id = None
    customization_id = None
    profile_id = None
    profile_execution_id =None
    copy_indicator = None
    uuid = None
    #issue_date None
    issue_time = None
    Note = None # List
    tax_point_date = None
    document_currency_code = None
    tax_currency_code = None
    pricing_currency_code = None
    payment_currency_code = None
    payment_alternative_currency_code = None
    accounting_cost_code = None
    accounting_cost = None
    line_count_numeric = None
    invoice_period = None #List
    discrepancy_response = None #List
    order_reference = None
    billing_reference = None #List 
    despatch_document_reference = None #List 
    receipt_document_reference = None #List 
    statement_document_reference = None #List 
    contract_document_reference = None #List 
    additional_document_reference = None #List 
    signature = None  #List 
    payee_party = None
    buyer_customer_party = None
    seller_supplier_party = None
    tax_representative_party = None
    prepaid_payment =  None #List 
    allowance_charge =  None #List 
    delivery =  None #List 
    delivery_terms =  None #List 
    payment_means =  None #List 
    payment_terms =  None #List 
    tax_exchange_rate =  None
    pricing_exchange_rate =  None
    payment_exchange_rate =  None
    payment_alternative_exchange_rate =  None
    tax_total =  None #List

    order_list = [
        'ubl_extensions' ,
        'ubl_version_id' ,
        'customization_id' ,
        'profile_id' ,
        'profile_execution_i' ,
        'id' ,
        'issue_time' ,
        'Note' ,# List
        'tax_point_date' ,
        'document_currency_code' ,
        'tax_currency_code' ,
        'pricing_currency_code' ,
        'payment_currency_code' ,
        'payment_alternative_currency_code' ,
        'accounting_cost_code' ,
        'accounting_cost' ,
        'line_count_numeric' ,
        'invoice_period', #List
        'discrepancy_response', #List
        'order_reference' ,
        'billing_reference', #List 
        'despatch_document_reference', #List 
        'receipt_document_reference', #List 
        'statement_document_reference', #List 
        'contract_document_reference', #List 
        'additional_document_referen', #List 
        'signature',  #List 
        'accountingsupplier_party' ,
        'accounting_customer_party' ,
        'payee_party' ,
        'buyer_customer_party' ,
        'seller_supplier_party' ,
        'tax_representative_party' ,
        'prepaid_payment' , #List 
        'allowance_charge' , #List 
        'delivery' , #List 
        'delivery_terms', #List 
        'payment_means' , #List 
        'payment_terms' , #List 
        'tax_exchange_rate'  ,
        'pricing_exchange_rate'  ,
        'payment_exchange_rate'  ,
        'payment_alternative_exchange_rate'  ,
        'tax_total' , #List
        'requested_monetary_total' ,
        'debit_note_line' , #List (at least 1)

    ]

    xml_namespaces = [
        'xmlns="urn:oasis:names:specification:ubl:schema:xsd:DebitNote-2"',
        'xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"',
        'xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"',
        'xmlns:ext="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"',
        'xmlns:xsd="http://www.w3.org/2001/XMLSchema"',
    
    ]
    def __init__(self, id_: cbc.ID,
                    issue_date:cbc.IssueDate,
                    accountingsupplier_party:cac.AccountingSupplierParty,
                    accounting_customer_party:cac.AccountingCustomerParty,
                    requested_monetary_total:cac.RequestedMonetaryTotal,
                    debit_note_line:List[cac.DebitNoteLine],
                    ubl_extensions:ext.UBLExtensions = None,
                    ubl_version_id:cbc.UBLVersionID = None,
                    customization_id:cbc.CustomizationID = None,
                    profile_id:cbc.ProfileID = None,
                    profile_execution_id:cbc.ProfileExecutionID =None,
                    copy_indicator:cbc.CopyIndicator = None,
                    uuid:cbc.UUID = None,
                    issue_time:cbc.IssueTime = None,
                    Note:List[cbc.Note] = None, # List
                    tax_point_date:cbc.TaxPointDate = None,
                    document_currency_code:cbc.DocumentCurrencyCode = None,
                    tax_currency_code:cbc.TaxCurrencyCode = None,
                    pricing_currency_code:cbc.PricingCurrencyCode = None,
                    payment_currency_code:cbc.PaymentCurrencyCode = None,
                    payment_alternative_currency_code:cbc.PaymentAlternativeCurrencyCode = None,
                    accounting_cost_code:cbc.AccountingCostCode = None,
                    accounting_cost:cbc.AccountingCost = None,
                    line_count_numeric:cbc.LineCountNumeric = None,
                    invoice_period:List[cac.InvoicePeriod]= None, #List
                    discrepancy_response:List[cac.DiscrepancyResponse] = None, #List
                    order_reference:cac.OrderReference = None,
                    billing_reference:List[cac.BillingReference] = None, #List 
                    despatch_document_reference:List[cac.DespatchDocumentReference] = None, #List 
                    receipt_document_reference:List[cac.ReceiptDocumentReference] = None, #List 
                    statement_document_reference:List[cac.StatementDocumentReference] = None, #List 
                    contract_document_reference:List[cac.ContractDocumentReference] = None, #List 
                    additional_document_reference:List[cac.AdditionalDocumentReference] = None, #List 
                    signature:List[cac.Signature] = None,  #List 
                    payee_party:cac.PayeeParty = None,
                    buyer_customer_party:cac.BuyerCustomerParty = None,
                    seller_supplier_party:cac.SellerSupplierParty = None,
                    tax_representative_party:cac.TaxRepresentativeParty = None,
                    prepaid_payment:List[cac.PrepaidPayment] =  None, #List 
                    allowance_charge:List[cac.AllowanceCharge] =  None, #List 
                    delivery:List[cac.Delivery] =  None, #List 
                    delivery_terms:List[cac.DeliveryTerms] =  None, #List 
                    payment_means:List[cac.PaymentMeans] =  None, #List 
                    payment_terms:List[cac.PaymentTerms] =  None, #List 
                    tax_exchange_rate:cac.TaxExchangeRate =  None,
                    pricing_exchange_rate:cac.PricingExchangeRate =  None,
                    payment_exchange_rate:cac.PaymentExchangeRate =  None,
                    payment_alternative_exchange_rate:cac.PaymentAlternativeExchangeRate =  None,
                    tax_total:List[cac.TaxTotal] =  None) -> None:
            self.id_ = id_
            issue_date =  issue_date
            accountingsupplier_party = accountingsupplier_party
            accounting_customer_party = accounting_customer_party
            requested_monetary_total =  requested_monetary_total
            debit_note_line =  debit_note_line
            ubl_extensions =  ubl_extensions
            ubl_version_id =  ubl_version_id
            customization_id = customization_id
            profile_id = profile_id
            profile_execution_id = profile_execution_id
            copy_indicator = copy_indicator
            uuid = uuid
            issue_time = issue_time
            Note = Note
            tax_point_date = tax_point_date
            document_currency_code = document_currency_code
            tax_currency_code = tax_currency_code
            pricing_currency_code = pricing_currency_code
            payment_currency_code = payment_currency_code
            payment_alternative_currency_code = payment_alternative_currency_code
            accounting_cost_code = accounting_cost_code
            accounting_cost = accounting_cost
            line_count_numeric = line_count_numeric
            invoice_period = invoice_period
            discrepancy_response = discrepancy_response
            order_reference = order_reference
            billing_reference = billing_reference
            despatch_document_reference = despatch_document_reference
            receipt_document_reference = receipt_document_reference
            statement_document_reference = statement_document_reference
            contract_document_reference = contract_document_reference
            additional_document_reference = additional_document_reference
            signature = signature
            payee_party = payee_party
            buyer_customer_party = buyer_customer_party
            seller_supplier_party = seller_supplier_party
            tax_representative_party = tax_representative_party
            prepaid_payment = prepaid_payment
            allowance_charge = allowance_charge
            delivery = delivery
            delivery_terms = delivery_terms
            payment_means = payment_means
            payment_terms = payment_terms
            tax_exchange_rate = tax_exchange_rate
            pricing_exchange_rate = pricing_exchange_rate
            payment_exchange_rate = payment_exchange_rate
            payment_alternative_exchange_rate = payment_alternative_exchange_rate
            tax_total = tax_total

    def __str__(self):
        tag = self.get_tag()
        namespaces = ''
        if self.xml_namespaces is not None:
            for ns in self.xml_namespaces:
                namespaces += f' {ns}'

        return f'<{tag}{namespaces}>{self.get_value()}</{tag}>'

    def to_file(self):
        full_file = f'<?xml version="1.0" encoding="UTF-8" standalone="no"?>{self}'
        return full_file
        
