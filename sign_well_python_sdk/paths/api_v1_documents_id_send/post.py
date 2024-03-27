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

from sign_well_python_sdk.model.document_update_and_send422_response import DocumentUpdateAndSend422Response as DocumentUpdateAndSend422ResponseSchema
from sign_well_python_sdk.model.update_document_and_send_request import UpdateDocumentAndSendRequest as UpdateDocumentAndSendRequestSchema
from sign_well_python_sdk.model.document_update_and_send_response import DocumentUpdateAndSendResponse as DocumentUpdateAndSendResponseSchema
from sign_well_python_sdk.model.expires_in_map import ExpiresInMap as ExpiresInMapSchema

from sign_well_python_sdk.type.document_update_and_send_response import DocumentUpdateAndSendResponse
from sign_well_python_sdk.type.update_document_and_send_request import UpdateDocumentAndSendRequest
from sign_well_python_sdk.type.expires_in_map import ExpiresInMap
from sign_well_python_sdk.type.document_update_and_send422_response import DocumentUpdateAndSend422Response

from ...api_client import Dictionary
from sign_well_python_sdk.pydantic.update_document_and_send_request import UpdateDocumentAndSendRequest as UpdateDocumentAndSendRequestPydantic
from sign_well_python_sdk.pydantic.document_update_and_send422_response import DocumentUpdateAndSend422Response as DocumentUpdateAndSend422ResponsePydantic
from sign_well_python_sdk.pydantic.document_update_and_send_response import DocumentUpdateAndSendResponse as DocumentUpdateAndSendResponsePydantic
from sign_well_python_sdk.pydantic.expires_in_map import ExpiresInMap as ExpiresInMapPydantic

from . import path

