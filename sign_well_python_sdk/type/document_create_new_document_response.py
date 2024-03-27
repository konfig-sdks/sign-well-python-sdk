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

from sign_well_python_sdk.type.document_create_new_document_response_copied_contacts import DocumentCreateNewDocumentResponseCopiedContacts
from sign_well_python_sdk.type.document_create_new_document_response_fields import DocumentCreateNewDocumentResponseFields
from sign_well_python_sdk.type.document_create_new_document_response_files import DocumentCreateNewDocumentResponseFiles
from sign_well_python_sdk.type.document_create_new_document_response_metadata import DocumentCreateNewDocumentResponseMetadata
from sign_well_python_sdk.type.document_create_new_document_response_recipients import DocumentCreateNewDocumentResponseRecipients

class RequiredDocumentCreateNewDocumentResponse(TypedDict):
    pass

class OptionalDocumentCreateNewDocumentResponse(TypedDict, total=False):
    id: str

    archived: bool

    copied_contacts: DocumentCreateNewDocumentResponseCopiedContacts

    created_at: str

    custom_requester_email: str

    custom_requester_name: str

    decline_redirect_url: str

    embedded_edit_url: str

    embedded_preview_url: typing.Optional[str]

    error_message: typing.Optional[str]

    fields: DocumentCreateNewDocumentResponseFields

    metadata: DocumentCreateNewDocumentResponseMetadata

    name: str

    recipients: DocumentCreateNewDocumentResponseRecipients

    subject: str

    test_mode: bool

    updated_at: str

    decline_message: typing.Optional[str]

    api_application_id: typing.Optional[str]

    allow_decline: bool

    allow_reassign: bool

    apply_signing_order: bool

    embedded_signing: bool

    expires_in: typing.Union[int, float]

    message: str

    reminders: bool

    requester_email_address: str

    redirect_url: str

    status: str

    files: DocumentCreateNewDocumentResponseFiles

class DocumentCreateNewDocumentResponse(RequiredDocumentCreateNewDocumentResponse, OptionalDocumentCreateNewDocumentResponse):
    pass