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

from sign_well_python_sdk.pydantic.document_response_fields_item_item_recipient import DocumentResponseFieldsItemItemRecipient

class DocumentResponseFieldsItemItem(BaseModel):
    x: typing.Union[int, float] = Field(alias='x')

    y: typing.Union[int, float] = Field(alias='y')

    page: int = Field(alias='page')

    recipient: typing.Optional[DocumentResponseFieldsItemItemRecipient] = Field(None, alias='recipient')

    api_id: typing.Optional[str] = Field(None, alias='api_id')

    date_format: typing.Optional[str] = Field(None, alias='date_format')

    fixed_width: typing.Optional[bool] = Field(None, alias='fixed_width')

    label: typing.Optional[str] = Field(None, alias='label')

    lock_sign_date: typing.Optional[bool] = Field(None, alias='lock_sign_date')

    required: typing.Optional[bool] = Field(None, alias='required')

    type: typing.Optional[str] = Field(None, alias='type')

    validation: typing.Optional[str] = Field(None, alias='validation')

    value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='value')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )