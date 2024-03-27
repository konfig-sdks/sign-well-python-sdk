# coding: utf-8

"""
    Resources and endpoints

    When I started SignWell in 2019, I saw there was a need for an alternative to the hard-to-use and expensive e-signature software already out there. Documents can be complicated enough, but getting a document signed shouldn't be complicated too.  At SignWell, we pride ourselves not only on the ease and affordability of our e-signature process but also on our personalized and industry-leading customer support — whether it's for individual use or larger team accounts, SignWell is here to help you feel comfortable and confident getting your documents signed.  The SignWell mission? Simplify how documents get signed for millions of people and businesses. We're excited to help you continue to move toward the future of paperless document signing.  Ruben Gamez Founder, SignWell

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from sign_well_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from sign_well_python_sdk.api_response import AsyncGeneratorResponse
from sign_well_python_sdk import api_client, exceptions
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

from sign_well_python_sdk.model.copied_placeholders_map import CopiedPlaceholdersMap as CopiedPlaceholdersMapSchema
from sign_well_python_sdk.model.fields_for_template_map import FieldsForTemplateMap as FieldsForTemplateMapSchema
from sign_well_python_sdk.model.placeholders_map import PlaceholdersMap as PlaceholdersMapSchema
from sign_well_python_sdk.model.template_create_new400_response import TemplateCreateNew400Response as TemplateCreateNew400ResponseSchema
from sign_well_python_sdk.model.files_map import FilesMap as FilesMapSchema
from sign_well_python_sdk.model.template_create_new422_response import TemplateCreateNew422Response as TemplateCreateNew422ResponseSchema
from sign_well_python_sdk.model.document_template_request import DocumentTemplateRequest as DocumentTemplateRequestSchema
from sign_well_python_sdk.model.template_create_new_response import TemplateCreateNewResponse as TemplateCreateNewResponseSchema
from sign_well_python_sdk.model.attachment_requests_for_template_map import AttachmentRequestsForTemplateMap as AttachmentRequestsForTemplateMapSchema
from sign_well_python_sdk.model.expires_in_map import ExpiresInMap as ExpiresInMapSchema

from sign_well_python_sdk.type.files_map import FilesMap
from sign_well_python_sdk.type.document_template_request import DocumentTemplateRequest
from sign_well_python_sdk.type.placeholders_map import PlaceholdersMap
from sign_well_python_sdk.type.template_create_new_response import TemplateCreateNewResponse
from sign_well_python_sdk.type.template_create_new422_response import TemplateCreateNew422Response
from sign_well_python_sdk.type.template_create_new400_response import TemplateCreateNew400Response
from sign_well_python_sdk.type.fields_for_template_map import FieldsForTemplateMap
from sign_well_python_sdk.type.copied_placeholders_map import CopiedPlaceholdersMap
from sign_well_python_sdk.type.expires_in_map import ExpiresInMap
from sign_well_python_sdk.type.attachment_requests_for_template_map import AttachmentRequestsForTemplateMap

from ...api_client import Dictionary
from sign_well_python_sdk.pydantic.template_create_new400_response import TemplateCreateNew400Response as TemplateCreateNew400ResponsePydantic
from sign_well_python_sdk.pydantic.copied_placeholders_map import CopiedPlaceholdersMap as CopiedPlaceholdersMapPydantic
from sign_well_python_sdk.pydantic.attachment_requests_for_template_map import AttachmentRequestsForTemplateMap as AttachmentRequestsForTemplateMapPydantic
from sign_well_python_sdk.pydantic.placeholders_map import PlaceholdersMap as PlaceholdersMapPydantic
from sign_well_python_sdk.pydantic.template_create_new_response import TemplateCreateNewResponse as TemplateCreateNewResponsePydantic
from sign_well_python_sdk.pydantic.template_create_new422_response import TemplateCreateNew422Response as TemplateCreateNew422ResponsePydantic
from sign_well_python_sdk.pydantic.fields_for_template_map import FieldsForTemplateMap as FieldsForTemplateMapPydantic
from sign_well_python_sdk.pydantic.files_map import FilesMap as FilesMapPydantic
from sign_well_python_sdk.pydantic.expires_in_map import ExpiresInMap as ExpiresInMapPydantic
from sign_well_python_sdk.pydantic.document_template_request import DocumentTemplateRequest as DocumentTemplateRequestPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = DocumentTemplateRequestSchema


request_body_document_template_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'api_key',
]
SchemaFor201ResponseBodyApplicationJson = TemplateCreateNewResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: TemplateCreateNewResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: TemplateCreateNewResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = TemplateCreateNew400ResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: TemplateCreateNew400Response


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: TemplateCreateNew400Response


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = TemplateCreateNew422ResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: TemplateCreateNew422Response


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: TemplateCreateNew422Response


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
    '400': _response_for_400,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_new_mapped_args(
        self,
        files: FilesMap,
        placeholders: PlaceholdersMap,
        name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        copied_placeholders: typing.Optional[CopiedPlaceholdersMap] = None,
        draft: typing.Optional[bool] = None,
        expires_in: typing.Optional[ExpiresInMap] = None,
        reminders: typing.Optional[bool] = None,
        apply_signing_order: typing.Optional[bool] = None,
        api_application_id: typing.Optional[str] = None,
        text_tags: typing.Optional[bool] = None,
        redirect_url: typing.Optional[str] = None,
        allow_decline: typing.Optional[bool] = None,
        allow_reassign: typing.Optional[bool] = None,
        decline_redirect_url: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        fields: typing.Optional[FieldsForTemplateMap] = None,
        attachment_requests: typing.Optional[AttachmentRequestsForTemplateMap] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if files is not None:
            _body["files"] = files
        if name is not None:
            _body["name"] = name
        if subject is not None:
            _body["subject"] = subject
        if message is not None:
            _body["message"] = message
        if placeholders is not None:
            _body["placeholders"] = placeholders
        if copied_placeholders is not None:
            _body["copied_placeholders"] = copied_placeholders
        if draft is not None:
            _body["draft"] = draft
        if expires_in is not None:
            _body["expires_in"] = expires_in
        if reminders is not None:
            _body["reminders"] = reminders
        if apply_signing_order is not None:
            _body["apply_signing_order"] = apply_signing_order
        if api_application_id is not None:
            _body["api_application_id"] = api_application_id
        if text_tags is not None:
            _body["text_tags"] = text_tags
        if redirect_url is not None:
            _body["redirect_url"] = redirect_url
        if allow_decline is not None:
            _body["allow_decline"] = allow_decline
        if allow_reassign is not None:
            _body["allow_reassign"] = allow_reassign
        if decline_redirect_url is not None:
            _body["decline_redirect_url"] = decline_redirect_url
        if metadata is not None:
            _body["metadata"] = metadata
        if fields is not None:
            _body["fields"] = fields
        if attachment_requests is not None:
            _body["attachment_requests"] = attachment_requests
        args.body = _body
        return args

    async def _acreate_new_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create Template
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/document_templates',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_document_template_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_new_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create Template
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/document_templates',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_document_template_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateNewRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new(
        self,
        files: FilesMap,
        placeholders: PlaceholdersMap,
        name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        copied_placeholders: typing.Optional[CopiedPlaceholdersMap] = None,
        draft: typing.Optional[bool] = None,
        expires_in: typing.Optional[ExpiresInMap] = None,
        reminders: typing.Optional[bool] = None,
        apply_signing_order: typing.Optional[bool] = None,
        api_application_id: typing.Optional[str] = None,
        text_tags: typing.Optional[bool] = None,
        redirect_url: typing.Optional[str] = None,
        allow_decline: typing.Optional[bool] = None,
        allow_reassign: typing.Optional[bool] = None,
        decline_redirect_url: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        fields: typing.Optional[FieldsForTemplateMap] = None,
        attachment_requests: typing.Optional[AttachmentRequestsForTemplateMap] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_mapped_args(
            files=files,
            placeholders=placeholders,
            name=name,
            subject=subject,
            message=message,
            copied_placeholders=copied_placeholders,
            draft=draft,
            expires_in=expires_in,
            reminders=reminders,
            apply_signing_order=apply_signing_order,
            api_application_id=api_application_id,
            text_tags=text_tags,
            redirect_url=redirect_url,
            allow_decline=allow_decline,
            allow_reassign=allow_reassign,
            decline_redirect_url=decline_redirect_url,
            metadata=metadata,
            fields=fields,
            attachment_requests=attachment_requests,
        )
        return await self._acreate_new_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_new(
        self,
        files: FilesMap,
        placeholders: PlaceholdersMap,
        name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        copied_placeholders: typing.Optional[CopiedPlaceholdersMap] = None,
        draft: typing.Optional[bool] = None,
        expires_in: typing.Optional[ExpiresInMap] = None,
        reminders: typing.Optional[bool] = None,
        apply_signing_order: typing.Optional[bool] = None,
        api_application_id: typing.Optional[str] = None,
        text_tags: typing.Optional[bool] = None,
        redirect_url: typing.Optional[str] = None,
        allow_decline: typing.Optional[bool] = None,
        allow_reassign: typing.Optional[bool] = None,
        decline_redirect_url: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        fields: typing.Optional[FieldsForTemplateMap] = None,
        attachment_requests: typing.Optional[AttachmentRequestsForTemplateMap] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_mapped_args(
            files=files,
            placeholders=placeholders,
            name=name,
            subject=subject,
            message=message,
            copied_placeholders=copied_placeholders,
            draft=draft,
            expires_in=expires_in,
            reminders=reminders,
            apply_signing_order=apply_signing_order,
            api_application_id=api_application_id,
            text_tags=text_tags,
            redirect_url=redirect_url,
            allow_decline=allow_decline,
            allow_reassign=allow_reassign,
            decline_redirect_url=decline_redirect_url,
            metadata=metadata,
            fields=fields,
            attachment_requests=attachment_requests,
        )
        return self._create_new_oapg(
            body=args.body,
        )

class CreateNew(BaseApi):

    async def acreate_new(
        self,
        files: FilesMap,
        placeholders: PlaceholdersMap,
        name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        copied_placeholders: typing.Optional[CopiedPlaceholdersMap] = None,
        draft: typing.Optional[bool] = None,
        expires_in: typing.Optional[ExpiresInMap] = None,
        reminders: typing.Optional[bool] = None,
        apply_signing_order: typing.Optional[bool] = None,
        api_application_id: typing.Optional[str] = None,
        text_tags: typing.Optional[bool] = None,
        redirect_url: typing.Optional[str] = None,
        allow_decline: typing.Optional[bool] = None,
        allow_reassign: typing.Optional[bool] = None,
        decline_redirect_url: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        fields: typing.Optional[FieldsForTemplateMap] = None,
        attachment_requests: typing.Optional[AttachmentRequestsForTemplateMap] = None,
        validate: bool = False,
        **kwargs,
    ) -> TemplateCreateNewResponsePydantic:
        raw_response = await self.raw.acreate_new(
            files=files,
            placeholders=placeholders,
            name=name,
            subject=subject,
            message=message,
            copied_placeholders=copied_placeholders,
            draft=draft,
            expires_in=expires_in,
            reminders=reminders,
            apply_signing_order=apply_signing_order,
            api_application_id=api_application_id,
            text_tags=text_tags,
            redirect_url=redirect_url,
            allow_decline=allow_decline,
            allow_reassign=allow_reassign,
            decline_redirect_url=decline_redirect_url,
            metadata=metadata,
            fields=fields,
            attachment_requests=attachment_requests,
            **kwargs,
        )
        if validate:
            return TemplateCreateNewResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TemplateCreateNewResponsePydantic, raw_response.body)
    
    
    def create_new(
        self,
        files: FilesMap,
        placeholders: PlaceholdersMap,
        name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        copied_placeholders: typing.Optional[CopiedPlaceholdersMap] = None,
        draft: typing.Optional[bool] = None,
        expires_in: typing.Optional[ExpiresInMap] = None,
        reminders: typing.Optional[bool] = None,
        apply_signing_order: typing.Optional[bool] = None,
        api_application_id: typing.Optional[str] = None,
        text_tags: typing.Optional[bool] = None,
        redirect_url: typing.Optional[str] = None,
        allow_decline: typing.Optional[bool] = None,
        allow_reassign: typing.Optional[bool] = None,
        decline_redirect_url: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        fields: typing.Optional[FieldsForTemplateMap] = None,
        attachment_requests: typing.Optional[AttachmentRequestsForTemplateMap] = None,
        validate: bool = False,
    ) -> TemplateCreateNewResponsePydantic:
        raw_response = self.raw.create_new(
            files=files,
            placeholders=placeholders,
            name=name,
            subject=subject,
            message=message,
            copied_placeholders=copied_placeholders,
            draft=draft,
            expires_in=expires_in,
            reminders=reminders,
            apply_signing_order=apply_signing_order,
            api_application_id=api_application_id,
            text_tags=text_tags,
            redirect_url=redirect_url,
            allow_decline=allow_decline,
            allow_reassign=allow_reassign,
            decline_redirect_url=decline_redirect_url,
            metadata=metadata,
            fields=fields,
            attachment_requests=attachment_requests,
        )
        if validate:
            return TemplateCreateNewResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TemplateCreateNewResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        files: FilesMap,
        placeholders: PlaceholdersMap,
        name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        copied_placeholders: typing.Optional[CopiedPlaceholdersMap] = None,
        draft: typing.Optional[bool] = None,
        expires_in: typing.Optional[ExpiresInMap] = None,
        reminders: typing.Optional[bool] = None,
        apply_signing_order: typing.Optional[bool] = None,
        api_application_id: typing.Optional[str] = None,
        text_tags: typing.Optional[bool] = None,
        redirect_url: typing.Optional[str] = None,
        allow_decline: typing.Optional[bool] = None,
        allow_reassign: typing.Optional[bool] = None,
        decline_redirect_url: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        fields: typing.Optional[FieldsForTemplateMap] = None,
        attachment_requests: typing.Optional[AttachmentRequestsForTemplateMap] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_mapped_args(
            files=files,
            placeholders=placeholders,
            name=name,
            subject=subject,
            message=message,
            copied_placeholders=copied_placeholders,
            draft=draft,
            expires_in=expires_in,
            reminders=reminders,
            apply_signing_order=apply_signing_order,
            api_application_id=api_application_id,
            text_tags=text_tags,
            redirect_url=redirect_url,
            allow_decline=allow_decline,
            allow_reassign=allow_reassign,
            decline_redirect_url=decline_redirect_url,
            metadata=metadata,
            fields=fields,
            attachment_requests=attachment_requests,
        )
        return await self._acreate_new_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        files: FilesMap,
        placeholders: PlaceholdersMap,
        name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        copied_placeholders: typing.Optional[CopiedPlaceholdersMap] = None,
        draft: typing.Optional[bool] = None,
        expires_in: typing.Optional[ExpiresInMap] = None,
        reminders: typing.Optional[bool] = None,
        apply_signing_order: typing.Optional[bool] = None,
        api_application_id: typing.Optional[str] = None,
        text_tags: typing.Optional[bool] = None,
        redirect_url: typing.Optional[str] = None,
        allow_decline: typing.Optional[bool] = None,
        allow_reassign: typing.Optional[bool] = None,
        decline_redirect_url: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        fields: typing.Optional[FieldsForTemplateMap] = None,
        attachment_requests: typing.Optional[AttachmentRequestsForTemplateMap] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_mapped_args(
            files=files,
            placeholders=placeholders,
            name=name,
            subject=subject,
            message=message,
            copied_placeholders=copied_placeholders,
            draft=draft,
            expires_in=expires_in,
            reminders=reminders,
            apply_signing_order=apply_signing_order,
            api_application_id=api_application_id,
            text_tags=text_tags,
            redirect_url=redirect_url,
            allow_decline=allow_decline,
            allow_reassign=allow_reassign,
            decline_redirect_url=decline_redirect_url,
            metadata=metadata,
            fields=fields,
            attachment_requests=attachment_requests,
        )
        return self._create_new_oapg(
            body=args.body,
        )

