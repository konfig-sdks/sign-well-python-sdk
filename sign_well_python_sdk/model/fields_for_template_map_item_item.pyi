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


class FieldsForTemplateMapItemItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "placeholder_id",
            "x",
            "y",
            "page",
            "type",
        }
        
        class properties:
            x = schemas.Float32Schema
            y = schemas.Float32Schema
            page = schemas.IntSchema
            placeholder_id = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INITIALS(cls):
                    return cls("initials")
                
                @schemas.classproperty
                def SIGNATURE(cls):
                    return cls("signature")
                
                @schemas.classproperty
                def CHECKBOX(cls):
                    return cls("checkbox")
                
                @schemas.classproperty
                def DATE(cls):
                    return cls("date")
                
                @schemas.classproperty
                def TEXT(cls):
                    return cls("text")
                
                @schemas.classproperty
                def AUTOFILL_COMPANY(cls):
                    return cls("autofill_company")
                
                @schemas.classproperty
                def AUTOFILL_EMAIL(cls):
                    return cls("autofill_email")
                
                @schemas.classproperty
                def AUTOFILL_FIRST_NAME(cls):
                    return cls("autofill_first_name")
                
                @schemas.classproperty
                def AUTOFILL_LAST_NAME(cls):
                    return cls("autofill_last_name")
                
                @schemas.classproperty
                def AUTOFILL_NAME(cls):
                    return cls("autofill_name")
                
                @schemas.classproperty
                def AUTOFILL_PHONE(cls):
                    return cls("autofill_phone")
                
                @schemas.classproperty
                def AUTOFILL_TITLE(cls):
                    return cls("autofill_title")
                
                @schemas.classproperty
                def AUTOFILL_DATE_SIGNED(cls):
                    return cls("autofill_date_signed")
            required = schemas.BoolSchema
            label = schemas.StrSchema
            value = schemas.AnyTypeSchema
            api_id = schemas.StrSchema
            
            
            class validation(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def NO_TEXT_VALIDATION(cls):
                    return cls("no_text_validation")
                
                @schemas.classproperty
                def NUMBERS(cls):
                    return cls("numbers")
                
                @schemas.classproperty
                def LETTERS(cls):
                    return cls("letters")
                
                @schemas.classproperty
                def EMAIL_ADDRESS(cls):
                    return cls("email_address")
                
                @schemas.classproperty
                def US_PHONE_NUMBER(cls):
                    return cls("us_phone_number")
                
                @schemas.classproperty
                def US_ZIP_CODE(cls):
                    return cls("us_zip_code")
                
                @schemas.classproperty
                def US_SSN(cls):
                    return cls("us_ssn")
                
                @schemas.classproperty
                def US_AGE(cls):
                    return cls("us_age")
                
                @schemas.classproperty
                def ALPHANUMERIC(cls):
                    return cls("alphanumeric")
                
                @schemas.classproperty
                def US_BANK_ROUTING_NUMBER(cls):
                    return cls("us_bank_routing_number")
                
                @schemas.classproperty
                def US_BANK_ACCOUNT_NUMBER(cls):
                    return cls("us_bank_account_number")
            fixed_width = schemas.BoolSchema
            lock_sign_date = schemas.BoolSchema
            
            
            class date_format(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def MM_DD_YYYY(cls):
                    return cls("MM/DD/YYYY")
                
                @schemas.classproperty
                def DD_MM_YYYY(cls):
                    return cls("DD/MM/YYYY")
                
                @schemas.classproperty
                def YYYY_MM_DD(cls):
                    return cls("YYYY/MM/DD")
                
                @schemas.classproperty
                def MONTH_DD_YYYY(cls):
                    return cls("Month DD, YYYY")
                
                @schemas.classproperty
                def MM_DD_YYYY_HHMMSS_A(cls):
                    return cls("MM/DD/YYYY hh:mm:ss a")
            __annotations__ = {
                "x": x,
                "y": y,
                "page": page,
                "placeholder_id": placeholder_id,
                "type": type,
                "required": required,
                "label": label,
                "value": value,
                "api_id": api_id,
                "validation": validation,
                "fixed_width": fixed_width,
                "lock_sign_date": lock_sign_date,
                "date_format": date_format,
            }
    
    placeholder_id: MetaOapg.properties.placeholder_id
    x: MetaOapg.properties.x
    y: MetaOapg.properties.y
    page: MetaOapg.properties.page
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["x"]) -> MetaOapg.properties.x: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["y"]) -> MetaOapg.properties.y: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["placeholder_id"]) -> MetaOapg.properties.placeholder_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["api_id"]) -> MetaOapg.properties.api_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["validation"]) -> MetaOapg.properties.validation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fixed_width"]) -> MetaOapg.properties.fixed_width: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lock_sign_date"]) -> MetaOapg.properties.lock_sign_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_format"]) -> MetaOapg.properties.date_format: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["x", "y", "page", "placeholder_id", "type", "required", "label", "value", "api_id", "validation", "fixed_width", "lock_sign_date", "date_format", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["x"]) -> MetaOapg.properties.x: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["y"]) -> MetaOapg.properties.y: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["placeholder_id"]) -> MetaOapg.properties.placeholder_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["required"]) -> typing.Union[MetaOapg.properties.required, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union[MetaOapg.properties.label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["api_id"]) -> typing.Union[MetaOapg.properties.api_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["validation"]) -> typing.Union[MetaOapg.properties.validation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fixed_width"]) -> typing.Union[MetaOapg.properties.fixed_width, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lock_sign_date"]) -> typing.Union[MetaOapg.properties.lock_sign_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_format"]) -> typing.Union[MetaOapg.properties.date_format, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["x", "y", "page", "placeholder_id", "type", "required", "label", "value", "api_id", "validation", "fixed_width", "lock_sign_date", "date_format", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        placeholder_id: typing.Union[MetaOapg.properties.placeholder_id, str, ],
        x: typing.Union[MetaOapg.properties.x, decimal.Decimal, int, float, ],
        y: typing.Union[MetaOapg.properties.y, decimal.Decimal, int, float, ],
        page: typing.Union[MetaOapg.properties.page, decimal.Decimal, int, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        required: typing.Union[MetaOapg.properties.required, bool, schemas.Unset] = schemas.unset,
        label: typing.Union[MetaOapg.properties.label, str, schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        api_id: typing.Union[MetaOapg.properties.api_id, str, schemas.Unset] = schemas.unset,
        validation: typing.Union[MetaOapg.properties.validation, str, schemas.Unset] = schemas.unset,
        fixed_width: typing.Union[MetaOapg.properties.fixed_width, bool, schemas.Unset] = schemas.unset,
        lock_sign_date: typing.Union[MetaOapg.properties.lock_sign_date, bool, schemas.Unset] = schemas.unset,
        date_format: typing.Union[MetaOapg.properties.date_format, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FieldsForTemplateMapItemItem':
        return super().__new__(
            cls,
            *args,
            placeholder_id=placeholder_id,
            x=x,
            y=y,
            page=page,
            type=type,
            required=required,
            label=label,
            value=value,
            api_id=api_id,
            validation=validation,
            fixed_width=fixed_width,
            lock_sign_date=lock_sign_date,
            date_format=date_format,
            _configuration=_configuration,
            **kwargs,
        )
