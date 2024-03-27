import typing_extensions

from sign_well_python_sdk.paths import PathValues
from sign_well_python_sdk.apis.paths.api_v1_documents_id_remind import ApiV1DocumentsIdRemind
from sign_well_python_sdk.apis.paths.api_v1_bulk_sends_id import ApiV1BulkSendsId
from sign_well_python_sdk.apis.paths.api_v1_bulk_sends import ApiV1BulkSends
from sign_well_python_sdk.apis.paths.api_v1_bulk_sends_csv_template import ApiV1BulkSendsCsvTemplate
from sign_well_python_sdk.apis.paths.api_v1_bulk_sends_validate_csv import ApiV1BulkSendsValidateCsv
from sign_well_python_sdk.apis.paths.api_v1_bulk_sends_id_documents import ApiV1BulkSendsIdDocuments
from sign_well_python_sdk.apis.paths.api_v1_documents_id import ApiV1DocumentsId
from sign_well_python_sdk.apis.paths.api_v1_documents import ApiV1Documents
from sign_well_python_sdk.apis.paths.api_v1_document_templates_documents import ApiV1DocumentTemplatesDocuments
from sign_well_python_sdk.apis.paths.api_v1_documents_id_send import ApiV1DocumentsIdSend
from sign_well_python_sdk.apis.paths.api_v1_documents_id_completed_pdf import ApiV1DocumentsIdCompletedPdf
from sign_well_python_sdk.apis.paths.api_v1_document_templates_id import ApiV1DocumentTemplatesId
from sign_well_python_sdk.apis.paths.api_v1_document_templates import ApiV1DocumentTemplates
from sign_well_python_sdk.apis.paths.api_v1_api_applications_id import ApiV1ApiApplicationsId
from sign_well_python_sdk.apis.paths.api_v1_hooks import ApiV1Hooks
from sign_well_python_sdk.apis.paths.api_v1_hooks_id import ApiV1HooksId
from sign_well_python_sdk.apis.paths.api_v1_me import ApiV1Me

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_V1_DOCUMENTS_ID_REMIND: ApiV1DocumentsIdRemind,
        PathValues.API_V1_BULK_SENDS_ID: ApiV1BulkSendsId,
        PathValues.API_V1_BULK_SENDS: ApiV1BulkSends,
        PathValues.API_V1_BULK_SENDS_CSV_TEMPLATE: ApiV1BulkSendsCsvTemplate,
        PathValues.API_V1_BULK_SENDS_VALIDATE_CSV: ApiV1BulkSendsValidateCsv,
        PathValues.API_V1_BULK_SENDS_ID_DOCUMENTS: ApiV1BulkSendsIdDocuments,
        PathValues.API_V1_DOCUMENTS_ID: ApiV1DocumentsId,
        PathValues.API_V1_DOCUMENTS: ApiV1Documents,
        PathValues.API_V1_DOCUMENT_TEMPLATES_DOCUMENTS: ApiV1DocumentTemplatesDocuments,
        PathValues.API_V1_DOCUMENTS_ID_SEND: ApiV1DocumentsIdSend,
        PathValues.API_V1_DOCUMENTS_ID_COMPLETED_PDF: ApiV1DocumentsIdCompletedPdf,
        PathValues.API_V1_DOCUMENT_TEMPLATES_ID: ApiV1DocumentTemplatesId,
        PathValues.API_V1_DOCUMENT_TEMPLATES: ApiV1DocumentTemplates,
        PathValues.API_V1_API_APPLICATIONS_ID: ApiV1ApiApplicationsId,
        PathValues.API_V1_HOOKS: ApiV1Hooks,
        PathValues.API_V1_HOOKS_ID: ApiV1HooksId,
        PathValues.API_V1_ME: ApiV1Me,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_V1_DOCUMENTS_ID_REMIND: ApiV1DocumentsIdRemind,
        PathValues.API_V1_BULK_SENDS_ID: ApiV1BulkSendsId,
        PathValues.API_V1_BULK_SENDS: ApiV1BulkSends,
        PathValues.API_V1_BULK_SENDS_CSV_TEMPLATE: ApiV1BulkSendsCsvTemplate,
        PathValues.API_V1_BULK_SENDS_VALIDATE_CSV: ApiV1BulkSendsValidateCsv,
        PathValues.API_V1_BULK_SENDS_ID_DOCUMENTS: ApiV1BulkSendsIdDocuments,
        PathValues.API_V1_DOCUMENTS_ID: ApiV1DocumentsId,
        PathValues.API_V1_DOCUMENTS: ApiV1Documents,
        PathValues.API_V1_DOCUMENT_TEMPLATES_DOCUMENTS: ApiV1DocumentTemplatesDocuments,
        PathValues.API_V1_DOCUMENTS_ID_SEND: ApiV1DocumentsIdSend,
        PathValues.API_V1_DOCUMENTS_ID_COMPLETED_PDF: ApiV1DocumentsIdCompletedPdf,
        PathValues.API_V1_DOCUMENT_TEMPLATES_ID: ApiV1DocumentTemplatesId,
        PathValues.API_V1_DOCUMENT_TEMPLATES: ApiV1DocumentTemplates,
        PathValues.API_V1_API_APPLICATIONS_ID: ApiV1ApiApplicationsId,
        PathValues.API_V1_HOOKS: ApiV1Hooks,
        PathValues.API_V1_HOOKS_ID: ApiV1HooksId,
        PathValues.API_V1_ME: ApiV1Me,
    }
)
