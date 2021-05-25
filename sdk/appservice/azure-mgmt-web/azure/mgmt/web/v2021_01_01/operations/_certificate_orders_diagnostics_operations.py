# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class CertificateOrdersDiagnosticsOperations(object):
    """CertificateOrdersDiagnosticsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: API Version. Constant value: "2021-01-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2021-01-01"

        self.config = config

    def list_app_service_certificate_order_detector_response(
            self, resource_group_name, certificate_order_name, custom_headers=None, raw=False, **operation_config):
        """Microsoft.CertificateRegistration to get the list of detectors for this
        RP.

        Description for Microsoft.CertificateRegistration to get the list of
        detectors for this RP.

        :param resource_group_name: Name of the resource group to which the
         resource belongs.
        :type resource_group_name: str
        :param certificate_order_name: The certificate order name for which
         the response is needed.
        :type certificate_order_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of DetectorResponse
        :rtype:
         ~azure.mgmt.web.v2021_01_01.models.DetectorResponsePaged[~azure.mgmt.web.v2021_01_01.models.DetectorResponse]
        :raises:
         :class:`DefaultErrorResponseException<azure.mgmt.web.v2021_01_01.models.DefaultErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_app_service_certificate_order_detector_response.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+[^\.]$'),
                    'certificateOrderName': self._serialize.url("certificate_order_name", certificate_order_name, 'str'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.DefaultErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.DetectorResponsePaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list_app_service_certificate_order_detector_response.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/detectors'}

    def get_app_service_certificate_order_detector_response(
            self, resource_group_name, certificate_order_name, detector_name, start_time=None, end_time=None, time_grain=None, custom_headers=None, raw=False, **operation_config):
        """Microsoft.CertificateRegistration call to get a detector response from
        App Lens.

        Description for Microsoft.CertificateRegistration call to get a
        detector response from App Lens.

        :param resource_group_name: Name of the resource group to which the
         resource belongs.
        :type resource_group_name: str
        :param certificate_order_name: The certificate order name for which
         the response is needed.
        :type certificate_order_name: str
        :param detector_name: The detector name which needs to be run.
        :type detector_name: str
        :param start_time: The start time for detector response.
        :type start_time: datetime
        :param end_time: The end time for the detector response.
        :type end_time: datetime
        :param time_grain: The time grain for the detector response.
        :type time_grain: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DetectorResponse or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.web.v2021_01_01.models.DetectorResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`DefaultErrorResponseException<azure.mgmt.web.v2021_01_01.models.DefaultErrorResponseException>`
        """
        # Construct URL
        url = self.get_app_service_certificate_order_detector_response.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+[^\.]$'),
            'certificateOrderName': self._serialize.url("certificate_order_name", certificate_order_name, 'str'),
            'detectorName': self._serialize.url("detector_name", detector_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if start_time is not None:
            query_parameters['startTime'] = self._serialize.query("start_time", start_time, 'iso-8601')
        if end_time is not None:
            query_parameters['endTime'] = self._serialize.query("end_time", end_time, 'iso-8601')
        if time_grain is not None:
            query_parameters['timeGrain'] = self._serialize.query("time_grain", time_grain, 'str', pattern=r'PT[1-9][0-9]+[SMH]')
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.DefaultErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('DetectorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_app_service_certificate_order_detector_response.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/detectors/{detectorName}'}
