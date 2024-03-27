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


class DocumentTemplateResponseFieldsItemItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "x",
            "y",
            "page",
        }
        
        class properties:
            x = schemas.Float32Schema
            y = schemas.Float32Schema
            page = schemas.IntSchema
        
            @staticmethod
            def recipient() -> typing.Type['DocumentTemplateResponseFieldsItemItemRecipient']:
                return DocumentTemplateResponseFieldsItemItemRecipient
            api_id = schemas.UUIDSchema
            date_format = schemas.StrSchema
            fixed_width = schemas.BoolSchema
            label = schemas.StrSchema
            lock_sign_date = schemas.BoolSchema
            required = schemas.BoolSchema
            type = schemas.StrSchema
            validation = schemas.StrSchema
            value = schemas.AnyTypeSchema
            __annotations__ = {
                "x": x,
                "y": y,
                "page": page,
                "recipient": recipient,
                "api_id": api_id,
                "date_format": date_format,
                "fixed_width": fixed_width,
                "label": label,
                "lock_sign_date": lock_sign_date,
                "required": required,
                "type": type,
                "validation": validation,
                "value": value,
            }
    
    x: MetaOapg.properties.x
    y: MetaOapg.properties.y
    page: MetaOapg.properties.page
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["x"]) -> MetaOapg.properties.x: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["y"]) -> MetaOapg.properties.y: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recipient"]) -> 'DocumentTemplateResponseFieldsItemItemRecipient': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["api_id"]) -> MetaOapg.properties.api_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_format"]) -> MetaOapg.properties.date_format: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fixed_width"]) -> MetaOapg.properties.fixed_width: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lock_sign_date"]) -> MetaOapg.properties.lock_sign_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["validation"]) -> MetaOapg.properties.validation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["x", "y", "page", "recipient", "api_id", "date_format", "fixed_width", "label", "lock_sign_date", "required", "type", "validation", "value", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["x"]) -> MetaOapg.properties.x: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["y"]) -> MetaOapg.properties.y: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recipient"]) -> typing.Union['DocumentTemplateResponseFieldsItemItemRecipient', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["api_id"]) -> typing.Union[MetaOapg.properties.api_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_format"]) -> typing.Union[MetaOapg.properties.date_format, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fixed_width"]) -> typing.Union[MetaOapg.properties.fixed_width, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union[MetaOapg.properties.label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lock_sign_date"]) -> typing.Union[MetaOapg.properties.lock_sign_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["required"]) -> typing.Union[MetaOapg.properties.required, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["validation"]) -> typing.Union[MetaOapg.properties.validation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["x", "y", "page", "recipient", "api_id", "date_format", "fixed_width", "label", "lock_sign_date", "required", "type", "validation", "value", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        x: typing.Union[MetaOapg.properties.x, decimal.Decimal, int, float, ],
        y: typing.Union[MetaOapg.properties.y, decimal.Decimal, int, float, ],
        page: typing.Union[MetaOapg.properties.page, decimal.Decimal, int, ],
        recipient: typing.Union['DocumentTemplateResponseFieldsItemItemRecipient', schemas.Unset] = schemas.unset,
        api_id: typing.Union[MetaOapg.properties.api_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        date_format: typing.Union[MetaOapg.properties.date_format, str, schemas.Unset] = schemas.unset,
        fixed_width: typing.Union[MetaOapg.properties.fixed_width, bool, schemas.Unset] = schemas.unset,
        label: typing.Union[MetaOapg.properties.label, str, schemas.Unset] = schemas.unset,
        lock_sign_date: typing.Union[MetaOapg.properties.lock_sign_date, bool, schemas.Unset] = schemas.unset,
        required: typing.Union[MetaOapg.properties.required, bool, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        validation: typing.Union[MetaOapg.properties.validation, str, schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentTemplateResponseFieldsItemItem':
        return super().__new__(
            cls,
            *args,
            x=x,
            y=y,
            page=page,
            recipient=recipient,
            api_id=api_id,
            date_format=date_format,
            fixed_width=fixed_width,
            label=label,
            lock_sign_date=lock_sign_date,
            required=required,
            type=type,
            validation=validation,
            value=value,
            _configuration=_configuration,
            **kwargs,
        )

from sign_well_python_sdk.model.document_template_response_fields_item_item_recipient import DocumentTemplateResponseFieldsItemItemRecipient
