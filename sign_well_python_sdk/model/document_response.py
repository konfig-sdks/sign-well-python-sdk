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


class DocumentResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "test_mode",
            "id",
        }
        
        class properties:
            test_mode = schemas.BoolSchema
            id = schemas.StrSchema
            api_application_id = schemas.UUIDSchema
            requester_email_address = schemas.StrSchema
            custom_requester_name = schemas.StrSchema
            custom_requester_email = schemas.StrSchema
            name = schemas.StrSchema
            subject = schemas.StrSchema
            message = schemas.StrSchema
            metadata = schemas.DictSchema
            created_at = schemas.DateTimeSchema
            updated_at = schemas.DateTimeSchema
        
            @staticmethod
            def recipients() -> typing.Type['DocumentResponseRecipients']:
                return DocumentResponseRecipients
            status = schemas.StrSchema
            reminders = schemas.BoolSchema
            archived = schemas.BoolSchema
            embedded = schemas.BoolSchema
            embedded_edit_url = schemas.StrSchema
            embedded_preview_url = schemas.StrSchema
            apply_signing_order = schemas.BoolSchema
            redirect_url = schemas.StrSchema
            decline_redirect_url = schemas.StrSchema
            expires_in = schemas.IntSchema
        
            @staticmethod
            def attachment_requests() -> typing.Type['DocumentResponseAttachmentRequests']:
                return DocumentResponseAttachmentRequests
        
            @staticmethod
            def files() -> typing.Type['DocumentResponseFiles']:
                return DocumentResponseFiles
        
            @staticmethod
            def copied_contacts() -> typing.Type['DocumentResponseCopiedContacts']:
                return DocumentResponseCopiedContacts
        
            @staticmethod
            def fields() -> typing.Type['DocumentResponseFields']:
                return DocumentResponseFields
            allow_decline = schemas.BoolSchema
            allow_reassign = schemas.BoolSchema
            __annotations__ = {
                "test_mode": test_mode,
                "id": id,
                "api_application_id": api_application_id,
                "requester_email_address": requester_email_address,
                "custom_requester_name": custom_requester_name,
                "custom_requester_email": custom_requester_email,
                "name": name,
                "subject": subject,
                "message": message,
                "metadata": metadata,
                "created_at": created_at,
                "updated_at": updated_at,
                "recipients": recipients,
                "status": status,
                "reminders": reminders,
                "archived": archived,
                "embedded": embedded,
                "embedded_edit_url": embedded_edit_url,
                "embedded_preview_url": embedded_preview_url,
                "apply_signing_order": apply_signing_order,
                "redirect_url": redirect_url,
                "decline_redirect_url": decline_redirect_url,
                "expires_in": expires_in,
                "attachment_requests": attachment_requests,
                "files": files,
                "copied_contacts": copied_contacts,
                "fields": fields,
                "allow_decline": allow_decline,
                "allow_reassign": allow_reassign,
            }
    
    test_mode: MetaOapg.properties.test_mode
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["test_mode"]) -> MetaOapg.properties.test_mode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["api_application_id"]) -> MetaOapg.properties.api_application_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requester_email_address"]) -> MetaOapg.properties.requester_email_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_requester_name"]) -> MetaOapg.properties.custom_requester_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_requester_email"]) -> MetaOapg.properties.custom_requester_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subject"]) -> MetaOapg.properties.subject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recipients"]) -> 'DocumentResponseRecipients': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reminders"]) -> MetaOapg.properties.reminders: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["archived"]) -> MetaOapg.properties.archived: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["embedded"]) -> MetaOapg.properties.embedded: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["embedded_edit_url"]) -> MetaOapg.properties.embedded_edit_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["embedded_preview_url"]) -> MetaOapg.properties.embedded_preview_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apply_signing_order"]) -> MetaOapg.properties.apply_signing_order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirect_url"]) -> MetaOapg.properties.redirect_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["decline_redirect_url"]) -> MetaOapg.properties.decline_redirect_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expires_in"]) -> MetaOapg.properties.expires_in: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachment_requests"]) -> 'DocumentResponseAttachmentRequests': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["files"]) -> 'DocumentResponseFiles': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copied_contacts"]) -> 'DocumentResponseCopiedContacts': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fields"]) -> 'DocumentResponseFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allow_decline"]) -> MetaOapg.properties.allow_decline: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allow_reassign"]) -> MetaOapg.properties.allow_reassign: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["test_mode", "id", "api_application_id", "requester_email_address", "custom_requester_name", "custom_requester_email", "name", "subject", "message", "metadata", "created_at", "updated_at", "recipients", "status", "reminders", "archived", "embedded", "embedded_edit_url", "embedded_preview_url", "apply_signing_order", "redirect_url", "decline_redirect_url", "expires_in", "attachment_requests", "files", "copied_contacts", "fields", "allow_decline", "allow_reassign", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["test_mode"]) -> MetaOapg.properties.test_mode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["api_application_id"]) -> typing.Union[MetaOapg.properties.api_application_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requester_email_address"]) -> typing.Union[MetaOapg.properties.requester_email_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_requester_name"]) -> typing.Union[MetaOapg.properties.custom_requester_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_requester_email"]) -> typing.Union[MetaOapg.properties.custom_requester_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subject"]) -> typing.Union[MetaOapg.properties.subject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recipients"]) -> typing.Union['DocumentResponseRecipients', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reminders"]) -> typing.Union[MetaOapg.properties.reminders, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["archived"]) -> typing.Union[MetaOapg.properties.archived, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["embedded"]) -> typing.Union[MetaOapg.properties.embedded, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["embedded_edit_url"]) -> typing.Union[MetaOapg.properties.embedded_edit_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["embedded_preview_url"]) -> typing.Union[MetaOapg.properties.embedded_preview_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apply_signing_order"]) -> typing.Union[MetaOapg.properties.apply_signing_order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirect_url"]) -> typing.Union[MetaOapg.properties.redirect_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["decline_redirect_url"]) -> typing.Union[MetaOapg.properties.decline_redirect_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expires_in"]) -> typing.Union[MetaOapg.properties.expires_in, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachment_requests"]) -> typing.Union['DocumentResponseAttachmentRequests', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["files"]) -> typing.Union['DocumentResponseFiles', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copied_contacts"]) -> typing.Union['DocumentResponseCopiedContacts', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fields"]) -> typing.Union['DocumentResponseFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allow_decline"]) -> typing.Union[MetaOapg.properties.allow_decline, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allow_reassign"]) -> typing.Union[MetaOapg.properties.allow_reassign, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["test_mode", "id", "api_application_id", "requester_email_address", "custom_requester_name", "custom_requester_email", "name", "subject", "message", "metadata", "created_at", "updated_at", "recipients", "status", "reminders", "archived", "embedded", "embedded_edit_url", "embedded_preview_url", "apply_signing_order", "redirect_url", "decline_redirect_url", "expires_in", "attachment_requests", "files", "copied_contacts", "fields", "allow_decline", "allow_reassign", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        test_mode: typing.Union[MetaOapg.properties.test_mode, bool, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        api_application_id: typing.Union[MetaOapg.properties.api_application_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        requester_email_address: typing.Union[MetaOapg.properties.requester_email_address, str, schemas.Unset] = schemas.unset,
        custom_requester_name: typing.Union[MetaOapg.properties.custom_requester_name, str, schemas.Unset] = schemas.unset,
        custom_requester_email: typing.Union[MetaOapg.properties.custom_requester_email, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        subject: typing.Union[MetaOapg.properties.subject, str, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
        recipients: typing.Union['DocumentResponseRecipients', schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        reminders: typing.Union[MetaOapg.properties.reminders, bool, schemas.Unset] = schemas.unset,
        archived: typing.Union[MetaOapg.properties.archived, bool, schemas.Unset] = schemas.unset,
        embedded: typing.Union[MetaOapg.properties.embedded, bool, schemas.Unset] = schemas.unset,
        embedded_edit_url: typing.Union[MetaOapg.properties.embedded_edit_url, str, schemas.Unset] = schemas.unset,
        embedded_preview_url: typing.Union[MetaOapg.properties.embedded_preview_url, str, schemas.Unset] = schemas.unset,
        apply_signing_order: typing.Union[MetaOapg.properties.apply_signing_order, bool, schemas.Unset] = schemas.unset,
        redirect_url: typing.Union[MetaOapg.properties.redirect_url, str, schemas.Unset] = schemas.unset,
        decline_redirect_url: typing.Union[MetaOapg.properties.decline_redirect_url, str, schemas.Unset] = schemas.unset,
        expires_in: typing.Union[MetaOapg.properties.expires_in, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        attachment_requests: typing.Union['DocumentResponseAttachmentRequests', schemas.Unset] = schemas.unset,
        files: typing.Union['DocumentResponseFiles', schemas.Unset] = schemas.unset,
        copied_contacts: typing.Union['DocumentResponseCopiedContacts', schemas.Unset] = schemas.unset,
        fields: typing.Union['DocumentResponseFields', schemas.Unset] = schemas.unset,
        allow_decline: typing.Union[MetaOapg.properties.allow_decline, bool, schemas.Unset] = schemas.unset,
        allow_reassign: typing.Union[MetaOapg.properties.allow_reassign, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentResponse':
        return super().__new__(
            cls,
            *args,
            test_mode=test_mode,
            id=id,
            api_application_id=api_application_id,
            requester_email_address=requester_email_address,
            custom_requester_name=custom_requester_name,
            custom_requester_email=custom_requester_email,
            name=name,
            subject=subject,
            message=message,
            metadata=metadata,
            created_at=created_at,
            updated_at=updated_at,
            recipients=recipients,
            status=status,
            reminders=reminders,
            archived=archived,
            embedded=embedded,
            embedded_edit_url=embedded_edit_url,
            embedded_preview_url=embedded_preview_url,
            apply_signing_order=apply_signing_order,
            redirect_url=redirect_url,
            decline_redirect_url=decline_redirect_url,
            expires_in=expires_in,
            attachment_requests=attachment_requests,
            files=files,
            copied_contacts=copied_contacts,
            fields=fields,
            allow_decline=allow_decline,
            allow_reassign=allow_reassign,
            _configuration=_configuration,
            **kwargs,
        )

from sign_well_python_sdk.model.document_response_attachment_requests import DocumentResponseAttachmentRequests
from sign_well_python_sdk.model.document_response_copied_contacts import DocumentResponseCopiedContacts
from sign_well_python_sdk.model.document_response_fields import DocumentResponseFields
from sign_well_python_sdk.model.document_response_files import DocumentResponseFiles
from sign_well_python_sdk.model.document_response_recipients import DocumentResponseRecipients
