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

from sign_well_python_sdk.pydantic.template_update_existing_template422_response_errors_api_application_id import TemplateUpdateExistingTemplate422ResponseErrorsApiApplicationId
from sign_well_python_sdk.pydantic.template_update_existing_template422_response_errors_decline_redirect_url import TemplateUpdateExistingTemplate422ResponseErrorsDeclineRedirectUrl
from sign_well_python_sdk.pydantic.template_update_existing_template422_response_errors_expires_in import TemplateUpdateExistingTemplate422ResponseErrorsExpiresIn
from sign_well_python_sdk.pydantic.template_update_existing_template422_response_errors_message import TemplateUpdateExistingTemplate422ResponseErrorsMessage
from sign_well_python_sdk.pydantic.template_update_existing_template422_response_errors_metadata import TemplateUpdateExistingTemplate422ResponseErrorsMetadata
from sign_well_python_sdk.pydantic.template_update_existing_template422_response_errors_name import TemplateUpdateExistingTemplate422ResponseErrorsName
from sign_well_python_sdk.pydantic.template_update_existing_template422_response_errors_redirect_url import TemplateUpdateExistingTemplate422ResponseErrorsRedirectUrl
from sign_well_python_sdk.pydantic.template_update_existing_template422_response_errors_subject import TemplateUpdateExistingTemplate422ResponseErrorsSubject

class TemplateUpdateExistingTemplate422ResponseErrors(BaseModel):
    name: typing.Optional[TemplateUpdateExistingTemplate422ResponseErrorsName] = Field(None, alias='name')

    decline_redirect_url: typing.Optional[TemplateUpdateExistingTemplate422ResponseErrorsDeclineRedirectUrl] = Field(None, alias='decline_redirect_url')

    redirect_url: typing.Optional[TemplateUpdateExistingTemplate422ResponseErrorsRedirectUrl] = Field(None, alias='redirect_url')

    expires_in: typing.Optional[TemplateUpdateExistingTemplate422ResponseErrorsExpiresIn] = Field(None, alias='expires_in')

    metadata: typing.Optional[TemplateUpdateExistingTemplate422ResponseErrorsMetadata] = Field(None, alias='metadata')

    api_application_id: typing.Optional[TemplateUpdateExistingTemplate422ResponseErrorsApiApplicationId] = Field(None, alias='api_application_id')

    subject: typing.Optional[TemplateUpdateExistingTemplate422ResponseErrorsSubject] = Field(None, alias='subject')

    message: typing.Optional[TemplateUpdateExistingTemplate422ResponseErrorsMessage] = Field(None, alias='message')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
