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


class BulkSendCreateValidationCsv422ResponseErrorsBulkSendCsvItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            row = schemas.NumberSchema
        
            @staticmethod
            def data() -> typing.Type['BulkSendCreateValidationCsv422ResponseErrorsBulkSendCsvItemData']:
                return BulkSendCreateValidationCsv422ResponseErrorsBulkSendCsvItemData
        
            @staticmethod
            def errors() -> typing.Type['BulkSendCreateValidationCsv422ResponseErrorsBulkSendCsvItemErrors']:
                return BulkSendCreateValidationCsv422ResponseErrorsBulkSendCsvItemErrors
            __annotations__ = {
                "row": row,
                "data": data,
                "errors": errors,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["row"]) -> MetaOapg.properties.row: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'BulkSendCreateValidationCsv422ResponseErrorsBulkSendCsvItemData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> 'BulkSendCreateValidationCsv422ResponseErrorsBulkSendCsvItemErrors': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["row", "data", "errors", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["row"]) -> typing.Union[MetaOapg.properties.row, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union['BulkSendCreateValidationCsv422ResponseErrorsBulkSendCsvItemData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> typing.Union['BulkSendCreateValidationCsv422ResponseErrorsBulkSendCsvItemErrors', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["row", "data", "errors", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        row: typing.Union[MetaOapg.properties.row, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        data: typing.Union['BulkSendCreateValidationCsv422ResponseErrorsBulkSendCsvItemData', schemas.Unset] = schemas.unset,
        errors: typing.Union['BulkSendCreateValidationCsv422ResponseErrorsBulkSendCsvItemErrors', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BulkSendCreateValidationCsv422ResponseErrorsBulkSendCsvItem':
        return super().__new__(
            cls,
            *args,
            row=row,
            data=data,
            errors=errors,
            _configuration=_configuration,
            **kwargs,
        )

from sign_well_python_sdk.model.bulk_send_create_validation_csv422_response_errors_bulk_send_csv_item_data import BulkSendCreateValidationCsv422ResponseErrorsBulkSendCsvItemData
from sign_well_python_sdk.model.bulk_send_create_validation_csv422_response_errors_bulk_send_csv_item_errors import BulkSendCreateValidationCsv422ResponseErrorsBulkSendCsvItemErrors
