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


class DocumentResponseAttachmentRequests(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['DocumentResponseAttachmentRequestsItem']:
            return DocumentResponseAttachmentRequestsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['DocumentResponseAttachmentRequestsItem'], typing.List['DocumentResponseAttachmentRequestsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DocumentResponseAttachmentRequests':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'DocumentResponseAttachmentRequestsItem':
        return super().__getitem__(i)

from sign_well_python_sdk.model.document_response_attachment_requests_item import DocumentResponseAttachmentRequestsItem
