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


class DocumentCreateFromTemplate422ResponseErrorsFieldsFile2(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def field_1() -> typing.Type['DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field1']:
                return DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field1
        
            @staticmethod
            def field_2() -> typing.Type['DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field2']:
                return DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field2
        
            @staticmethod
            def field_3() -> typing.Type['DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field3']:
                return DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field3
        
            @staticmethod
            def field_4() -> typing.Type['DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field4']:
                return DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field4
            __annotations__ = {
                "field_1": field_1,
                "field_2": field_2,
                "field_3": field_3,
                "field_4": field_4,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field_1"]) -> 'DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field_2"]) -> 'DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field2': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field_3"]) -> 'DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field3': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field_4"]) -> 'DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field4': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["field_1", "field_2", "field_3", "field_4", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field_1"]) -> typing.Union['DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field_2"]) -> typing.Union['DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field2', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field_3"]) -> typing.Union['DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field3', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field_4"]) -> typing.Union['DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field4', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["field_1", "field_2", "field_3", "field_4", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        field_1: typing.Union['DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field1', schemas.Unset] = schemas.unset,
        field_2: typing.Union['DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field2', schemas.Unset] = schemas.unset,
        field_3: typing.Union['DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field3', schemas.Unset] = schemas.unset,
        field_4: typing.Union['DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field4', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentCreateFromTemplate422ResponseErrorsFieldsFile2':
        return super().__new__(
            cls,
            *args,
            field_1=field_1,
            field_2=field_2,
            field_3=field_3,
            field_4=field_4,
            _configuration=_configuration,
            **kwargs,
        )

from sign_well_python_sdk.model.document_create_from_template422_response_errors_fields_file2_field1 import DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field1
from sign_well_python_sdk.model.document_create_from_template422_response_errors_fields_file2_field2 import DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field2
from sign_well_python_sdk.model.document_create_from_template422_response_errors_fields_file2_field3 import DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field3
from sign_well_python_sdk.model.document_create_from_template422_response_errors_fields_file2_field4 import DocumentCreateFromTemplate422ResponseErrorsFieldsFile2Field4
