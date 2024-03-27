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


class ApiApplicationGetDetailsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
        
            @staticmethod
            def callback_urls() -> typing.Type['ApiApplicationGetDetailsResponseCallbackUrls']:
                return ApiApplicationGetDetailsResponseCallbackUrls
            created_at = schemas.StrSchema
            name = schemas.StrSchema
            updated_at = schemas.StrSchema
        
            @staticmethod
            def owner() -> typing.Type['ApiApplicationGetDetailsResponseOwner']:
                return ApiApplicationGetDetailsResponseOwner
        
            @staticmethod
            def preferences() -> typing.Type['ApiApplicationGetDetailsResponsePreferences']:
                return ApiApplicationGetDetailsResponsePreferences
            __annotations__ = {
                "id": id,
                "callback_urls": callback_urls,
                "created_at": created_at,
                "name": name,
                "updated_at": updated_at,
                "owner": owner,
                "preferences": preferences,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callback_urls"]) -> 'ApiApplicationGetDetailsResponseCallbackUrls': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner"]) -> 'ApiApplicationGetDetailsResponseOwner': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preferences"]) -> 'ApiApplicationGetDetailsResponsePreferences': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "callback_urls", "created_at", "name", "updated_at", "owner", "preferences", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["callback_urls"]) -> typing.Union['ApiApplicationGetDetailsResponseCallbackUrls', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner"]) -> typing.Union['ApiApplicationGetDetailsResponseOwner', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preferences"]) -> typing.Union['ApiApplicationGetDetailsResponsePreferences', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "callback_urls", "created_at", "name", "updated_at", "owner", "preferences", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        callback_urls: typing.Union['ApiApplicationGetDetailsResponseCallbackUrls', schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, schemas.Unset] = schemas.unset,
        owner: typing.Union['ApiApplicationGetDetailsResponseOwner', schemas.Unset] = schemas.unset,
        preferences: typing.Union['ApiApplicationGetDetailsResponsePreferences', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApiApplicationGetDetailsResponse':
        return super().__new__(
            cls,
            *args,
            id=id,
            callback_urls=callback_urls,
            created_at=created_at,
            name=name,
            updated_at=updated_at,
            owner=owner,
            preferences=preferences,
            _configuration=_configuration,
            **kwargs,
        )

from sign_well_python_sdk.model.api_application_get_details_response_callback_urls import ApiApplicationGetDetailsResponseCallbackUrls
from sign_well_python_sdk.model.api_application_get_details_response_owner import ApiApplicationGetDetailsResponseOwner
from sign_well_python_sdk.model.api_application_get_details_response_preferences import ApiApplicationGetDetailsResponsePreferences