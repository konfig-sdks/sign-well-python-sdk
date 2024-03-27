import typing_extensions

from sign_well_python_sdk.apis.tags import TagValues
from sign_well_python_sdk.apis.tags.document_api import DocumentApi
from sign_well_python_sdk.apis.tags.bulk_send_api import BulkSendApi
from sign_well_python_sdk.apis.tags.template_api import TemplateApi
from sign_well_python_sdk.apis.tags.webhooks_api import WebhooksApi
from sign_well_python_sdk.apis.tags.api_application_api import APIApplicationApi
from sign_well_python_sdk.apis.tags.me_api import MeApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DOCUMENT: DocumentApi,
        TagValues.BULK_SEND: BulkSendApi,
        TagValues.TEMPLATE: TemplateApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.API_APPLICATION: APIApplicationApi,
        TagValues.ME: MeApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DOCUMENT: DocumentApi,
        TagValues.BULK_SEND: BulkSendApi,
        TagValues.TEMPLATE: TemplateApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.API_APPLICATION: APIApplicationApi,
        TagValues.ME: MeApi,
    }
)
