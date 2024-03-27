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

from sign_well_python_sdk.pydantic.document_template_response_copied_placeholders import DocumentTemplateResponseCopiedPlaceholders
from sign_well_python_sdk.pydantic.document_template_response_fields import DocumentTemplateResponseFields
from sign_well_python_sdk.pydantic.document_template_response_files import DocumentTemplateResponseFiles
from sign_well_python_sdk.pydantic.document_template_response_placeholders import DocumentTemplateResponsePlaceholders

class DocumentTemplateResponse(BaseModel):
    id: str = Field(alias='id')

    api_application_id: typing.Optional[str] = Field(None, alias='api_application_id')

    requester_email_address: typing.Optional[str] = Field(None, alias='requester_email_address')

    custom_requester_name: typing.Optional[str] = Field(None, alias='custom_requester_name')

    custom_requester_email: typing.Optional[str] = Field(None, alias='custom_requester_email')

    name: typing.Optional[str] = Field(None, alias='name')

    subject: typing.Optional[str] = Field(None, alias='subject')

    message: typing.Optional[str] = Field(None, alias='message')

    metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='metadata')

    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    updated_at: typing.Optional[datetime] = Field(None, alias='updated_at')

    placeholders: typing.Optional[DocumentTemplateResponsePlaceholders] = Field(None, alias='placeholders')

    copied_placeholders: typing.Optional[DocumentTemplateResponseCopiedPlaceholders] = Field(None, alias='copied_placeholders')

    status: typing.Optional[str] = Field(None, alias='status')

    reminders: typing.Optional[bool] = Field(None, alias='reminders')

    archived: typing.Optional[bool] = Field(None, alias='archived')

    template_link: typing.Optional[str] = Field(None, alias='template_link')

    apply_signing_order: typing.Optional[bool] = Field(None, alias='apply_signing_order')

    redirect_url: typing.Optional[str] = Field(None, alias='redirect_url')

    decline_redirect_url: typing.Optional[str] = Field(None, alias='decline_redirect_url')

    expires_in: typing.Optional[int] = Field(None, alias='expires_in')

    files: typing.Optional[DocumentTemplateResponseFiles] = Field(None, alias='files')

    fields: typing.Optional[DocumentTemplateResponseFields] = Field(None, alias='fields')

    allow_decline: typing.Optional[bool] = Field(None, alias='allow_decline')

    allow_reassign: typing.Optional[bool] = Field(None, alias='allow_reassign')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
