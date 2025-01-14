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


class DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def date_format() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4DateFormat']:
                return DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4DateFormat
        
            @staticmethod
            def fixed_width() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4FixedWidth']:
                return DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4FixedWidth
        
            @staticmethod
            def validation() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4Validation']:
                return DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4Validation
        
            @staticmethod
            def label() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4Label']:
                return DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4Label
        
            @staticmethod
            def lock_sign_date() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4LockSignDate']:
                return DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4LockSignDate
            __annotations__ = {
                "date_format": date_format,
                "fixed_width": fixed_width,
                "validation": validation,
                "label": label,
                "lock_sign_date": lock_sign_date,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_format"]) -> 'DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4DateFormat': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fixed_width"]) -> 'DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4FixedWidth': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["validation"]) -> 'DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4Validation': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> 'DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4Label': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lock_sign_date"]) -> 'DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4LockSignDate': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["date_format", "fixed_width", "validation", "label", "lock_sign_date", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_format"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4DateFormat', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fixed_width"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4FixedWidth', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["validation"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4Validation', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4Label', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lock_sign_date"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4LockSignDate', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["date_format", "fixed_width", "validation", "label", "lock_sign_date", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        date_format: typing.Union['DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4DateFormat', schemas.Unset] = schemas.unset,
        fixed_width: typing.Union['DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4FixedWidth', schemas.Unset] = schemas.unset,
        validation: typing.Union['DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4Validation', schemas.Unset] = schemas.unset,
        label: typing.Union['DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4Label', schemas.Unset] = schemas.unset,
        lock_sign_date: typing.Union['DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4LockSignDate', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4':
        return super().__new__(
            cls,
            *args,
            date_format=date_format,
            fixed_width=fixed_width,
            validation=validation,
            label=label,
            lock_sign_date=lock_sign_date,
            _configuration=_configuration,
            **kwargs,
        )

from sign_well_python_sdk.model.document_create_new_document422_response_errors_fields_file2_field4_date_format import DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4DateFormat
from sign_well_python_sdk.model.document_create_new_document422_response_errors_fields_file2_field4_fixed_width import DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4FixedWidth
from sign_well_python_sdk.model.document_create_new_document422_response_errors_fields_file2_field4_label import DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4Label
from sign_well_python_sdk.model.document_create_new_document422_response_errors_fields_file2_field4_lock_sign_date import DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4LockSignDate
from sign_well_python_sdk.model.document_create_new_document422_response_errors_fields_file2_field4_validation import DocumentCreateNewDocument422ResponseErrorsFieldsFile2Field4Validation
