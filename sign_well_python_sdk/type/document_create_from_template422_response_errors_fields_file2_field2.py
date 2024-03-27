# coding: utf-8

"""
    Resources and endpoints

    When I started SignWell in 2019, I saw there was a need for an alternative to the hard-to-use and expensive e-signature software already out there. Documents can be complicated enough, but getting a document signed shouldn't be complicated too.  At SignWell, we pride ourselves not only on the ease and affordability of our e-signature process but also on our personalized and industry-leading customer support — whether it's for individual use or larger team accounts, SignWell is here to help you feel comfortable and confident getting your documents signed.  The SignWell mission? Simplify how documents get signed for millions of people and businesses. We're excited to help you continue to move toward the future of paperless document signing.  Ruben Gamez Founder, SignWell

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from sign_well_python_sdk.type.document_create_from_template422_response_errors_fields_file2_field2_date_format import DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field2DateFormat
from sign_well_python_sdk.type.document_create_from_template422_response_errors_fields_file2_field2_fixed_width import DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field2FixedWidth
from sign_well_python_sdk.type.document_create_from_template422_response_errors_fields_file2_field2_label import DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field2Label
from sign_well_python_sdk.type.document_create_from_template422_response_errors_fields_file2_field2_validation import DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field2Validation

class RequiredDocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field2(TypedDict):
    pass

class OptionalDocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field2(TypedDict, total=False):
    invalid_date_value: str

    fixed_width: DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field2FixedWidth

    validation: DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field2Validation

    label: DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field2Label

    date_format: DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field2DateFormat

class DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field2(RequiredDocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field2, OptionalDocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field2):
    pass
