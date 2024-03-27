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

from sign_well_python_sdk.type.template_update_existing_template_response_copied_placeholders import TemplateUpdateExistingTemplateResponseCopiedPlaceholders
from sign_well_python_sdk.type.template_update_existing_template_response_fields import TemplateUpdateExistingTemplateResponseFields
from sign_well_python_sdk.type.template_update_existing_template_response_files import TemplateUpdateExistingTemplateResponseFiles
from sign_well_python_sdk.type.template_update_existing_template_response_metadata import TemplateUpdateExistingTemplateResponseMetadata
from sign_well_python_sdk.type.template_update_existing_template_response_placeholders import TemplateUpdateExistingTemplateResponsePlaceholders

class RequiredTemplateUpdateExistingTemplateResponse(TypedDict):
    pass

class OptionalTemplateUpdateExistingTemplateResponse(TypedDict, total=False):
    id: str

    archived: bool

    embedded_edit_url: str

    name: str

    requester_email_address: str

    status: str

    created_at: str

    updated_at: str

    template_link: str

    allow_decline: bool

    allow_reassign: bool

    api_application_id: str

    decline_redirect_url: str

    expires_in: typing.Union[int, float]

    redirect_url: str

    reminders: bool

    metadata: TemplateUpdateExistingTemplateResponseMetadata

    apply_signing_order: bool

    message: str

    subject: str

    fields: TemplateUpdateExistingTemplateResponseFields

    files: TemplateUpdateExistingTemplateResponseFiles

    copied_placeholders: TemplateUpdateExistingTemplateResponseCopiedPlaceholders

    placeholders: TemplateUpdateExistingTemplateResponsePlaceholders

class TemplateUpdateExistingTemplateResponse(RequiredTemplateUpdateExistingTemplateResponse, OptionalTemplateUpdateExistingTemplateResponse):
    pass