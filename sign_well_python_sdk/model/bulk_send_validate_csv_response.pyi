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


class BulkSendValidateCsvResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            bulk_send_csv = schemas.StrSchema
        
            @staticmethod
            def template_ids() -> typing.Type['BulkSendValidateCsvResponseTemplateIds']:
                return BulkSendValidateCsvResponseTemplateIds
            skip_row_errors = schemas.BoolSchema
            
            
            class api_application_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'api_application_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            name = schemas.StrSchema
            subject = schemas.StrSchema
            message = schemas.StrSchema
            apply_signing_order = schemas.BoolSchema
            __annotations__ = {
                "bulk_send_csv": bulk_send_csv,
                "template_ids": template_ids,
                "skip_row_errors": skip_row_errors,
                "api_application_id": api_application_id,
                "name": name,
                "subject": subject,
                "message": message,
                "apply_signing_order": apply_signing_order,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bulk_send_csv"]) -> MetaOapg.properties.bulk_send_csv: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["template_ids"]) -> 'BulkSendValidateCsvResponseTemplateIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skip_row_errors"]) -> MetaOapg.properties.skip_row_errors: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["api_application_id"]) -> MetaOapg.properties.api_application_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subject"]) -> MetaOapg.properties.subject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apply_signing_order"]) -> MetaOapg.properties.apply_signing_order: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bulk_send_csv", "template_ids", "skip_row_errors", "api_application_id", "name", "subject", "message", "apply_signing_order", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bulk_send_csv"]) -> typing.Union[MetaOapg.properties.bulk_send_csv, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["template_ids"]) -> typing.Union['BulkSendValidateCsvResponseTemplateIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skip_row_errors"]) -> typing.Union[MetaOapg.properties.skip_row_errors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["api_application_id"]) -> typing.Union[MetaOapg.properties.api_application_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subject"]) -> typing.Union[MetaOapg.properties.subject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apply_signing_order"]) -> typing.Union[MetaOapg.properties.apply_signing_order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bulk_send_csv", "template_ids", "skip_row_errors", "api_application_id", "name", "subject", "message", "apply_signing_order", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        bulk_send_csv: typing.Union[MetaOapg.properties.bulk_send_csv, str, schemas.Unset] = schemas.unset,
        template_ids: typing.Union['BulkSendValidateCsvResponseTemplateIds', schemas.Unset] = schemas.unset,
        skip_row_errors: typing.Union[MetaOapg.properties.skip_row_errors, bool, schemas.Unset] = schemas.unset,
        api_application_id: typing.Union[MetaOapg.properties.api_application_id, None, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        subject: typing.Union[MetaOapg.properties.subject, str, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        apply_signing_order: typing.Union[MetaOapg.properties.apply_signing_order, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BulkSendValidateCsvResponse':
        return super().__new__(
            cls,
            *args,
            bulk_send_csv=bulk_send_csv,
            template_ids=template_ids,
            skip_row_errors=skip_row_errors,
            api_application_id=api_application_id,
            name=name,
            subject=subject,
            message=message,
            apply_signing_order=apply_signing_order,
            _configuration=_configuration,
            **kwargs,
        )

from sign_well_python_sdk.model.bulk_send_validate_csv_response_template_ids import BulkSendValidateCsvResponseTemplateIds