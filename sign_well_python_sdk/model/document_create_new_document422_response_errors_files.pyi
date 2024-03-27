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


class DocumentCreateNewDocument422ResponseErrorsFiles(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def file_1() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsFilesFile1']:
                return DocumentCreateNewDocument422ResponseErrorsFilesFile1
        
            @staticmethod
            def file_2() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsFilesFile2']:
                return DocumentCreateNewDocument422ResponseErrorsFilesFile2
        
            @staticmethod
            def file_3() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsFilesFile3']:
                return DocumentCreateNewDocument422ResponseErrorsFilesFile3
        
            @staticmethod
            def file_4() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsFilesFile4']:
                return DocumentCreateNewDocument422ResponseErrorsFilesFile4
        
            @staticmethod
            def file_5() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsFilesFile5']:
                return DocumentCreateNewDocument422ResponseErrorsFilesFile5
        
            @staticmethod
            def file_6() -> typing.Type['DocumentCreateNewDocument422ResponseErrorsFilesFile6']:
                return DocumentCreateNewDocument422ResponseErrorsFilesFile6
            __annotations__ = {
                "file_1": file_1,
                "file_2": file_2,
                "file_3": file_3,
                "file_4": file_4,
                "file_5": file_5,
                "file_6": file_6,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_1"]) -> 'DocumentCreateNewDocument422ResponseErrorsFilesFile1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_2"]) -> 'DocumentCreateNewDocument422ResponseErrorsFilesFile2': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_3"]) -> 'DocumentCreateNewDocument422ResponseErrorsFilesFile3': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_4"]) -> 'DocumentCreateNewDocument422ResponseErrorsFilesFile4': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_5"]) -> 'DocumentCreateNewDocument422ResponseErrorsFilesFile5': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_6"]) -> 'DocumentCreateNewDocument422ResponseErrorsFilesFile6': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["file_1", "file_2", "file_3", "file_4", "file_5", "file_6", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_1"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsFilesFile1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_2"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsFilesFile2', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_3"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsFilesFile3', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_4"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsFilesFile4', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_5"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsFilesFile5', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_6"]) -> typing.Union['DocumentCreateNewDocument422ResponseErrorsFilesFile6', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["file_1", "file_2", "file_3", "file_4", "file_5", "file_6", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        file_1: typing.Union['DocumentCreateNewDocument422ResponseErrorsFilesFile1', schemas.Unset] = schemas.unset,
        file_2: typing.Union['DocumentCreateNewDocument422ResponseErrorsFilesFile2', schemas.Unset] = schemas.unset,
        file_3: typing.Union['DocumentCreateNewDocument422ResponseErrorsFilesFile3', schemas.Unset] = schemas.unset,
        file_4: typing.Union['DocumentCreateNewDocument422ResponseErrorsFilesFile4', schemas.Unset] = schemas.unset,
        file_5: typing.Union['DocumentCreateNewDocument422ResponseErrorsFilesFile5', schemas.Unset] = schemas.unset,
        file_6: typing.Union['DocumentCreateNewDocument422ResponseErrorsFilesFile6', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentCreateNewDocument422ResponseErrorsFiles':
        return super().__new__(
            cls,
            *args,
            file_1=file_1,
            file_2=file_2,
            file_3=file_3,
            file_4=file_4,
            file_5=file_5,
            file_6=file_6,
            _configuration=_configuration,
            **kwargs,
        )

from sign_well_python_sdk.model.document_create_new_document422_response_errors_files_file1 import DocumentCreateNewDocument422ResponseErrorsFilesFile1
from sign_well_python_sdk.model.document_create_new_document422_response_errors_files_file2 import DocumentCreateNewDocument422ResponseErrorsFilesFile2
from sign_well_python_sdk.model.document_create_new_document422_response_errors_files_file3 import DocumentCreateNewDocument422ResponseErrorsFilesFile3
from sign_well_python_sdk.model.document_create_new_document422_response_errors_files_file4 import DocumentCreateNewDocument422ResponseErrorsFilesFile4
from sign_well_python_sdk.model.document_create_new_document422_response_errors_files_file5 import DocumentCreateNewDocument422ResponseErrorsFilesFile5
from sign_well_python_sdk.model.document_create_new_document422_response_errors_files_file6 import DocumentCreateNewDocument422ResponseErrorsFilesFile6