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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from sign_well_python_sdk.pydantic.document_create_new_document422_response_errors_fields_file1_field1_date_format import DocumentCreateNewDocument422ResponseErrorsFieldsFile1Field1DateFormat
from sign_well_python_sdk.pydantic.document_create_new_document422_response_errors_fields_file1_field1_lock_sign_date import DocumentCreateNewDocument422ResponseErrorsFieldsFile1Field1LockSignDate

class DocumentCreateNewDocument422ResponseErrorsFieldsFile1Field1(BaseModel):
    date_format: typing.Optional[DocumentCreateNewDocument422ResponseErrorsFieldsFile1Field1DateFormat] = Field(None, alias='date_format')

    lock_sign_date: typing.Optional[DocumentCreateNewDocument422ResponseErrorsFieldsFile1Field1LockSignDate] = Field(None, alias='lock_sign_date')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
