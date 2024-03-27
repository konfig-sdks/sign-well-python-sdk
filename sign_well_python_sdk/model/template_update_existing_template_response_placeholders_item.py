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


class TemplateUpdateExistingTemplateResponsePlaceholdersItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class subject(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'subject':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class message(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'message':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            preassigned_recipient_name = schemas.StrSchema
            preassigned_recipient_email = schemas.StrSchema
            signing_order = schemas.NumberSchema
        
            @staticmethod
            def attachment_requests() -> typing.Type['TemplateUpdateExistingTemplateResponsePlaceholdersItemAttachmentRequests']:
                return TemplateUpdateExistingTemplateResponsePlaceholdersItemAttachmentRequests
            __annotations__ = {
                "id": id,
                "name": name,
                "subject": subject,
                "message": message,
                "preassigned_recipient_name": preassigned_recipient_name,
                "preassigned_recipient_email": preassigned_recipient_email,
                "signing_order": signing_order,
                "attachment_requests": attachment_requests,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subject"]) -> MetaOapg.properties.subject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preassigned_recipient_name"]) -> MetaOapg.properties.preassigned_recipient_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preassigned_recipient_email"]) -> MetaOapg.properties.preassigned_recipient_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signing_order"]) -> MetaOapg.properties.signing_order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachment_requests"]) -> 'TemplateUpdateExistingTemplateResponsePlaceholdersItemAttachmentRequests': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "subject", "message", "preassigned_recipient_name", "preassigned_recipient_email", "signing_order", "attachment_requests", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subject"]) -> typing.Union[MetaOapg.properties.subject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preassigned_recipient_name"]) -> typing.Union[MetaOapg.properties.preassigned_recipient_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preassigned_recipient_email"]) -> typing.Union[MetaOapg.properties.preassigned_recipient_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signing_order"]) -> typing.Union[MetaOapg.properties.signing_order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachment_requests"]) -> typing.Union['TemplateUpdateExistingTemplateResponsePlaceholdersItemAttachmentRequests', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "subject", "message", "preassigned_recipient_name", "preassigned_recipient_email", "signing_order", "attachment_requests", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        subject: typing.Union[MetaOapg.properties.subject, None, str, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, None, str, schemas.Unset] = schemas.unset,
        preassigned_recipient_name: typing.Union[MetaOapg.properties.preassigned_recipient_name, str, schemas.Unset] = schemas.unset,
        preassigned_recipient_email: typing.Union[MetaOapg.properties.preassigned_recipient_email, str, schemas.Unset] = schemas.unset,
        signing_order: typing.Union[MetaOapg.properties.signing_order, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        attachment_requests: typing.Union['TemplateUpdateExistingTemplateResponsePlaceholdersItemAttachmentRequests', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TemplateUpdateExistingTemplateResponsePlaceholdersItem':
        return super().__new__(
            cls,
            *args,
            id=id,
            name=name,
            subject=subject,
            message=message,
            preassigned_recipient_name=preassigned_recipient_name,
            preassigned_recipient_email=preassigned_recipient_email,
            signing_order=signing_order,
            attachment_requests=attachment_requests,
            _configuration=_configuration,
            **kwargs,
        )

from sign_well_python_sdk.model.template_update_existing_template_response_placeholders_item_attachment_requests import TemplateUpdateExistingTemplateResponsePlaceholdersItemAttachmentRequests
