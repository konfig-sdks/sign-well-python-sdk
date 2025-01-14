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


class DocumentUpdateAndSend422ResponseErrors(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def decline_redirect_url() -> typing.Type['DocumentUpdateAndSend422ResponseErrorsDeclineRedirectUrl']:
                return DocumentUpdateAndSend422ResponseErrorsDeclineRedirectUrl
        
            @staticmethod
            def redirect_url() -> typing.Type['DocumentUpdateAndSend422ResponseErrorsRedirectUrl']:
                return DocumentUpdateAndSend422ResponseErrorsRedirectUrl
        
            @staticmethod
            def expires_in() -> typing.Type['DocumentUpdateAndSend422ResponseErrorsExpiresIn']:
                return DocumentUpdateAndSend422ResponseErrorsExpiresIn
        
            @staticmethod
            def metadata() -> typing.Type['DocumentUpdateAndSend422ResponseErrorsMetadata']:
                return DocumentUpdateAndSend422ResponseErrorsMetadata
        
            @staticmethod
            def subject() -> typing.Type['DocumentUpdateAndSend422ResponseErrorsSubject']:
                return DocumentUpdateAndSend422ResponseErrorsSubject
        
            @staticmethod
            def message() -> typing.Type['DocumentUpdateAndSend422ResponseErrorsMessage']:
                return DocumentUpdateAndSend422ResponseErrorsMessage
            __annotations__ = {
                "decline_redirect_url": decline_redirect_url,
                "redirect_url": redirect_url,
                "expires_in": expires_in,
                "metadata": metadata,
                "subject": subject,
                "message": message,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["decline_redirect_url"]) -> 'DocumentUpdateAndSend422ResponseErrorsDeclineRedirectUrl': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirect_url"]) -> 'DocumentUpdateAndSend422ResponseErrorsRedirectUrl': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expires_in"]) -> 'DocumentUpdateAndSend422ResponseErrorsExpiresIn': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'DocumentUpdateAndSend422ResponseErrorsMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subject"]) -> 'DocumentUpdateAndSend422ResponseErrorsSubject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> 'DocumentUpdateAndSend422ResponseErrorsMessage': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["decline_redirect_url", "redirect_url", "expires_in", "metadata", "subject", "message", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["decline_redirect_url"]) -> typing.Union['DocumentUpdateAndSend422ResponseErrorsDeclineRedirectUrl', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirect_url"]) -> typing.Union['DocumentUpdateAndSend422ResponseErrorsRedirectUrl', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expires_in"]) -> typing.Union['DocumentUpdateAndSend422ResponseErrorsExpiresIn', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['DocumentUpdateAndSend422ResponseErrorsMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subject"]) -> typing.Union['DocumentUpdateAndSend422ResponseErrorsSubject', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union['DocumentUpdateAndSend422ResponseErrorsMessage', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["decline_redirect_url", "redirect_url", "expires_in", "metadata", "subject", "message", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        decline_redirect_url: typing.Union['DocumentUpdateAndSend422ResponseErrorsDeclineRedirectUrl', schemas.Unset] = schemas.unset,
        redirect_url: typing.Union['DocumentUpdateAndSend422ResponseErrorsRedirectUrl', schemas.Unset] = schemas.unset,
        expires_in: typing.Union['DocumentUpdateAndSend422ResponseErrorsExpiresIn', schemas.Unset] = schemas.unset,
        metadata: typing.Union['DocumentUpdateAndSend422ResponseErrorsMetadata', schemas.Unset] = schemas.unset,
        subject: typing.Union['DocumentUpdateAndSend422ResponseErrorsSubject', schemas.Unset] = schemas.unset,
        message: typing.Union['DocumentUpdateAndSend422ResponseErrorsMessage', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentUpdateAndSend422ResponseErrors':
        return super().__new__(
            cls,
            *args,
            decline_redirect_url=decline_redirect_url,
            redirect_url=redirect_url,
            expires_in=expires_in,
            metadata=metadata,
            subject=subject,
            message=message,
            _configuration=_configuration,
            **kwargs,
        )

from sign_well_python_sdk.model.document_update_and_send422_response_errors_decline_redirect_url import DocumentUpdateAndSend422ResponseErrorsDeclineRedirectUrl
from sign_well_python_sdk.model.document_update_and_send422_response_errors_expires_in import DocumentUpdateAndSend422ResponseErrorsExpiresIn
from sign_well_python_sdk.model.document_update_and_send422_response_errors_message import DocumentUpdateAndSend422ResponseErrorsMessage
from sign_well_python_sdk.model.document_update_and_send422_response_errors_metadata import DocumentUpdateAndSend422ResponseErrorsMetadata
from sign_well_python_sdk.model.document_update_and_send422_response_errors_redirect_url import DocumentUpdateAndSend422ResponseErrorsRedirectUrl
from sign_well_python_sdk.model.document_update_and_send422_response_errors_subject import DocumentUpdateAndSend422ResponseErrorsSubject
