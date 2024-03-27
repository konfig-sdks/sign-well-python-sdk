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


class DocumentTemplateRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "placeholders",
            "files",
        }
        
        class properties:
        
            @staticmethod
            def files() -> typing.Type['FilesMap']:
                return FilesMap
        
            @staticmethod
            def placeholders() -> typing.Type['PlaceholdersMap']:
                return PlaceholdersMap
            name = schemas.StrSchema
            subject = schemas.StrSchema
            message = schemas.StrSchema
        
            @staticmethod
            def copied_placeholders() -> typing.Type['CopiedPlaceholdersMap']:
                return CopiedPlaceholdersMap
            draft = schemas.BoolSchema
        
            @staticmethod
            def expires_in() -> typing.Type['ExpiresInMap']:
                return ExpiresInMap
            reminders = schemas.BoolSchema
            apply_signing_order = schemas.BoolSchema
            api_application_id = schemas.UUIDSchema
            text_tags = schemas.BoolSchema
            redirect_url = schemas.StrSchema
            allow_decline = schemas.BoolSchema
            allow_reassign = schemas.BoolSchema
            decline_redirect_url = schemas.StrSchema
            metadata = schemas.DictSchema
        
            @staticmethod
            def fields() -> typing.Type['FieldsForTemplateMap']:
                return FieldsForTemplateMap
        
            @staticmethod
            def attachment_requests() -> typing.Type['AttachmentRequestsForTemplateMap']:
                return AttachmentRequestsForTemplateMap
            __annotations__ = {
                "files": files,
                "placeholders": placeholders,
                "name": name,
                "subject": subject,
                "message": message,
                "copied_placeholders": copied_placeholders,
                "draft": draft,
                "expires_in": expires_in,
                "reminders": reminders,
                "apply_signing_order": apply_signing_order,
                "api_application_id": api_application_id,
                "text_tags": text_tags,
                "redirect_url": redirect_url,
                "allow_decline": allow_decline,
                "allow_reassign": allow_reassign,
                "decline_redirect_url": decline_redirect_url,
                "metadata": metadata,
                "fields": fields,
                "attachment_requests": attachment_requests,
            }
    
    placeholders: 'PlaceholdersMap'
    files: 'FilesMap'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["files"]) -> 'FilesMap': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["placeholders"]) -> 'PlaceholdersMap': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subject"]) -> MetaOapg.properties.subject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copied_placeholders"]) -> 'CopiedPlaceholdersMap': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["draft"]) -> MetaOapg.properties.draft: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expires_in"]) -> 'ExpiresInMap': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reminders"]) -> MetaOapg.properties.reminders: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apply_signing_order"]) -> MetaOapg.properties.apply_signing_order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["api_application_id"]) -> MetaOapg.properties.api_application_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["text_tags"]) -> MetaOapg.properties.text_tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirect_url"]) -> MetaOapg.properties.redirect_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allow_decline"]) -> MetaOapg.properties.allow_decline: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allow_reassign"]) -> MetaOapg.properties.allow_reassign: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["decline_redirect_url"]) -> MetaOapg.properties.decline_redirect_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fields"]) -> 'FieldsForTemplateMap': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachment_requests"]) -> 'AttachmentRequestsForTemplateMap': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["files", "placeholders", "name", "subject", "message", "copied_placeholders", "draft", "expires_in", "reminders", "apply_signing_order", "api_application_id", "text_tags", "redirect_url", "allow_decline", "allow_reassign", "decline_redirect_url", "metadata", "fields", "attachment_requests", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["files"]) -> 'FilesMap': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["placeholders"]) -> 'PlaceholdersMap': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subject"]) -> typing.Union[MetaOapg.properties.subject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copied_placeholders"]) -> typing.Union['CopiedPlaceholdersMap', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["draft"]) -> typing.Union[MetaOapg.properties.draft, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expires_in"]) -> typing.Union['ExpiresInMap', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reminders"]) -> typing.Union[MetaOapg.properties.reminders, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apply_signing_order"]) -> typing.Union[MetaOapg.properties.apply_signing_order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["api_application_id"]) -> typing.Union[MetaOapg.properties.api_application_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["text_tags"]) -> typing.Union[MetaOapg.properties.text_tags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirect_url"]) -> typing.Union[MetaOapg.properties.redirect_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allow_decline"]) -> typing.Union[MetaOapg.properties.allow_decline, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allow_reassign"]) -> typing.Union[MetaOapg.properties.allow_reassign, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["decline_redirect_url"]) -> typing.Union[MetaOapg.properties.decline_redirect_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fields"]) -> typing.Union['FieldsForTemplateMap', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachment_requests"]) -> typing.Union['AttachmentRequestsForTemplateMap', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["files", "placeholders", "name", "subject", "message", "copied_placeholders", "draft", "expires_in", "reminders", "apply_signing_order", "api_application_id", "text_tags", "redirect_url", "allow_decline", "allow_reassign", "decline_redirect_url", "metadata", "fields", "attachment_requests", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        placeholders: 'PlaceholdersMap',
        files: 'FilesMap',
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        subject: typing.Union[MetaOapg.properties.subject, str, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        copied_placeholders: typing.Union['CopiedPlaceholdersMap', schemas.Unset] = schemas.unset,
        draft: typing.Union[MetaOapg.properties.draft, bool, schemas.Unset] = schemas.unset,
        expires_in: typing.Union['ExpiresInMap', schemas.Unset] = schemas.unset,
        reminders: typing.Union[MetaOapg.properties.reminders, bool, schemas.Unset] = schemas.unset,
        apply_signing_order: typing.Union[MetaOapg.properties.apply_signing_order, bool, schemas.Unset] = schemas.unset,
        api_application_id: typing.Union[MetaOapg.properties.api_application_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        text_tags: typing.Union[MetaOapg.properties.text_tags, bool, schemas.Unset] = schemas.unset,
        redirect_url: typing.Union[MetaOapg.properties.redirect_url, str, schemas.Unset] = schemas.unset,
        allow_decline: typing.Union[MetaOapg.properties.allow_decline, bool, schemas.Unset] = schemas.unset,
        allow_reassign: typing.Union[MetaOapg.properties.allow_reassign, bool, schemas.Unset] = schemas.unset,
        decline_redirect_url: typing.Union[MetaOapg.properties.decline_redirect_url, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        fields: typing.Union['FieldsForTemplateMap', schemas.Unset] = schemas.unset,
        attachment_requests: typing.Union['AttachmentRequestsForTemplateMap', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentTemplateRequest':
        return super().__new__(
            cls,
            *args,
            placeholders=placeholders,
            files=files,
            name=name,
            subject=subject,
            message=message,
            copied_placeholders=copied_placeholders,
            draft=draft,
            expires_in=expires_in,
            reminders=reminders,
            apply_signing_order=apply_signing_order,
            api_application_id=api_application_id,
            text_tags=text_tags,
            redirect_url=redirect_url,
            allow_decline=allow_decline,
            allow_reassign=allow_reassign,
            decline_redirect_url=decline_redirect_url,
            metadata=metadata,
            fields=fields,
            attachment_requests=attachment_requests,
            _configuration=_configuration,
            **kwargs,
        )

from sign_well_python_sdk.model.attachment_requests_for_template_map import AttachmentRequestsForTemplateMap
from sign_well_python_sdk.model.copied_placeholders_map import CopiedPlaceholdersMap
from sign_well_python_sdk.model.expires_in_map import ExpiresInMap
from sign_well_python_sdk.model.fields_for_template_map import FieldsForTemplateMap
from sign_well_python_sdk.model.files_map import FilesMap
from sign_well_python_sdk.model.placeholders_map import PlaceholdersMap