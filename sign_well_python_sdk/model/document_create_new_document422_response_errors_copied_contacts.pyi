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


class DocumentCreateNewDocument422ResponseErrorsCopiedContacts(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def copied_contact_1() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsCopiedContactsCopiedContact1']:
                return DocumentCreateNewDocument422ResponseErrorsCopiedContactsCopiedContact1
        
            @staticmethod
            def copied_contact_2() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsCopiedContactsCopiedContact2']:
                return DocumentCreateNewDocument422ResponseErrorsCopiedContactsCopiedContact2
            __annotations__ = {
                "copied_contact_1": copied_contact_1,
                "copied_contact_2": copied_contact_2,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copied_contact_1"]) -> 'DocumentCreateNewDocument422ResponseErrorsCopiedContactsCopiedContact1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copied_contact_2"]) -> 'DocumentCreateNewDocument422ResponseErrorsCopiedContactsCopiedContact2': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["copied_contact_1", "copied_contact_2", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copied_contact_1"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsCopiedContactsCopiedContact1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copied_contact_2"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsCopiedContactsCopiedContact2', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["copied_contact_1", "copied_contact_2", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        copied_contact_1: typing.Union['DocumentCreateNewDocument422ResponseErrorsCopiedContactsCopiedContact1', schemas.Unset] = schemas.unset,
        copied_contact_2: typing.Union['DocumentCreateNewDocument422ResponseErrorsCopiedContactsCopiedContact2', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentCreateNewDocument422ResponseErrorsCopiedContacts':
        return super().__new__(
            cls,
            *args,
            copied_contact_1=copied_contact_1,
            copied_contact_2=copied_contact_2,
            _configuration=_configuration,
            **kwargs,
        )

from sign_well_python_sdk.model.document_create_new_document422_response_errors_copied_contacts_copied_contact1 import DocumentCreateNewDocument422ResponseErrorsCopiedContactsCopiedContact1
from sign_well_python_sdk.model.document_create_new_document422_response_errors_copied_contacts_copied_contact2 import DocumentCreateNewDocument422ResponseErrorsCopiedContactsCopiedContact2
