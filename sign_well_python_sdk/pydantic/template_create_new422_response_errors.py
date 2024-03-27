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

from sign_well_python_sdk.pydantic.template_create_new422_response_errors_api_application_id import TemplateCreateNew422ResponseErrorsApiApplicationId
from sign_well_python_sdk.pydantic.template_create_new422_response_errors_attachment_requests import TemplateCreateNew422ResponseErrorsAttachmentRequests
from sign_well_python_sdk.pydantic.template_create_new422_response_errors_decline_redirect_url import TemplateCreateNew422ResponseErrorsDeclineRedirectUrl
from sign_well_python_sdk.pydantic.template_create_new422_response_errors_expires_in import TemplateCreateNew422ResponseErrorsExpiresIn
from sign_well_python_sdk.pydantic.template_create_new422_response_errors_fields import TemplateCreateNew422ResponseErrorsFields
from sign_well_python_sdk.pydantic.template_create_new422_response_errors_files import TemplateCreateNew422ResponseErrorsFiles
from sign_well_python_sdk.pydantic.template_create_new422_response_errors_message import TemplateCreateNew422ResponseErrorsMessage
from sign_well_python_sdk.pydantic.template_create_new422_response_errors_metadata import TemplateCreateNew422ResponseErrorsMetadata
from sign_well_python_sdk.pydantic.template_create_new422_response_errors_name import TemplateCreateNew422ResponseErrorsName
from sign_well_python_sdk.pydantic.template_create_new422_response_errors_placeholders import TemplateCreateNew422ResponseErrorsPlaceholders
from sign_well_python_sdk.pydantic.template_create_new422_response_errors_redirect_url import TemplateCreateNew422ResponseErrorsRedirectUrl
from sign_well_python_sdk.pydantic.template_create_new422_response_errors_subject import TemplateCreateNew422ResponseErrorsSubject

class TemplateCreateNew422ResponseErrors(BaseModel):
    name: typing.Optional[TemplateCreateNew422ResponseErrorsName] = Field(None, alias='name')

    decline_redirect_url: typing.Optional[TemplateCreateNew422ResponseErrorsDeclineRedirectUrl] = Field(None, alias='decline_redirect_url')

    redirect_url: typing.Optional[TemplateCreateNew422ResponseErrorsRedirectUrl] = Field(None, alias='redirect_url')

    expires_in: typing.Optional[TemplateCreateNew422ResponseErrorsExpiresIn] = Field(None, alias='expires_in')

    metadata: typing.Optional[TemplateCreateNew422ResponseErrorsMetadata] = Field(None, alias='metadata')

    api_application_id: typing.Optional[TemplateCreateNew422ResponseErrorsApiApplicationId] = Field(None, alias='api_application_id')

    subject: typing.Optional[TemplateCreateNew422ResponseErrorsSubject] = Field(None, alias='subject')

    message: typing.Optional[TemplateCreateNew422ResponseErrorsMessage] = Field(None, alias='message')

    placeholders: typing.Optional[TemplateCreateNew422ResponseErrorsPlaceholders] = Field(None, alias='placeholders')

    attachment_requests: typing.Optional[TemplateCreateNew422ResponseErrorsAttachmentRequests] = Field(None, alias='attachment_requests')

    fields: typing.Optional[TemplateCreateNew422ResponseErrorsFields] = Field(None, alias='fields')

    files: typing.Optional[TemplateCreateNew422ResponseErrorsFiles] = Field(None, alias='files')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )