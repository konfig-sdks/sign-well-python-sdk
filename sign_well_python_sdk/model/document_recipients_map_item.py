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


class DocumentRecipientsMapItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "id",
            "email",
        }
        
        class properties:
            id = schemas.StrSchema
            email = schemas.StrSchema
            name = schemas.StrSchema
            passcode = schemas.StrSchema
            subject = schemas.StrSchema
            message = schemas.StrSchema
            send_email = schemas.BoolSchema
            send_email_delay = schemas.IntSchema
            __annotations__ = {
                "id": id,
                "email": email,
                "name": name,
                "passcode": passcode,
                "subject": subject,
                "message": message,
                "send_email": send_email,
                "send_email_delay": send_email_delay,
            }
    
    id: MetaOapg.properties.id
    email: MetaOapg.properties.email
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["passcode"]) -> MetaOapg.properties.passcode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subject"]) -> MetaOapg.properties.subject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["send_email"]) -> MetaOapg.properties.send_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["send_email_delay"]) -> MetaOapg.properties.send_email_delay: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "email", "name", "passcode", "subject", "message", "send_email", "send_email_delay", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["passcode"]) -> typing.Union[MetaOapg.properties.passcode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subject"]) -> typing.Union[MetaOapg.properties.subject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["send_email"]) -> typing.Union[MetaOapg.properties.send_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["send_email_delay"]) -> typing.Union[MetaOapg.properties.send_email_delay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "email", "name", "passcode", "subject", "message", "send_email", "send_email_delay", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        email: typing.Union[MetaOapg.properties.email, str, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        passcode: typing.Union[MetaOapg.properties.passcode, str, schemas.Unset] = schemas.unset,
        subject: typing.Union[MetaOapg.properties.subject, str, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        send_email: typing.Union[MetaOapg.properties.send_email, bool, schemas.Unset] = schemas.unset,
        send_email_delay: typing.Union[MetaOapg.properties.send_email_delay, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentRecipientsMapItem':
        return super().__new__(
            cls,
            *args,
            id=id,
            email=email,
            name=name,
            passcode=passcode,
            subject=subject,
            message=message,
            send_email=send_email,
            send_email_delay=send_email_delay,
            _configuration=_configuration,
            **kwargs,
        )
