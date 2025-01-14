# coding: utf-8

"""
    Resources and endpoints

    When I started SignWell in 2019, I saw there was a need for an alternative to the hard-to-use and expensive e-signature software already out there. Documents can be complicated enough, but getting a document signed shouldn't be complicated too.  At SignWell, we pride ourselves not only on the ease and affordability of our e-signature process but also on our personalized and industry-leading customer support — whether it's for individual use or larger team accounts, SignWell is here to help you feel comfortable and confident getting your documents signed.  The SignWell mission? Simplify how documents get signed for millions of people and businesses. We're excited to help you continue to move toward the future of paperless document signing.  Ruben Gamez Founder, SignWell

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from sign_well_python_sdk import schemas  # noqa: F401


class DocumentCreateNewDocument422ResponseErrors(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def name() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsName']:
                return DocumentCreateNewDocument422ResponseErrorsName
        
            @staticmethod
            def custom_requester_email() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsCustomRequesterEmail']:
                return DocumentCreateNewDocument422ResponseErrorsCustomRequesterEmail
        
            @staticmethod
            def custom_requester_name() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsCustomRequesterName']:
                return DocumentCreateNewDocument422ResponseErrorsCustomRequesterName
        
            @staticmethod
            def decline_redirect_url() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsDeclineRedirectUrl']:
                return DocumentCreateNewDocument422ResponseErrorsDeclineRedirectUrl
        
            @staticmethod
            def redirect_url() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsRedirectUrl']:
                return DocumentCreateNewDocument422ResponseErrorsRedirectUrl
        
            @staticmethod
            def expires_in() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsExpiresIn']:
                return DocumentCreateNewDocument422ResponseErrorsExpiresIn
        
            @staticmethod
            def metadata() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsMetadata']:
                return DocumentCreateNewDocument422ResponseErrorsMetadata
        
            @staticmethod
            def api_application_id() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsApiApplicationId']:
                return DocumentCreateNewDocument422ResponseErrorsApiApplicationId
        
            @staticmethod
            def subject() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsSubject']:
                return DocumentCreateNewDocument422ResponseErrorsSubject
        
            @staticmethod
            def message() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsMessage']:
                return DocumentCreateNewDocument422ResponseErrorsMessage
        
            @staticmethod
            def recipients() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsRecipients']:
                return DocumentCreateNewDocument422ResponseErrorsRecipients
        
            @staticmethod
            def copied_contacts() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsCopiedContacts']:
                return DocumentCreateNewDocument422ResponseErrorsCopiedContacts
        
            @staticmethod
            def attachment_requests() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsAttachmentRequests']:
                return DocumentCreateNewDocument422ResponseErrorsAttachmentRequests
        
            @staticmethod
            def fields() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsFields']:
                return DocumentCreateNewDocument422ResponseErrorsFields
        
            @staticmethod
            def files() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsFiles']:
                return DocumentCreateNewDocument422ResponseErrorsFiles
            __annotations__ = {
                "name": name,
                "custom_requester_email": custom_requester_email,
                "custom_requester_name": custom_requester_name,
                "decline_redirect_url": decline_redirect_url,
                "redirect_url": redirect_url,
                "expires_in": expires_in,
                "metadata": metadata,
                "api_application_id": api_application_id,
                "subject": subject,
                "message": message,
                "recipients": recipients,
                "copied_contacts": copied_contacts,
                "attachment_requests": attachment_requests,
                "fields": fields,
                "files": files,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> 'DocumentCreateNewDocument422ResponseErrorsName': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_requester_email"]) -> 'DocumentCreateNewDocument422ResponseErrorsCustomRequesterEmail': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_requester_name"]) -> 'DocumentCreateNewDocument422ResponseErrorsCustomRequesterName': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["decline_redirect_url"]) -> 'DocumentCreateNewDocument422ResponseErrorsDeclineRedirectUrl': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirect_url"]) -> 'DocumentCreateNewDocument422ResponseErrorsRedirectUrl': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expires_in"]) -> 'DocumentCreateNewDocument422ResponseErrorsExpiresIn': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'DocumentCreateNewDocument422ResponseErrorsMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["api_application_id"]) -> 'DocumentCreateNewDocument422ResponseErrorsApiApplicationId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subject"]) -> 'DocumentCreateNewDocument422ResponseErrorsSubject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> 'DocumentCreateNewDocument422ResponseErrorsMessage': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recipients"]) -> 'DocumentCreateNewDocument422ResponseErrorsRecipients': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copied_contacts"]) -> 'DocumentCreateNewDocument422ResponseErrorsCopiedContacts': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachment_requests"]) -> 'DocumentCreateNewDocument422ResponseErrorsAttachmentRequests': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fields"]) -> 'DocumentCreateNewDocument422ResponseErrorsFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["files"]) -> 'DocumentCreateNewDocument422ResponseErrorsFiles': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "custom_requester_email", "custom_requester_name", "decline_redirect_url", "redirect_url", "expires_in", "metadata", "api_application_id", "subject", "message", "recipients", "copied_contacts", "attachment_requests", "fields", "files", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsName', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_requester_email"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsCustomRequesterEmail', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_requester_name"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsCustomRequesterName', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["decline_redirect_url"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsDeclineRedirectUrl', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirect_url"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsRedirectUrl', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expires_in"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsExpiresIn', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["api_application_id"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsApiApplicationId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subject"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsSubject', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsMessage', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recipients"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsRecipients', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copied_contacts"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsCopiedContacts', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachment_requests"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsAttachmentRequests', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fields"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["files"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsFiles', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "custom_requester_email", "custom_requester_name", "decline_redirect_url", "redirect_url", "expires_in", "metadata", "api_application_id", "subject", "message", "recipients", "copied_contacts", "attachment_requests", "fields", "files", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union['DocumentCreateNewDocument422ResponseErrorsName', schemas.Unset] = schemas.unset,
        custom_requester_email: typing.Union['DocumentCreateNewDocument422ResponseErrorsCustomRequesterEmail', schemas.Unset] = schemas.unset,
        custom_requester_name: typing.Union['DocumentCreateNewDocument422ResponseErrorsCustomRequesterName', schemas.Unset] = schemas.unset,
        decline_redirect_url: typing.Union['DocumentCreateNewDocument422ResponseErrorsDeclineRedirectUrl', schemas.Unset] = schemas.unset,
        redirect_url: typing.Union['DocumentCreateNewDocument422ResponseErrorsRedirectUrl', schemas.Unset] = schemas.unset,
        expires_in: typing.Union['DocumentCreateNewDocument422ResponseErrorsExpiresIn', schemas.Unset] = schemas.unset,
        metadata: typing.Union['DocumentCreateNewDocument422ResponseErrorsMetadata', schemas.Unset] = schemas.unset,
        api_application_id: typing.Union['DocumentCreateNewDocument422ResponseErrorsApiApplicationId', schemas.Unset] = schemas.unset,
        subject: typing.Union['DocumentCreateNewDocument422ResponseErrorsSubject', schemas.Unset] = schemas.unset,
        message: typing.Union['DocumentCreateNewDocument422ResponseErrorsMessage', schemas.Unset] = schemas.unset,
        recipients: typing.Union['DocumentCreateNewDocument422ResponseErrorsRecipients', schemas.Unset] = schemas.unset,
        copied_contacts: typing.Union['DocumentCreateNewDocument422ResponseErrorsCopiedContacts', schemas.Unset] = schemas.unset,
        attachment_requests: typing.Union['DocumentCreateNewDocument422ResponseErrorsAttachmentRequests', schemas.Unset] = schemas.unset,
        fields: typing.Union['DocumentCreateNewDocument422ResponseErrorsFields', schemas.Unset] = schemas.unset,
        files: typing.Union['DocumentCreateNewDocument422ResponseErrorsFiles', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentCreateNewDocument422ResponseErrors':
        return super().__new__(
            cls,
            *args,
            name=name,
            custom_requester_email=custom_requester_email,
            custom_requester_name=custom_requester_name,
            decline_redirect_url=decline_redirect_url,
            redirect_url=redirect_url,
            expires_in=expires_in,
            metadata=metadata,
            api_application_id=api_application_id,
            subject=subject,
            message=message,
            recipients=recipients,
            copied_contacts=copied_contacts,
            attachment_requests=attachment_requests,
            fields=fields,
            files=files,
            _configuration=_configuration,
            **kwargs,
        )

from sign_well_python_sdk.model.document_create_new_document422_response_errors_api_application_id import DocumentCreateNewDocument422ResponseErrorsApiApplicationId
from sign_well_python_sdk.model.document_create_new_document422_response_errors_attachment_requests import DocumentCreateNewDocument422ResponseErrorsAttachmentRequests
from sign_well_python_sdk.model.document_create_new_document422_response_errors_copied_contacts import DocumentCreateNewDocument422ResponseErrorsCopiedContacts
from sign_well_python_sdk.model.document_create_new_document422_response_errors_custom_requester_email import DocumentCreateNewDocument422ResponseErrorsCustomRequesterEmail
from sign_well_python_sdk.model.document_create_new_document422_response_errors_custom_requester_name import DocumentCreateNewDocument422ResponseErrorsCustomRequesterName
from sign_well_python_sdk.model.document_create_new_document422_response_errors_decline_redirect_url import DocumentCreateNewDocument422ResponseErrorsDeclineRedirectUrl
from sign_well_python_sdk.model.document_create_new_document422_response_errors_expires_in import DocumentCreateNewDocument422ResponseErrorsExpiresIn
from sign_well_python_sdk.model.document_create_new_document422_response_errors_fields import DocumentCreateNewDocument422ResponseErrorsFields
from sign_well_python_sdk.model.document_create_new_document422_response_errors_files import DocumentCreateNewDocument422ResponseErrorsFiles
from sign_well_python_sdk.model.document_create_new_document422_response_errors_message import DocumentCreateNewDocument422ResponseErrorsMessage
from sign_well_python_sdk.model.document_create_new_document422_response_errors_metadata import DocumentCreateNewDocument422ResponseErrorsMetadata
from sign_well_python_sdk.model.document_create_new_document422_response_errors_name import DocumentCreateNewDocument422ResponseErrorsName
from sign_well_python_sdk.model.document_create_new_document422_response_errors_recipients import DocumentCreateNewDocument422ResponseErrorsRecipients
from sign_well_python_sdk.model.document_create_new_document422_response_errors_redirect_url import DocumentCreateNewDocument422ResponseErrorsRedirectUrl
from sign_well_python_sdk.model.document_create_new_document422_response_errors_subject import DocumentCreateNewDocument422ResponseErrorsSubject
