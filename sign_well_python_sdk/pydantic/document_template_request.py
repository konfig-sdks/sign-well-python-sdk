# coding: utf-8

"""
    Resources and endpoints

    When I started SignWell in 2019, I saw there was a need for an alternative to the hard-to-use and expensive e-signature software already out there. Documents can be complicated enough, but getting a document signed shouldn't be complicated too.  At SignWell, we pride ourselves not only on the ease and affordability of our e-signature process but also on our personalized and industry-leading customer support — whether it's for individual use or larger team accounts, SignWell is here to help you feel comfortable and confident getting your documents signed.  The SignWell mission? Simplify how documents get signed for millions of people and businesses. We're excited to help you continue to move toward the future of paperless document signing.  Ruben Gamez Founder, SignWell

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from sign_well_python_sdk.pydantic.attachment_requests_for_template_map import AttachmentRequestsForTemplateMap
from sign_well_python_sdk.pydantic.copied_placeholders_map import CopiedPlaceholdersMap
from sign_well_python_sdk.pydantic.expires_in_map import ExpiresInMap
from sign_well_python_sdk.pydantic.fields_for_template_map import FieldsForTemplateMap
from sign_well_python_sdk.pydantic.files_map import FilesMap
from sign_well_python_sdk.pydantic.placeholders_map import PlaceholdersMap

class DocumentTemplateRequest(BaseModel):
    files: FilesMap = Field(alias='files')

    placeholders: PlaceholdersMap = Field(alias='placeholders')

    # The name of the template.
    name: typing.Optional[str] = Field(None, alias='name')

    # Email subject for the signature request that recipients will see. Defaults to the default system subject or a template subject (if the document is created from a template).
    subject: typing.Optional[str] = Field(None, alias='subject')

    # Email message for the signature request that recipients will see. Defaults to the default system message or a template message (if the document is created from a template).
    message: typing.Optional[str] = Field(None, alias='message')

    copied_placeholders: typing.Optional[CopiedPlaceholdersMap] = Field(None, alias='copied_placeholders')

    # Whether the template can still be updated before it is ready for usage. If set to `false` the template is marked as `Available` and it will be ready for use. Defaults to `false`.
    draft: typing.Optional[bool] = Field(None, alias='draft')

    expires_in: typing.Optional[ExpiresInMap] = Field(None, alias='expires_in')

    # Whether to send signing reminders to recipients. Reminders are sent on day 3, day 6, and day 10 if set to `true`. Defaults to `true`.
    reminders: typing.Optional[bool] = Field(None, alias='reminders')

    # When set to `true` recipients will sign one at a time in the order of the `recipients` collection of this request.
    apply_signing_order: typing.Optional[bool] = Field(None, alias='apply_signing_order')

    # Unique identifier for API Application settings to use. API Applications are optional and mainly used when isolating OAuth apps or for more control over embedded API settings
    api_application_id: typing.Optional[str] = Field(None, alias='api_application_id')

    # An alternative way (if you can’t use the recommended way) of placing fields in specific locations of your document by using special text tags. Useful when changing the content of your files changes the location of fields. See API documentation for “Text Tags” for details. Defaults to false.
    text_tags: typing.Optional[bool] = Field(None, alias='text_tags')

    # A URL that recipients are redirected to after successfully signing a document.
    redirect_url: typing.Optional[str] = Field(None, alias='redirect_url')

    # Whether to allow recipients the option to decline signing a document. If multiple signers are involved in a document, any single recipient can cancel the entire document signing process by declining to sign.
    allow_decline: typing.Optional[bool] = Field(None, alias='allow_decline')

    # In some cases a signer is not the right person to sign and may need to reassign their signing responsibilities to another person. This feature allows them to reassign the document to someone else.
    allow_reassign: typing.Optional[bool] = Field(None, alias='allow_reassign')

    # A URL that recipients are redirected to if the document is declined.
    decline_redirect_url: typing.Optional[str] = Field(None, alias='decline_redirect_url')

    # Optional key-value data that can be associated with the document. If set, will be available every time the document data is returned.
    metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='metadata')

    fields: typing.Optional[FieldsForTemplateMap] = Field(None, alias='fields')

    attachment_requests: typing.Optional[AttachmentRequestsForTemplateMap] = Field(None, alias='attachment_requests')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
