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


class RequiredFilesMapItem(TypedDict):
    # Name of the file that will be uploaded.
    name: str

class OptionalFilesMapItem(TypedDict, total=False):
    # Publicly available URL of the file to be uploaded.
    file_url: str

    # A RFC 4648 base64 string of the file to be uploaded.
    file_base64: str

class FilesMapItem(RequiredFilesMapItem, OptionalFilesMapItem):
    pass