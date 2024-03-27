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

from sign_well_python_sdk.model.bulk_send_get_csv_template404_response import BulkSendGetCsvTemplate404Response as BulkSendGetCsvTemplate404ResponseSchema
from sign_well_python_sdk.model.bulk_send_template_ids_param_map import BulkSendTemplateIdsParamMap as BulkSendTemplateIdsParamMapSchema
from sign_well_python_sdk.model.bulk_send_get_csv_template401_response import BulkSendGetCsvTemplate401Response as BulkSendGetCsvTemplate401ResponseSchema
from sign_well_python_sdk.model.bulk_send_get_csv_template200_response import BulkSendGetCsvTemplate200Response as BulkSendGetCsvTemplate200ResponseSchema

from sign_well_python_sdk.type.bulk_send_get_csv_template200_response import BulkSendGetCsvTemplate200Response
from sign_well_python_sdk.type.bulk_send_get_csv_template404_response import BulkSendGetCsvTemplate404Response
from sign_well_python_sdk.type.bulk_send_get_csv_template401_response import BulkSendGetCsvTemplate401Response
from sign_well_python_sdk.type.bulk_send_template_ids_param_map import BulkSendTemplateIdsParamMap

from ...api_client import Dictionary
from sign_well_python_sdk.pydantic.bulk_send_get_csv_template200_response import BulkSendGetCsvTemplate200Response as BulkSendGetCsvTemplate200ResponsePydantic
from sign_well_python_sdk.pydantic.bulk_send_template_ids_param_map import BulkSendTemplateIdsParamMap as BulkSendTemplateIdsParamMapPydantic
from sign_well_python_sdk.pydantic.bulk_send_get_csv_template401_response import BulkSendGetCsvTemplate401Response as BulkSendGetCsvTemplate401ResponsePydantic
from sign_well_python_sdk.pydantic.bulk_send_get_csv_template404_response import BulkSendGetCsvTemplate404Response as BulkSendGetCsvTemplate404ResponsePydantic

from . import path

# Query params
TemplateIdsSchema = BulkSendTemplateIdsParamMapSchema
Base64Schema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'template_ids[]': typing.Union[BulkSendTemplateIdsParamMapSchema, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'base64': typing.Union[Base64Schema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_template_ids_ = api_client.QueryParameter(
    name="template_ids[]",
    style=api_client.ParameterStyle.FORM,
    schema=BulkSendTemplateIdsParamMapSchema,
    required=True,
    explode=True,
)
request_query_base64 = api_client.QueryParameter(
    name="base64",
    style=api_client.ParameterStyle.FORM,
    schema=Base64Schema,
    explode=True,
)
_auth = [
    'api_key',
]
SchemaFor200ResponseBodyApplicationJson = BulkSendGetCsvTemplate200ResponseSchema
SchemaFor200ResponseBodyApplicationOctetStream = schemas.BinarySchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: BulkSendGetCsvTemplate200Response


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: BulkSendGetCsvTemplate200Response


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'application/octet-stream': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationOctetStream),
    },
)
SchemaFor401ResponseBodyApplicationJson = BulkSendGetCsvTemplate401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: BulkSendGetCsvTemplate401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: BulkSendGetCsvTemplate401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = BulkSendGetCsvTemplate404ResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: BulkSendGetCsvTemplate404Response


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: BulkSendGetCsvTemplate404Response


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '401': _response_for_401,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
    'application/octet-stream',
)


class BaseApi(api_client.Api):

    def _get_csv_template_mapped_args(
        self,
        template_ids_: BulkSendTemplateIdsParamMap,
        base64: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if template_ids_ is not None:
            _query_params["template_ids[]"] = template_ids_
        if base64 is not None:
            _query_params["base64"] = base64
        args.query = _query_params
        return args

    async def _aget_csv_template_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get Bulk Send CSV Template
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_template_ids_,
            request_query_base64,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/bulk_sends/csv_template',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _get_csv_template_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get Bulk Send CSV Template
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_template_ids_,
            request_query_base64,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/bulk_sends/csv_template',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


class GetCsvTemplateRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_csv_template(
        self,
        template_ids_: BulkSendTemplateIdsParamMap,
        base64: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_csv_template_mapped_args(
            template_ids_=template_ids_,
            base64=base64,
        )
        return await self._aget_csv_template_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_csv_template(
        self,
        template_ids_: BulkSendTemplateIdsParamMap,
        base64: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_csv_template_mapped_args(
            template_ids_=template_ids_,
            base64=base64,
        )
        return self._get_csv_template_oapg(
            query_params=args.query,
        )

class GetCsvTemplate(BaseApi):

    async def aget_csv_template(
        self,
        template_ids_: BulkSendTemplateIdsParamMap,
        base64: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> BulkSendGetCsvTemplate200ResponsePydantic:
        raw_response = await self.raw.aget_csv_template(
            template_ids_=template_ids_,
            base64=base64,
            **kwargs,
        )
        if validate:
            return BulkSendGetCsvTemplate200ResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(BulkSendGetCsvTemplate200ResponsePydantic, raw_response.body)
    
    
    def get_csv_template(
        self,
        template_ids_: BulkSendTemplateIdsParamMap,
        base64: typing.Optional[str] = None,
        validate: bool = False,
    ) -> BulkSendGetCsvTemplate200ResponsePydantic:
        raw_response = self.raw.get_csv_template(
            template_ids_=template_ids_,
            base64=base64,
        )
        if validate:
            return BulkSendGetCsvTemplate200ResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(BulkSendGetCsvTemplate200ResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        template_ids_: BulkSendTemplateIdsParamMap,
        base64: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_csv_template_mapped_args(
            template_ids_=template_ids_,
            base64=base64,
        )
        return await self._aget_csv_template_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        template_ids_: BulkSendTemplateIdsParamMap,
        base64: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_csv_template_mapped_args(
            template_ids_=template_ids_,
            base64=base64,
        )
        return self._get_csv_template_oapg(
            query_params=args.query,
        )

