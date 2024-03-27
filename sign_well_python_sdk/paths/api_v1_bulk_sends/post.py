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

from sign_well_python_sdk.model.bulk_send_create_validation_csv422_response import BulkSendCreateValidationCsv422Response as BulkSendCreateValidationCsv422ResponseSchema
from sign_well_python_sdk.model.create_bulk_send_request import CreateBulkSendRequest as CreateBulkSendRequestSchema
from sign_well_python_sdk.model.bulk_send_create_validation_csv401_response import BulkSendCreateValidationCsv401Response as BulkSendCreateValidationCsv401ResponseSchema
from sign_well_python_sdk.model.template_ids_param_map import TemplateIdsParamMap as TemplateIdsParamMapSchema
from sign_well_python_sdk.model.bulk_send_create_validation_csv_response import BulkSendCreateValidationCsvResponse as BulkSendCreateValidationCsvResponseSchema

from sign_well_python_sdk.type.bulk_send_create_validation_csv_response import BulkSendCreateValidationCsvResponse
from sign_well_python_sdk.type.bulk_send_create_validation_csv422_response import BulkSendCreateValidationCsv422Response
from sign_well_python_sdk.type.bulk_send_create_validation_csv401_response import BulkSendCreateValidationCsv401Response
from sign_well_python_sdk.type.create_bulk_send_request import CreateBulkSendRequest
from sign_well_python_sdk.type.template_ids_param_map import TemplateIdsParamMap

from ...api_client import Dictionary
from sign_well_python_sdk.pydantic.template_ids_param_map import TemplateIdsParamMap as TemplateIdsParamMapPydantic
from sign_well_python_sdk.pydantic.bulk_send_create_validation_csv_response import BulkSendCreateValidationCsvResponse as BulkSendCreateValidationCsvResponsePydantic
from sign_well_python_sdk.pydantic.bulk_send_create_validation_csv401_response import BulkSendCreateValidationCsv401Response as BulkSendCreateValidationCsv401ResponsePydantic
from sign_well_python_sdk.pydantic.bulk_send_create_validation_csv422_response import BulkSendCreateValidationCsv422Response as BulkSendCreateValidationCsv422ResponsePydantic
from sign_well_python_sdk.pydantic.create_bulk_send_request import CreateBulkSendRequest as CreateBulkSendRequestPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = CreateBulkSendRequestSchema