# Path params
IdSchema = schemas.UUIDSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'id': typing.Union[IdSchema, str, uuid.UUID, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_id = api_client.PathParameter(
    name="id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = UpdateDocumentAndSendRequestSchema


request_body_update_document_and_send_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'api_key',
]
SchemaFor201ResponseBodyApplicationJson = DocumentUpdateAndSendResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: DocumentUpdateAndSendResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: DocumentUpdateAndSendResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = DocumentUpdateAndSend422ResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: DocumentUpdateAndSend422Response


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: DocumentUpdateAndSend422Response


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
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_and_send_mapped_args(
        self,
        id: str,
        test_mode: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        expires_in: typing.Optional[ExpiresInMap] = None,
        reminders: typing.Optional[bool] = None,
        apply_signing_order: typing.Optional[bool] = None,
        api_application_id: typing.Optional[str] = None,
        embedded_signing: typing.Optional[bool] = None,
        embedded_signing_notifications: typing.Optional[bool] = None,
        custom_requester_name: typing.Optional[str] = None,
        custom_requester_email: typing.Optional[str] = None,
        redirect_url: typing.Optional[str] = None,
        allow_decline: typing.Optional[bool] = None,
        allow_reassign: typing.Optional[bool] = None,
        decline_redirect_url: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if test_mode is not None:
            _body["test_mode"] = test_mode
        if name is not None:
            _body["name"] = name
        if subject is not None:
            _body["subject"] = subject
        if message is not None:
            _body["message"] = message
        if expires_in is not None:
            _body["expires_in"] = expires_in
        if reminders is not None:
            _body["reminders"] = reminders
        if apply_signing_order is not None:
            _body["apply_signing_order"] = apply_signing_order
        if api_application_id is not None:
            _body["api_application_id"] = api_application_id
        if embedded_signing is not None:
            _body["embedded_signing"] = embedded_signing
        if embedded_signing_notifications is not None:
            _body["embedded_signing_notifications"] = embedded_signing_notifications
        if custom_requester_name is not None:
            _body["custom_requester_name"] = custom_requester_name
        if custom_requester_email is not None:
            _body["custom_requester_email"] = custom_requester_email
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
        args.body = _body
        if id is not None:
            _path_params["id"] = id
        args.path = _path_params
        return args

    async def _aupdate_and_send_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Update and Send Document
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
            path_template='/api/v1/documents/{id}/send',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_document_and_send_request.serialize(body, content_type)
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


    def _update_and_send_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Update and Send Document
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
            path_template='/api/v1/documents/{id}/send',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_document_and_send_request.serialize(body, content_type)
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


class UpdateAndSendRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_and_send(
        self,
        id: str,
        test_mode: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        expires_in: typing.Optional[ExpiresInMap] = None,
        reminders: typing.Optional[bool] = None,
        apply_signing_order: typing.Optional[bool] = None,
        api_application_id: typing.Optional[str] = None,
        embedded_signing: typing.Optional[bool] = None,
        embedded_signing_notifications: typing.Optional[bool] = None,
        custom_requester_name: typing.Optional[str] = None,
        custom_requester_email: typing.Optional[str] = None,
        redirect_url: typing.Optional[str] = None,
        allow_decline: typing.Optional[bool] = None,
        allow_reassign: typing.Optional[bool] = None,
        decline_redirect_url: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_and_send_mapped_args(
            id=id,
            test_mode=test_mode,
            name=name,
            subject=subject,
            message=message,
            expires_in=expires_in,
            reminders=reminders,
            apply_signing_order=apply_signing_order,
            api_application_id=api_application_id,
            embedded_signing=embedded_signing,
            embedded_signing_notifications=embedded_signing_notifications,
            custom_requester_name=custom_requester_name,
            custom_requester_email=custom_requester_email,
            redirect_url=redirect_url,
            allow_decline=allow_decline,
            allow_reassign=allow_reassign,
            decline_redirect_url=decline_redirect_url,
            metadata=metadata,
        )
        return await self._aupdate_and_send_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_and_send(
        self,
        id: str,
        test_mode: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        expires_in: typing.Optional[ExpiresInMap] = None,
        reminders: typing.Optional[bool] = None,
        apply_signing_order: typing.Optional[bool] = None,
        api_application_id: typing.Optional[str] = None,
        embedded_signing: typing.Optional[bool] = None,
        embedded_signing_notifications: typing.Optional[bool] = None,
        custom_requester_name: typing.Optional[str] = None,
        custom_requester_email: typing.Optional[str] = None,
        redirect_url: typing.Optional[str] = None,
        allow_decline: typing.Optional[bool] = None,
        allow_reassign: typing.Optional[bool] = None,
        decline_redirect_url: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_and_send_mapped_args(
            id=id,
            test_mode=test_mode,
            name=name,
            subject=subject,
            message=message,
            expires_in=expires_in,
            reminders=reminders,
            apply_signing_order=apply_signing_order,
            api_application_id=api_application_id,
            embedded_signing=embedded_signing,
            embedded_signing_notifications=embedded_signing_notifications,
            custom_requester_name=custom_requester_name,
            custom_requester_email=custom_requester_email,
            redirect_url=redirect_url,
            allow_decline=allow_decline,
            allow_reassign=allow_reassign,
            decline_redirect_url=decline_redirect_url,
            metadata=metadata,
        )
        return self._update_and_send_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateAndSend(BaseApi):

    async def aupdate_and_send(
        self,
        id: str,
        test_mode: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        expires_in: typing.Optional[ExpiresInMap] = None,
        reminders: typing.Optional[bool] = None,
        apply_signing_order: typing.Optional[bool] = None,
        api_application_id: typing.Optional[str] = None,
        embedded_signing: typing.Optional[bool] = None,
        embedded_signing_notifications: typing.Optional[bool] = None,
        custom_requester_name: typing.Optional[str] = None,
        custom_requester_email: typing.Optional[str] = None,
        redirect_url: typing.Optional[str] = None,
        allow_decline: typing.Optional[bool] = None,
        allow_reassign: typing.Optional[bool] = None,
        decline_redirect_url: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        validate: bool = False,
        **kwargs,
    ) -> DocumentUpdateAndSendResponsePydantic:
        raw_response = await self.raw.aupdate_and_send(
            id=id,
            test_mode=test_mode,
            name=name,
            subject=subject,
            message=message,
            expires_in=expires_in,
            reminders=reminders,
            apply_signing_order=apply_signing_order,
            api_application_id=api_application_id,
            embedded_signing=embedded_signing,
            embedded_signing_notifications=embedded_signing_notifications,
            custom_requester_name=custom_requester_name,
            custom_requester_email=custom_requester_email,
            redirect_url=redirect_url,
            allow_decline=allow_decline,
            allow_reassign=allow_reassign,
            decline_redirect_url=decline_redirect_url,
            metadata=metadata,
            **kwargs,
        )
        if validate:
            return DocumentUpdateAndSendResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(DocumentUpdateAndSendResponsePydantic, raw_response.body)
    
    
    def update_and_send(
        self,
        id: str,
        test_mode: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        expires_in: typing.Optional[ExpiresInMap] = None,
        reminders: typing.Optional[bool] = None,
        apply_signing_order: typing.Optional[bool] = None,
        api_application_id: typing.Optional[str] = None,
        embedded_signing: typing.Optional[bool] = None,
        embedded_signing_notifications: typing.Optional[bool] = None,
        custom_requester_name: typing.Optional[str] = None,
        custom_requester_email: typing.Optional[str] = None,
        redirect_url: typing.Optional[str] = None,
        allow_decline: typing.Optional[bool] = None,
        allow_reassign: typing.Optional[bool] = None,
        decline_redirect_url: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        validate: bool = False,
    ) -> DocumentUpdateAndSendResponsePydantic:
        raw_response = self.raw.update_and_send(
            id=id,
            test_mode=test_mode,
            name=name,
            subject=subject,
            message=message,
            expires_in=expires_in,
            reminders=reminders,
            apply_signing_order=apply_signing_order,
            api_application_id=api_application_id,
            embedded_signing=embedded_signing,
            embedded_signing_notifications=embedded_signing_notifications,
            custom_requester_name=custom_requester_name,
            custom_requester_email=custom_requester_email,
            redirect_url=redirect_url,
            allow_decline=allow_decline,
            allow_reassign=allow_reassign,
            decline_redirect_url=decline_redirect_url,
            metadata=metadata,
        )
        if validate:
            return DocumentUpdateAndSendResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(DocumentUpdateAndSendResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        id: str,
        test_mode: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        expires_in: typing.Optional[ExpiresInMap] = None,
        reminders: typing.Optional[bool] = None,
        apply_signing_order: typing.Optional[bool] = None,
        api_application_id: typing.Optional[str] = None,
        embedded_signing: typing.Optional[bool] = None,
        embedded_signing_notifications: typing.Optional[bool] = None,
        custom_requester_name: typing.Optional[str] = None,
        custom_requester_email: typing.Optional[str] = None,
        redirect_url: typing.Optional[str] = None,
        allow_decline: typing.Optional[bool] = None,
        allow_reassign: typing.Optional[bool] = None,
        decline_redirect_url: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_and_send_mapped_args(
            id=id,
            test_mode=test_mode,
            name=name,
            subject=subject,
            message=message,
            expires_in=expires_in,
            reminders=reminders,
            apply_signing_order=apply_signing_order,
            api_application_id=api_application_id,
            embedded_signing=embedded_signing,
            embedded_signing_notifications=embedded_signing_notifications,
            custom_requester_name=custom_requester_name,
            custom_requester_email=custom_requester_email,
            redirect_url=redirect_url,
            allow_decline=allow_decline,
            allow_reassign=allow_reassign,
            decline_redirect_url=decline_redirect_url,
            metadata=metadata,
        )
        return await self._aupdate_and_send_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        id: str,
        test_mode: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        expires_in: typing.Optional[ExpiresInMap] = None,
        reminders: typing.Optional[bool] = None,
        apply_signing_order: typing.Optional[bool] = None,
        api_application_id: typing.Optional[str] = None,
        embedded_signing: typing.Optional[bool] = None,
        embedded_signing_notifications: typing.Optional[bool] = None,
        custom_requester_name: typing.Optional[str] = None,
        custom_requester_email: typing.Optional[str] = None,
        redirect_url: typing.Optional[str] = None,
        allow_decline: typing.Optional[bool] = None,
        allow_reassign: typing.Optional[bool] = None,
        decline_redirect_url: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_and_send_mapped_args(
            id=id,
            test_mode=test_mode,
            name=name,
            subject=subject,
            message=message,
            expires_in=expires_in,
            reminders=reminders,
            apply_signing_order=apply_signing_order,
            api_application_id=api_application_id,
            embedded_signing=embedded_signing,
            embedded_signing_notifications=embedded_signing_notifications,
            custom_requester_name=custom_requester_name,
            custom_requester_email=custom_requester_email,
            redirect_url=redirect_url,
            allow_decline=allow_decline,
            allow_reassign=allow_reassign,
            decline_redirect_url=decline_redirect_url,
            metadata=metadata,
        )
        return self._update_and_send_oapg(
            body=args.body,
            path_params=args.path,
        )

