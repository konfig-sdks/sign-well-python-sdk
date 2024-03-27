# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from sign_well_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_V1_DOCUMENTS_ID_REMIND = "/api/v1/documents/{id}/remind"
    API_V1_BULK_SENDS_ID = "/api/v1/bulk_sends/{id}"
    API_V1_BULK_SENDS = "/api/v1/bulk_sends"
    API_V1_BULK_SENDS_CSV_TEMPLATE = "/api/v1/bulk_sends/csv_template"
    API_V1_BULK_SENDS_VALIDATE_CSV = "/api/v1/bulk_sends/validate_csv"
    API_V1_BULK_SENDS_ID_DOCUMENTS = "/api/v1/bulk_sends/{id}/documents"
    API_V1_DOCUMENTS_ID = "/api/v1/documents/{id}"
    API_V1_DOCUMENTS = "/api/v1/documents"
    API_V1_DOCUMENT_TEMPLATES_DOCUMENTS = "/api/v1/document_templates/documents"
    API_V1_DOCUMENTS_ID_SEND = "/api/v1/documents/{id}/send"
    API_V1_DOCUMENTS_ID_COMPLETED_PDF = "/api/v1/documents/{id}/completed_pdf"
    API_V1_DOCUMENT_TEMPLATES_ID = "/api/v1/document_templates/{id}"
    API_V1_DOCUMENT_TEMPLATES = "/api/v1/document_templates"
    API_V1_API_APPLICATIONS_ID = "/api/v1/api_applications/{id}"
    API_V1_HOOKS = "/api/v1/hooks"
    API_V1_HOOKS_ID = "/api/v1/hooks/{id}"
    API_V1_ME = "/api/v1/me"
