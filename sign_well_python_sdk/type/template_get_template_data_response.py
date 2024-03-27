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

from sign_well_python_sdk.type.template_get_template_data_response_copied_placeholders import TemplateGetTemplateDataResponseCopiedPlaceholders
from sign_well_python_sdk.type.template_get_template_data_response_fields import TemplateGetTemplateDataResponseFields
from sign_well_python_sdk.type.template_get_template_data_response_files import TemplateGetTemplateDataResponseFiles
from sign_well_python_sdk.type.template_get_template_data_response_placeholders import TemplateGetTemplateDataResponsePlaceholders

class RequiredTemplateGetTemplateDataResponse(TypedDict):
    pass

class OptionalTemplateGetTemplateDataResponse(TypedDict, total=False):
    id: str

    archived: bool

    embedded_edit_url: str

    name: str

    requester_email_address: str

    status: str

    created_at: str

    updated_at: str

    template_link: str

    allow_decline: typing.Optional[str]

    allow_reassign: typing.Optional[str]

    api_application_id: typing.Optional[str]

    decline_redirect_url: typing.Optional[str]

    expires_in: typing.Optional[str]

    redirect_url: typing.Optional[str]

    reminders: typing.Optional[str]

    metadata: typing.Optional[str]

    apply_signing_order: bool

    message: str

    subject: str

    fields: TemplateGetTemplateDataResponseFields

    files: TemplateGetTemplateDataResponseFiles

    copied_placeholders: TemplateGetTemplateDataResponseCopiedPlaceholders

    placeholders: TemplateGetTemplateDataResponsePlaceholders

class TemplateGetTemplateDataResponse(RequiredTemplateGetTemplateDataResponse, OptionalTemplateGetTemplateDataResponse):
    pass
