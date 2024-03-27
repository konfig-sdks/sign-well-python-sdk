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

from sign_well_python_sdk.pydantic.document_create_new_document422_response_errors_api_application_id import DocumentCreateNewDocument422ResponseErrorsApiApplicationId
from sign_well_python_sdk.pydantic.document_create_new_document422_response_errors_attachment_requests import DocumentCreateNewDocument422ResponseErrorsAttachmentRequests
from sign_well_python_sdk.pydantic.document_create_new_document422_response_errors_copied_contacts import DocumentCreateNewDocument422ResponseErrorsCopiedContacts
from sign_well_python_sdk.pydantic.document_create_new_document422_response_errors_custom_requester_email import DocumentCreateNewDocument422ResponseErrorsCustomRequesterEmail
from sign_well_python_sdk.pydantic.document_create_new_document422_response_errors_custom_requester_name import DocumentCreateNewDocument422ResponseErrorsCustomRequesterName
from sign_well_python_sdk.pydantic.document_create_new_document422_response_errors_decline_redirect_url import DocumentCreateNewDocument422ResponseErrorsDeclineRedirectUrl
from sign_well_python_sdk.pydantic.document_create_new_document422_response_errors_expires_in import DocumentCreateNewDocument422ResponseErrorsExpiresIn
from sign_well_python_sdk.pydantic.document_create_new_document422_response_errors_fields import DocumentCreateNewDocument422ResponseErrorsFields
from sign_well_python_sdk.pydantic.document_create_new_document422_response_errors_files import DocumentCreateNewDocument422ResponseErrorsFiles
from sign_well_python_sdk.pydantic.document_create_new_document422_response_errors_message import DocumentCreateNewDocument422ResponseErrorsMessage
from sign_well_python_sdk.pydantic.document_create_new_document422_response_errors_metadata import DocumentCreateNewDocument422ResponseErrorsMetadata
from sign_well_python_sdk.pydantic.document_create_new_document422_response_errors_name import DocumentCreateNewDocument422ResponseErrorsName
from sign_well_python_sdk.pydantic.document_create_new_document422_response_errors_recipients import DocumentCreateNewDocument422ResponseErrorsRecipients
from sign_well_python_sdk.pydantic.document_create_new_document422_response_errors_redirect_url import DocumentCreateNewDocument422ResponseErrorsRedirectUrl
from sign_well_python_sdk.pydantic.document_create_new_document422_response_errors_subject import DocumentCreateNewDocument422ResponseErrorsSubject

class DocumentCreateNewDocument422ResponseErrors(BaseModel):
    name: typing.Optional[DocumentCreateNewDocument422ResponseErrorsName] = Field(None, alias='name')

    custom_requester_email: typing.Optional[DocumentCreateNewDocument422ResponseErrorsCustomRequesterEmail] = Field(None, alias='custom_requester_email')

    custom_requester_name: typing.Optional[DocumentCreateNewDocument422ResponseErrorsCustomRequesterName] = Field(None, alias='custom_requester_name')

    decline_redirect_url: typing.Optional[DocumentCreateNewDocument422ResponseErrorsDeclineRedirectUrl] = Field(None, alias='decline_redirect_url')

    redirect_url: typing.Optional[DocumentCreateNewDocument422ResponseErrorsRedirectUrl] = Field(None, alias='redirect_url')

    expires_in: typing.Optional[DocumentCreateNewDocument422ResponseErrorsExpiresIn] = Field(None, alias='expires_in')

    metadata: typing.Optional[DocumentCreateNewDocument422ResponseErrorsMetadata] = Field(None, alias='metadata')

    api_application_id: typing.Optional[DocumentCreateNewDocument422ResponseErrorsApiApplicationId] = Field(None, alias='api_application_id')

    subject: typing.Optional[DocumentCreateNewDocument422ResponseErrorsSubject] = Field(None, alias='subject')

    message: typing.Optional[DocumentCreateNewDocument422ResponseErrorsMessage] = Field(None, alias='message')

    recipients: typing.Optional[DocumentCreateNewDocument422ResponseErrorsRecipients] = Field(None, alias='recipients')

    copied_contacts: typing.Optional[DocumentCreateNewDocument422ResponseErrorsCopiedContacts] = Field(None, alias='copied_contacts')

    attachment_requests: typing.Optional[DocumentCreateNewDocument422ResponseErrorsAttachmentRequests] = Field(None, alias='attachment_requests')

    fields: typing.Optional[DocumentCreateNewDocument422ResponseErrorsFields] = Field(None, alias='fields')

    files: typing.Optional[DocumentCreateNewDocument422ResponseErrorsFiles] = Field(None, alias='files')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
