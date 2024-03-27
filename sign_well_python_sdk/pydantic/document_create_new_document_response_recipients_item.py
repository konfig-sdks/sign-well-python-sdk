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

from sign_well_python_sdk.pydantic.document_create_new_document_response_recipients_item_attachment_requests import DocumentCreateNewDocumentResponseRecipientsItemAttachmentRequests

class DocumentCreateNewDocumentResponseRecipientsItem(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    attachment_requests: typing.Optional[DocumentCreateNewDocumentResponseRecipientsItemAttachmentRequests] = Field(None, alias='attachment_requests')

    email: typing.Optional[str] = Field(None, alias='email')

    message: typing.Optional[typing.Optional[str]] = Field(None, alias='message')

    name: typing.Optional[str] = Field(None, alias='name')

    passcode: typing.Optional[typing.Optional[str]] = Field(None, alias='passcode')

    send_email_delay: typing.Optional[typing.Union[int, float]] = Field(None, alias='send_email_delay')

    signing_order: typing.Optional[typing.Union[int, float]] = Field(None, alias='signing_order')

    status: typing.Optional[str] = Field(None, alias='status')

    subject: typing.Optional[typing.Optional[str]] = Field(None, alias='subject')

    bounced: typing.Optional[typing.Optional[str]] = Field(None, alias='bounced')

    bounced_details: typing.Optional[typing.Optional[str]] = Field(None, alias='bounced_details')

    send_email: typing.Optional[bool] = Field(None, alias='send_email')

    signing_url: typing.Optional[str] = Field(None, alias='signing_url')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