request_body_create_bulk_send_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'api_key',
]
SchemaFor201ResponseBodyApplicationJson = BulkSendCreateValidationCsvResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: BulkSendCreateValidationCsvResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: BulkSendCreateValidationCsvResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = BulkSendCreateValidationCsv401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: BulkSendCreateValidationCsv401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: BulkSendCreateValidationCsv401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = BulkSendCreateValidationCsv422ResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: BulkSendCreateValidationCsv422Response


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: BulkSendCreateValidationCsv422Response


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
    '401': _response_for_401,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_validation_csv_mapped_args(
        self,
        template_ids: TemplateIdsParamMap,
        bulk_send_csv: str,
        skip_row_errors: typing.Optional[bool] = None,
        api_application_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        apply_signing_order: typing.Optional[bool] = None,
        custom_requester_name: typing.Optional[str] = None,
        custom_requester_email: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if template_ids is not None:
            _body["template_ids"] = template_ids
        if bulk_send_csv is not None:
            _body["bulk_send_csv"] = bulk_send_csv
        if skip_row_errors is not None:
            _body["skip_row_errors"] = skip_row_errors
        if api_application_id is not None:
            _body["api_application_id"] = api_application_id
        if name is not None:
            _body["name"] = name
        if subject is not None:
            _body["subject"] = subject
        if message is not None:
            _body["message"] = message
        if apply_signing_order is not None:
            _body["apply_signing_order"] = apply_signing_order
        if custom_requester_name is not None:
            _body["custom_requester_name"] = custom_requester_name
        if custom_requester_email is not None:
            _body["custom_requester_email"] = custom_requester_email
        args.body = _body
        return args

    async def _acreate_validation_csv_oapg(
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
        Create Bulk Send
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
            path_template='/api/v1/bulk_sends',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_bulk_send_request.serialize(body, content_type)
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


    def _create_validation_csv_oapg(
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
        Create Bulk Send
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
            path_template='/api/v1/bulk_sends',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_bulk_send_request.serialize(body, content_type)
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


class CreateValidationCsvRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_validation_csv(
        self,
        template_ids: TemplateIdsParamMap,
        bulk_send_csv: str,
        skip_row_errors: typing.Optional[bool] = None,
        api_application_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        apply_signing_order: typing.Optional[bool] = None,
        custom_requester_name: typing.Optional[str] = None,
        custom_requester_email: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_validation_csv_mapped_args(
            template_ids=template_ids,
            bulk_send_csv=bulk_send_csv,
            skip_row_errors=skip_row_errors,
            api_application_id=api_application_id,
            name=name,
            subject=subject,
            message=message,
            apply_signing_order=apply_signing_order,
            custom_requester_name=custom_requester_name,
            custom_requester_email=custom_requester_email,
        )
        return await self._acreate_validation_csv_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_validation_csv(
        self,
        template_ids: TemplateIdsParamMap,
        bulk_send_csv: str,
        skip_row_errors: typing.Optional[bool] = None,
        api_application_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        apply_signing_order: typing.Optional[bool] = None,
        custom_requester_name: typing.Optional[str] = None,
        custom_requester_email: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_validation_csv_mapped_args(
            template_ids=template_ids,
            bulk_send_csv=bulk_send_csv,
            skip_row_errors=skip_row_errors,
            api_application_id=api_application_id,
            name=name,
            subject=subject,
            message=message,
            apply_signing_order=apply_signing_order,
            custom_requester_name=custom_requester_name,
            custom_requester_email=custom_requester_email,
        )
        return self._create_validation_csv_oapg(
            body=args.body,
        )

class CreateValidationCsv(BaseApi):

    async def acreate_validation_csv(
        self,
        template_ids: TemplateIdsParamMap,
        bulk_send_csv: str,
        skip_row_errors: typing.Optional[bool] = None,
        api_application_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        apply_signing_order: typing.Optional[bool] = None,
        custom_requester_name: typing.Optional[str] = None,
        custom_requester_email: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> BulkSendCreateValidationCsvResponsePydantic:
        raw_response = await self.raw.acreate_validation_csv(
            template_ids=template_ids,
            bulk_send_csv=bulk_send_csv,
            skip_row_errors=skip_row_errors,
            api_application_id=api_application_id,
            name=name,
            subject=subject,
            message=message,
            apply_signing_order=apply_signing_order,
            custom_requester_name=custom_requester_name,
            custom_requester_email=custom_requester_email,
            **kwargs,
        )
        if validate:
            return BulkSendCreateValidationCsvResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(BulkSendCreateValidationCsvResponsePydantic, raw_response.body)
    
    
    def create_validation_csv(
        self,
        template_ids: TemplateIdsParamMap,
        bulk_send_csv: str,
        skip_row_errors: typing.Optional[bool] = None,
        api_application_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        apply_signing_order: typing.Optional[bool] = None,
        custom_requester_name: typing.Optional[str] = None,
        custom_requester_email: typing.Optional[str] = None,
        validate: bool = False,
    ) -> BulkSendCreateValidationCsvResponsePydantic:
        raw_response = self.raw.create_validation_csv(
            template_ids=template_ids,
            bulk_send_csv=bulk_send_csv,
            skip_row_errors=skip_row_errors,
            api_application_id=api_application_id,
            name=name,
            subject=subject,
            message=message,
            apply_signing_order=apply_signing_order,
            custom_requester_name=custom_requester_name,
            custom_requester_email=custom_requester_email,
        )
        if validate:
            return BulkSendCreateValidationCsvResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(BulkSendCreateValidationCsvResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        template_ids: TemplateIdsParamMap,
        bulk_send_csv: str,
        skip_row_errors: typing.Optional[bool] = None,
        api_application_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        apply_signing_order: typing.Optional[bool] = None,
        custom_requester_name: typing.Optional[str] = None,
        custom_requester_email: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_validation_csv_mapped_args(
            template_ids=template_ids,
            bulk_send_csv=bulk_send_csv,
            skip_row_errors=skip_row_errors,
            api_application_id=api_application_id,
            name=name,
            subject=subject,
            message=message,
            apply_signing_order=apply_signing_order,
            custom_requester_name=custom_requester_name,
            custom_requester_email=custom_requester_email,
        )
        return await self._acreate_validation_csv_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        template_ids: TemplateIdsParamMap,
        bulk_send_csv: str,
        skip_row_errors: typing.Optional[bool] = None,
        api_application_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        apply_signing_order: typing.Optional[bool] = None,
        custom_requester_name: typing.Optional[str] = None,
        custom_requester_email: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_validation_csv_mapped_args(
            template_ids=template_ids,
            bulk_send_csv=bulk_send_csv,
            skip_row_errors=skip_row_errors,
            api_application_id=api_application_id,
            name=name,
            subject=subject,
            message=message,
            apply_signing_order=apply_signing_order,
            custom_requester_name=custom_requester_name,
            custom_requester_email=custom_requester_email,
        )
        return self._create_validation_csv_oapg(
            body=args.body,
        )
