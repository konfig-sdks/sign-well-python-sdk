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


class BulkSendListBulkSendingsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def bulk_sends() -> typing.Type['BulkSendListBulkSendingsResponseBulkSends']:
                return BulkSendListBulkSendingsResponseBulkSends
            current_page = schemas.NumberSchema
            
            
            class next_page(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'next_page':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class previous_page(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'previous_page':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            total_count = schemas.NumberSchema
            total_pages = schemas.NumberSchema
            __annotations__ = {
                "bulk_sends": bulk_sends,
                "current_page": current_page,
                "next_page": next_page,
                "previous_page": previous_page,
                "total_count": total_count,
                "total_pages": total_pages,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bulk_sends"]) -> 'BulkSendListBulkSendingsResponseBulkSends': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_page"]) -> MetaOapg.properties.current_page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_page"]) -> MetaOapg.properties.next_page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["previous_page"]) -> MetaOapg.properties.previous_page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_count"]) -> MetaOapg.properties.total_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_pages"]) -> MetaOapg.properties.total_pages: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bulk_sends", "current_page", "next_page", "previous_page", "total_count", "total_pages", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bulk_sends"]) -> typing.Union['BulkSendListBulkSendingsResponseBulkSends', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_page"]) -> typing.Union[MetaOapg.properties.current_page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_page"]) -> typing.Union[MetaOapg.properties.next_page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["previous_page"]) -> typing.Union[MetaOapg.properties.previous_page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_count"]) -> typing.Union[MetaOapg.properties.total_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_pages"]) -> typing.Union[MetaOapg.properties.total_pages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bulk_sends", "current_page", "next_page", "previous_page", "total_count", "total_pages", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        bulk_sends: typing.Union['BulkSendListBulkSendingsResponseBulkSends', schemas.Unset] = schemas.unset,
        current_page: typing.Union[MetaOapg.properties.current_page, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        next_page: typing.Union[MetaOapg.properties.next_page, None, str, schemas.Unset] = schemas.unset,
        previous_page: typing.Union[MetaOapg.properties.previous_page, None, str, schemas.Unset] = schemas.unset,
        total_count: typing.Union[MetaOapg.properties.total_count, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        total_pages: typing.Union[MetaOapg.properties.total_pages, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BulkSendListBulkSendingsResponse':
        return super().__new__(
            cls,
            *args,
            bulk_sends=bulk_sends,
            current_page=current_page,
            next_page=next_page,
            previous_page=previous_page,
            total_count=total_count,
            total_pages=total_pages,
            _configuration=_configuration,
            **kwargs,
        )

from sign_well_python_sdk.model.bulk_send_list_bulk_sendings_response_bulk_sends import BulkSendListBulkSendingsResponseBulkSends
