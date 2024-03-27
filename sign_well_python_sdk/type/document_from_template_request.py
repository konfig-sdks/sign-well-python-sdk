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

from sign_well_python_sdk.type.additional_fields_map import AdditionalFieldsMap
from sign_well_python_sdk.type.additional_files_map import AdditionalFilesMap
from sign_well_python_sdk.type.attachment_requests_map import AttachmentRequestsMap
from sign_well_python_sdk.type.copied_contacts_map import CopiedContactsMap
from sign_well_python_sdk.type.expires_in_map import ExpiresInMap
from sign_well_python_sdk.type.template_fields_map import TemplateFieldsMap
from sign_well_python_sdk.type.template_ids_map import TemplateIdsMap
from sign_well_python_sdk.type.template_recipients_map import TemplateRecipientsMap

class RequiredDocumentFromTemplateRequest(TypedDict):
    recipients: TemplateRecipientsMap

class OptionalDocumentFromTemplateRequest(TypedDict, total=False):
    # Set to `true` to enable Test Mode. Documents created with Test Mode do not count towards API billing and are not legally binding. Defaults to `false`
    test_mode: bool

    # Use when you have to create a document from a single template. Either :template_id or :template_ids must be present in the request, not both.
    template_id: str

    template_ids: TemplateIdsMap

    # The name of the document.
    name: str

    # Email subject for the signature request that recipients will see. Defaults to the default system subject or a template subject (if the document is created from a template).
    subject: str

    # Email message for the signature request that recipients will see. Defaults to the default system message or a template message (if the document is created from a template).
    message: str

    # Whether the document can still be updated before sending a signature request. If set to `false` the document is sent for signing as part of this request. Defaults to `false`.
    draft: bool

    # When set to `true` the document will have a signature page added to the end, and all signers will be required to add their signature on that page.
    with_signature_page: bool

    expires_in: ExpiresInMap

    # Whether to send signing reminders to recipients. Reminders are sent on day 3, day 6, and day 10 if set to `true`. Defaults to `true`.
    reminders: bool

    # When set to `true` recipients will sign one at a time in the order of the `recipients` collection of this request.
    apply_signing_order: bool

    # Unique identifier for API Application settings to use. API Applications are optional and mainly used when isolating OAuth apps or for more control over embedded API settings
    api_application_id: str

    # When set to `true` it enables embedded signing in your website/web application. Embedded functionality works with an iFrame and email authentication is disabled. :embedded_signinig defaults to `false`.
    embedded_signing: bool

    # On embedding signing, document owners (and CC'd contacts) do not get a notification email when documents have been completed. Setting this param to `true` will send out those final completed notifications. Default is `false`
    embedded_signing_notifications: bool

    # An alternative way (if you can’t use the recommended way) of placing fields in specific locations of your document by using special text tags. Useful when changing the content of your files changes the location of fields. See API documentation for “Text Tags” for details. Defaults to false.
    text_tags: bool

    # Sets the custom requester name for the document. When set, this is the name used for all email communications, signing notifications, and in the audit file.
    custom_requester_name: str

    # Sets the custom requester email for the document. When set, this is the email used for all email communications, signing notifications, and in the audit file.
    custom_requester_email: str

    # A URL that recipients are redirected to after successfully signing a document.
    redirect_url: str

    # Whether to allow recipients the option to decline signing a document. If multiple signers are involved in a document, any single recipient can cancel the entire document signing process by declining to sign.
    allow_decline: bool

    # In some cases a signer is not the right person to sign and may need to reassign their signing responsibilities to another person. This feature allows them to reassign the document to someone else.
    allow_reassign: bool

    # A URL that recipients are redirected to if the document is declined.
    decline_redirect_url: str

    # Optional key-value data that can be associated with the document. If set, will be available every time the document data is returned.
    metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    template_fields: TemplateFieldsMap

    files: AdditionalFilesMap

    fields: AdditionalFieldsMap

    attachment_requests: AttachmentRequestsMap

    copied_contacts: CopiedContactsMap

class DocumentFromTemplateRequest(RequiredDocumentFromTemplateRequest, OptionalDocumentFromTemplateRequest):
    pass