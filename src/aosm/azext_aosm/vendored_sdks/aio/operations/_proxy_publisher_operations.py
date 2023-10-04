# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._proxy_publisher_operations import build_get_request, build_list_by_location_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ProxyPublisherOperations:
    """ProxyPublisherOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~Microsoft.HybridNetwork.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list_by_location(
        self,
        publisher_scope_name: str,
        publisher_location_name: str,
        **kwargs: Any
    ) -> AsyncIterable["_models.ProxyPublisherOverviewListResult"]:
        """Lists all the available network function definition and network service design publishers.

        :param publisher_scope_name: The name of the publisher scope.
        :type publisher_scope_name: str
        :param publisher_location_name: The name of the publisher location.
        :type publisher_location_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ProxyPublisherOverviewListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~Microsoft.HybridNetwork.models.ProxyPublisherOverviewListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2023-04-01-preview")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ProxyPublisherOverviewListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_location_request(
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    publisher_scope_name=publisher_scope_name,
                    publisher_location_name=publisher_location_name,
                    template_url=self.list_by_location.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_by_location_request(
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    publisher_scope_name=publisher_scope_name,
                    publisher_location_name=publisher_location_name,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ProxyPublisherOverviewListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_location.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.HybridNetwork/proxyPublishers"}  # type: ignore

    @distributed_trace_async
    async def get(
        self,
        publisher_scope_name: str,
        publisher_location_name: str,
        proxy_publisher_name: str,
        **kwargs: Any
    ) -> "_models.ProxyPublisherOverview":
        """Get a publisher overview information.

        :param publisher_scope_name: The name of the publisher scope.
        :type publisher_scope_name: str
        :param publisher_location_name: The name of the publisher location.
        :type publisher_location_name: str
        :param proxy_publisher_name: The name of the proxy publisher.
        :type proxy_publisher_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProxyPublisherOverview, or the result of cls(response)
        :rtype: ~Microsoft.HybridNetwork.models.ProxyPublisherOverview
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ProxyPublisherOverview"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2023-04-01-preview")  # type: str

        
        request = build_get_request(
            proxy_publisher_name=proxy_publisher_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            publisher_scope_name=publisher_scope_name,
            publisher_location_name=publisher_location_name,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ProxyPublisherOverview', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.HybridNetwork/proxyPublishers/{proxyPublisherName}"}  # type: ignore
