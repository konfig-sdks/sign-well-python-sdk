# coding: utf-8

"""
    Resources and endpoints

    When I started SignWell in 2019, I saw there was a need for an alternative to the hard-to-use and expensive e-signature software already out there. Documents can be complicated enough, but getting a document signed shouldn't be complicated too.  At SignWell, we pride ourselves not only on the ease and affordability of our e-signature process but also on our personalized and industry-leading customer support — whether it's for individual use or larger team accounts, SignWell is here to help you feel comfortable and confident getting your documents signed.  The SignWell mission? Simplify how documents get signed for millions of people and businesses. We're excited to help you continue to move toward the future of paperless document signing.  Ruben Gamez Founder, SignWell

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from sign_well_python_sdk.paths.api_v1_hooks_id.delete import DeleteCallbackUrlRaw
from sign_well_python_sdk.paths.api_v1_hooks.get import GetAllRaw
from sign_well_python_sdk.paths.api_v1_hooks.post import RegisterCallbackUrlRaw


class WebhooksApiRaw(
    DeleteCallbackUrlRaw,
    GetAllRaw,
    RegisterCallbackUrlRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
