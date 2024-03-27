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

from sign_well_python_sdk.pydantic.document_update_and_send422_response_errors_decline_redirect_url import DocumentUpdateAndSend422ResponseErrorsDeclineRedirectUrl
from sign_well_python_sdk.pydantic.document_update_and_send422_response_errors_expires_in import DocumentUpdateAndSend422ResponseErrorsExpiresIn
from sign_well_python_sdk.pydantic.document_update_and_send422_response_errors_message import DocumentUpdateAndSend422ResponseErrorsMessage
from sign_well_python_sdk.pydantic.document_update_and_send422_response_errors_metadata import DocumentUpdateAndSend422ResponseErrorsMetadata
from sign_well_python_sdk.pydantic.document_update_and_send422_response_errors_redirect_url import DocumentUpdateAndSend422ResponseErrorsRedirectUrl
from sign_well_python_sdk.pydantic.document_update_and_send422_response_errors_subject import DocumentUpdateAndSend422ResponseErrorsSubject

class DocumentUpdateAndSend422ResponseErrors(BaseModel):
    decline_redirect_url: typing.Optional[DocumentUpdateAndSend422ResponseErrorsDeclineRedirectUrl] = Field(None, alias='decline_redirect_url')

    redirect_url: typing.Optional[DocumentUpdateAndSend422ResponseErrorsRedirectUrl] = Field(None, alias='redirect_url')

    expires_in: typing.Optional[DocumentUpdateAndSend422ResponseErrorsExpiresIn] = Field(None, alias='expires_in')

    metadata: typing.Optional[DocumentUpdateAndSend422ResponseErrorsMetadata] = Field(None, alias='metadata')

    subject: typing.Optional[DocumentUpdateAndSend422ResponseErrorsSubject] = Field(None, alias='subject')

    message: typing.Optional[DocumentUpdateAndSend422ResponseErrorsMessage] = Field(None, alias='message')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
