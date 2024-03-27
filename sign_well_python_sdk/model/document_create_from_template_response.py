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


class DocumentCreateFromTemplateResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            archived = schemas.BoolSchema
        
            @staticmethod
            def copied_contacts() -> typing.Type['DocumentCreateFromTemplateResponseCopiedContacts']:
                return DocumentCreateFromTemplateResponseCopiedContacts
            created_at = schemas.StrSchema
            custom_requester_email = schemas.StrSchema
            custom_requester_name = schemas.StrSchema
            decline_redirect_url = schemas.StrSchema
            embedded_edit_url = schemas.StrSchema
            
            
            class embedded_preview_url(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'embedded_preview_url':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class error_message(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'error_message':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def fields() -> typing.Type['DocumentCreateFromTemplateResponseFields']:
                return DocumentCreateFromTemplateResponseFields
        
            @staticmethod
            def metadata() -> typing.Type['DocumentCreateFromTemplateResponseMetadata']:
                return DocumentCreateFromTemplateResponseMetadata
            name = schemas.StrSchema
        
            @staticmethod
            def recipients() -> typing.Type['DocumentCreateFromTemplateResponseRecipients']:
                return DocumentCreateFromTemplateResponseRecipients
            subject = schemas.StrSchema
            test_mode = schemas.BoolSchema
            updated_at = schemas.StrSchema
            
            
            class decline_message(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'decline_message':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
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
            allow_decline = schemas.BoolSchema
            allow_reassign = schemas.BoolSchema
            apply_signing_order = schemas.BoolSchema
            embedded_signing = schemas.BoolSchema
            expires_in = schemas.NumberSchema
            message = schemas.StrSchema
            reminders = schemas.BoolSchema
            requester_email_address = schemas.StrSchema
            redirect_url = schemas.StrSchema
            status = schemas.StrSchema
        
            @staticmethod
            def template_ids() -> typing.Type['DocumentCreateFromTemplateResponseTemplateIds']:
                return DocumentCreateFromTemplateResponseTemplateIds
        
            @staticmethod
            def files() -> typing.Type['DocumentCreateFromTemplateResponseFiles']:
                return DocumentCreateFromTemplateResponseFiles
            __annotations__ = {
                "id": id,
                "archived": archived,
                "copied_contacts": copied_contacts,
                "created_at": created_at,
                "custom_requester_email": custom_requester_email,
                "custom_requester_name": custom_requester_name,
                "decline_redirect_url": decline_redirect_url,
                "embedded_edit_url": embedded_edit_url,
                "embedded_preview_url": embedded_preview_url,
                "error_message": error_message,
                "fields": fields,
                "metadata": metadata,
                "name": name,
                "recipients": recipients,
                "subject": subject,
                "test_mode": test_mode,
                "updated_at": updated_at,
                "decline_message": decline_message,
                "api_application_id": api_application_id,
                "allow_decline": allow_decline,
                "allow_reassign": allow_reassign,
                "apply_signing_order": apply_signing_order,
                "embedded_signing": embedded_signing,
                "expires_in": expires_in,
                "message": message,
                "reminders": reminders,
                "requester_email_address": requester_email_address,
                "redirect_url": redirect_url,
                "status": status,
                "template_ids": template_ids,
                "files": files,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["archived"]) -> MetaOapg.properties.archived: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copied_contacts"]) -> 'DocumentCreateFromTemplateResponseCopiedContacts': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_requester_email"]) -> MetaOapg.properties.custom_requester_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_requester_name"]) -> MetaOapg.properties.custom_requester_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["decline_redirect_url"]) -> MetaOapg.properties.decline_redirect_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["embedded_edit_url"]) -> MetaOapg.properties.embedded_edit_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["embedded_preview_url"]) -> MetaOapg.properties.embedded_preview_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error_message"]) -> MetaOapg.properties.error_message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fields"]) -> 'DocumentCreateFromTemplateResponseFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'DocumentCreateFromTemplateResponseMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recipients"]) -> 'DocumentCreateFromTemplateResponseRecipients': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subject"]) -> MetaOapg.properties.subject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["test_mode"]) -> MetaOapg.properties.test_mode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["decline_message"]) -> MetaOapg.properties.decline_message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["api_application_id"]) -> MetaOapg.properties.api_application_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allow_decline"]) -> MetaOapg.properties.allow_decline: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allow_reassign"]) -> MetaOapg.properties.allow_reassign: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apply_signing_order"]) -> MetaOapg.properties.apply_signing_order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["embedded_signing"]) -> MetaOapg.properties.embedded_signing: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expires_in"]) -> MetaOapg.properties.expires_in: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reminders"]) -> MetaOapg.properties.reminders: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requester_email_address"]) -> MetaOapg.properties.requester_email_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirect_url"]) -> MetaOapg.properties.redirect_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["template_ids"]) -> 'DocumentCreateFromTemplateResponseTemplateIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["files"]) -> 'DocumentCreateFromTemplateResponseFiles': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "archived", "copied_contacts", "created_at", "custom_requester_email", "custom_requester_name", "decline_redirect_url", "embedded_edit_url", "embedded_preview_url", "error_message", "fields", "metadata", "name", "recipients", "subject", "test_mode", "updated_at", "decline_message", "api_application_id", "allow_decline", "allow_reassign", "apply_signing_order", "embedded_signing", "expires_in", "message", "reminders", "requester_email_address", "redirect_url", "status", "template_ids", "files", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["archived"]) -> typing.Union[MetaOapg.properties.archived, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copied_contacts"]) -> typing.Union['DocumentCreateFromTemplateResponseCopiedContacts', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_requester_email"]) -> typing.Union[MetaOapg.properties.custom_requester_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_requester_name"]) -> typing.Union[MetaOapg.properties.custom_requester_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["decline_redirect_url"]) -> typing.Union[MetaOapg.properties.decline_redirect_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["embedded_edit_url"]) -> typing.Union[MetaOapg.properties.embedded_edit_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["embedded_preview_url"]) -> typing.Union[MetaOapg.properties.embedded_preview_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error_message"]) -> typing.Union[MetaOapg.properties.error_message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fields"]) -> typing.Union['DocumentCreateFromTemplateResponseFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['DocumentCreateFromTemplateResponseMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recipients"]) -> typing.Union['DocumentCreateFromTemplateResponseRecipients', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subject"]) -> typing.Union[MetaOapg.properties.subject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["test_mode"]) -> typing.Union[MetaOapg.properties.test_mode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["decline_message"]) -> typing.Union[MetaOapg.properties.decline_message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["api_application_id"]) -> typing.Union[MetaOapg.properties.api_application_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allow_decline"]) -> typing.Union[MetaOapg.properties.allow_decline, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allow_reassign"]) -> typing.Union[MetaOapg.properties.allow_reassign, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apply_signing_order"]) -> typing.Union[MetaOapg.properties.apply_signing_order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["embedded_signing"]) -> typing.Union[MetaOapg.properties.embedded_signing, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expires_in"]) -> typing.Union[MetaOapg.properties.expires_in, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reminders"]) -> typing.Union[MetaOapg.properties.reminders, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requester_email_address"]) -> typing.Union[MetaOapg.properties.requester_email_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirect_url"]) -> typing.Union[MetaOapg.properties.redirect_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["template_ids"]) -> typing.Union['DocumentCreateFromTemplateResponseTemplateIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["files"]) -> typing.Union['DocumentCreateFromTemplateResponseFiles', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "archived", "copied_contacts", "created_at", "custom_requester_email", "custom_requester_name", "decline_redirect_url", "embedded_edit_url", "embedded_preview_url", "error_message", "fields", "metadata", "name", "recipients", "subject", "test_mode", "updated_at", "decline_message", "api_application_id", "allow_decline", "allow_reassign", "apply_signing_order", "embedded_signing", "expires_in", "message", "reminders", "requester_email_address", "redirect_url", "status", "template_ids", "files", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        archived: typing.Union[MetaOapg.properties.archived, bool, schemas.Unset] = schemas.unset,
        copied_contacts: typing.Union['DocumentCreateFromTemplateResponseCopiedContacts', schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, schemas.Unset] = schemas.unset,
        custom_requester_email: typing.Union[MetaOapg.properties.custom_requester_email, str, schemas.Unset] = schemas.unset,
        custom_requester_name: typing.Union[MetaOapg.properties.custom_requester_name, str, schemas.Unset] = schemas.unset,
        decline_redirect_url: typing.Union[MetaOapg.properties.decline_redirect_url, str, schemas.Unset] = schemas.unset,
        embedded_edit_url: typing.Union[MetaOapg.properties.embedded_edit_url, str, schemas.Unset] = schemas.unset,
        embedded_preview_url: typing.Union[MetaOapg.properties.embedded_preview_url, None, str, schemas.Unset] = schemas.unset,
        error_message: typing.Union[MetaOapg.properties.error_message, None, str, schemas.Unset] = schemas.unset,
        fields: typing.Union['DocumentCreateFromTemplateResponseFields', schemas.Unset] = schemas.unset,
        metadata: typing.Union['DocumentCreateFromTemplateResponseMetadata', schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        recipients: typing.Union['DocumentCreateFromTemplateResponseRecipients', schemas.Unset] = schemas.unset,
        subject: typing.Union[MetaOapg.properties.subject, str, schemas.Unset] = schemas.unset,
        test_mode: typing.Union[MetaOapg.properties.test_mode, bool, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, schemas.Unset] = schemas.unset,
        decline_message: typing.Union[MetaOapg.properties.decline_message, None, str, schemas.Unset] = schemas.unset,
        api_application_id: typing.Union[MetaOapg.properties.api_application_id, None, str, schemas.Unset] = schemas.unset,
        allow_decline: typing.Union[MetaOapg.properties.allow_decline, bool, schemas.Unset] = schemas.unset,
        allow_reassign: typing.Union[MetaOapg.properties.allow_reassign, bool, schemas.Unset] = schemas.unset,
        apply_signing_order: typing.Union[MetaOapg.properties.apply_signing_order, bool, schemas.Unset] = schemas.unset,
        embedded_signing: typing.Union[MetaOapg.properties.embedded_signing, bool, schemas.Unset] = schemas.unset,
        expires_in: typing.Union[MetaOapg.properties.expires_in, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        reminders: typing.Union[MetaOapg.properties.reminders, bool, schemas.Unset] = schemas.unset,
        requester_email_address: typing.Union[MetaOapg.properties.requester_email_address, str, schemas.Unset] = schemas.unset,
        redirect_url: typing.Union[MetaOapg.properties.redirect_url, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        template_ids: typing.Union['DocumentCreateFromTemplateResponseTemplateIds', schemas.Unset] = schemas.unset,
        files: typing.Union['DocumentCreateFromTemplateResponseFiles', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentCreateFromTemplateResponse':
        return super().__new__(
            cls,
            *args,
            id=id,
            archived=archived,
            copied_contacts=copied_contacts,
            created_at=created_at,
            custom_requester_email=custom_requester_email,
            custom_requester_name=custom_requester_name,
            decline_redirect_url=decline_redirect_url,
            embedded_edit_url=embedded_edit_url,
            embedded_preview_url=embedded_preview_url,
            error_message=error_message,
            fields=fields,
            metadata=metadata,
            name=name,
            recipients=recipients,
            subject=subject,
            test_mode=test_mode,
            updated_at=updated_at,
            decline_message=decline_message,
            api_application_id=api_application_id,
            allow_decline=allow_decline,
            allow_reassign=allow_reassign,
            apply_signing_order=apply_signing_order,
            embedded_signing=embedded_signing,
            expires_in=expires_in,
            message=message,
            reminders=reminders,
            requester_email_address=requester_email_address,
            redirect_url=redirect_url,
            status=status,
            template_ids=template_ids,
            files=files,
            _configuration=_configuration,
            **kwargs,
        )

from sign_well_python_sdk.model.document_create_from_template_response_copied_contacts import DocumentCreateFromTemplateResponseCopiedContacts
from sign_well_python_sdk.model.document_create_from_template_response_fields import DocumentCreateFromTemplateResponseFields
from sign_well_python_sdk.model.document_create_from_template_response_files import DocumentCreateFromTemplateResponseFiles
from sign_well_python_sdk.model.document_create_from_template_response_metadata import DocumentCreateFromTemplateResponseMetadata
from sign_well_python_sdk.model.document_create_from_template_response_recipients import DocumentCreateFromTemplateResponseRecipients
from sign_well_python_sdk.model.document_create_from_template_response_template_ids import DocumentCreateFromTemplateResponseTemplateIds
