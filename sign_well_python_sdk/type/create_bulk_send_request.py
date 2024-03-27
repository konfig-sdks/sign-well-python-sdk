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

from sign_well_python_sdk.type.template_ids_param_map import TemplateIdsParamMap

class RequiredCreateBulkSendRequest(TypedDict):
    template_ids: TemplateIdsParamMap

    # A RFC 4648 base64 string of the template CSV file to be validated.
    bulk_send_csv: str

class OptionalCreateBulkSendRequest(TypedDict, total=False):
    # Whether to skip errors in the rows. Defaults to `false`.
    skip_row_errors: bool

    # Unique identifier for API Application settings to use. API Applications are optional and mainly used when isolating OAuth apps or for more control over embedded API settings
    api_application_id: str

    # The name of the Bulk Send. Will be used as the document name for each of the documents.
    name: str

    # Email subject for the signature request that recipients will see. Defaults to the default system subject or a template subject.
    subject: str

    # Email message for the signature request that recipients will see. Defaults to the default system message or a template message.
    message: str

    # When set to `true` recipients will sign one at a time in the order of the `recipients` collection of this request.
    apply_signing_order: bool

    # Sets the custom requester name for the document. When set, this is the name used for all email communications, signing notifications, and in the audit file.
    custom_requester_name: str

    # Sets the custom requester email for the document. When set, this is the email used for all email communications, signing notifications, and in the audit file.
    custom_requester_email: str

class CreateBulkSendRequest(RequiredCreateBulkSendRequest, OptionalCreateBulkSendRequest):
    pass
