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


class MeGetAccountInfoResponseContact(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            email = schemas.StrSchema
            name = schemas.StrSchema
            company_name = schemas.StrSchema
            phone_number = schemas.StrSchema
            alt_phone_number = schemas.StrSchema
            website = schemas.StrSchema
            initials = schemas.StrSchema
            archived = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "email": email,
                "name": name,
                "company_name": company_name,
                "phone_number": phone_number,
                "alt_phone_number": alt_phone_number,
                "website": website,
                "initials": initials,
                "archived": archived,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_name"]) -> MetaOapg.properties.company_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone_number"]) -> MetaOapg.properties.phone_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alt_phone_number"]) -> MetaOapg.properties.alt_phone_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["website"]) -> MetaOapg.properties.website: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["initials"]) -> MetaOapg.properties.initials: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["archived"]) -> MetaOapg.properties.archived: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "email", "name", "company_name", "phone_number", "alt_phone_number", "website", "initials", "archived", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_name"]) -> typing.Union[MetaOapg.properties.company_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone_number"]) -> typing.Union[MetaOapg.properties.phone_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alt_phone_number"]) -> typing.Union[MetaOapg.properties.alt_phone_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["website"]) -> typing.Union[MetaOapg.properties.website, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["initials"]) -> typing.Union[MetaOapg.properties.initials, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["archived"]) -> typing.Union[MetaOapg.properties.archived, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "email", "name", "company_name", "phone_number", "alt_phone_number", "website", "initials", "archived", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        company_name: typing.Union[MetaOapg.properties.company_name, str, schemas.Unset] = schemas.unset,
        phone_number: typing.Union[MetaOapg.properties.phone_number, str, schemas.Unset] = schemas.unset,
        alt_phone_number: typing.Union[MetaOapg.properties.alt_phone_number, str, schemas.Unset] = schemas.unset,
        website: typing.Union[MetaOapg.properties.website, str, schemas.Unset] = schemas.unset,
        initials: typing.Union[MetaOapg.properties.initials, str, schemas.Unset] = schemas.unset,
        archived: typing.Union[MetaOapg.properties.archived, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MeGetAccountInfoResponseContact':
        return super().__new__(
            cls,
            *args,
            id=id,
            email=email,
            name=name,
            company_name=company_name,
            phone_number=phone_number,
            alt_phone_number=alt_phone_number,
            website=website,
            initials=initials,
            archived=archived,
            _configuration=_configuration,
            **kwargs,
        )
