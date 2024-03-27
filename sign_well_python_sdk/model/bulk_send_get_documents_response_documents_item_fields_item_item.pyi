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


class BulkSendGetDocumentsResponseDocumentsItemFieldsItemItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            api_id = schemas.StrSchema
            height = schemas.StrSchema
            page = schemas.NumberSchema
            required = schemas.BoolSchema
            type = schemas.StrSchema
            
            
            class value(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'value':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            width = schemas.StrSchema
            x = schemas.NumberSchema
            y = schemas.NumberSchema
            recipient_id = schemas.StrSchema
            __annotations__ = {
                "api_id": api_id,
                "height": height,
                "page": page,
                "required": required,
                "type": type,
                "value": value,
                "width": width,
                "x": x,
                "y": y,
                "recipient_id": recipient_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["api_id"]) -> MetaOapg.properties.api_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["height"]) -> MetaOapg.properties.height: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["width"]) -> MetaOapg.properties.width: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["x"]) -> MetaOapg.properties.x: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["y"]) -> MetaOapg.properties.y: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recipient_id"]) -> MetaOapg.properties.recipient_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["api_id", "height", "page", "required", "type", "value", "width", "x", "y", "recipient_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["api_id"]) -> typing.Union[MetaOapg.properties.api_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["height"]) -> typing.Union[MetaOapg.properties.height, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page"]) -> typing.Union[MetaOapg.properties.page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["required"]) -> typing.Union[MetaOapg.properties.required, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["width"]) -> typing.Union[MetaOapg.properties.width, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["x"]) -> typing.Union[MetaOapg.properties.x, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["y"]) -> typing.Union[MetaOapg.properties.y, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recipient_id"]) -> typing.Union[MetaOapg.properties.recipient_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["api_id", "height", "page", "required", "type", "value", "width", "x", "y", "recipient_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        api_id: typing.Union[MetaOapg.properties.api_id, str, schemas.Unset] = schemas.unset,
        height: typing.Union[MetaOapg.properties.height, str, schemas.Unset] = schemas.unset,
        page: typing.Union[MetaOapg.properties.page, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        required: typing.Union[MetaOapg.properties.required, bool, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, None, str, schemas.Unset] = schemas.unset,
        width: typing.Union[MetaOapg.properties.width, str, schemas.Unset] = schemas.unset,
        x: typing.Union[MetaOapg.properties.x, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        y: typing.Union[MetaOapg.properties.y, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        recipient_id: typing.Union[MetaOapg.properties.recipient_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BulkSendGetDocumentsResponseDocumentsItemFieldsItemItem':
        return super().__new__(
            cls,
            *args,
            api_id=api_id,
            height=height,
            page=page,
            required=required,
            type=type,
            value=value,
            width=width,
            x=x,
            y=y,
            recipient_id=recipient_id,
            _configuration=_configuration,
            **kwargs,
        )
