# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.core import PipelineClient

from . import models
from ._configuration import AzureFileStorageConfiguration
from .operations import DirectoryOperations, FileOperations, ServiceOperations, ShareOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

    from azure.core.rest import HttpRequest, HttpResponse

class AzureFileStorage(object):
    """AzureFileStorage.

    :ivar service: ServiceOperations operations
    :vartype service: azure.storage.fileshare.operations.ServiceOperations
    :ivar share: ShareOperations operations
    :vartype share: azure.storage.fileshare.operations.ShareOperations
    :ivar directory: DirectoryOperations operations
    :vartype directory: azure.storage.fileshare.operations.DirectoryOperations
    :ivar file: FileOperations operations
    :vartype file: azure.storage.fileshare.operations.FileOperations
    :param url: The URL of the service account, share, directory or file that is the target of the
     desired operation.
    :type url: str
    :param base_url: Service URL. Default value is ''.
    :type base_url: str
    :keyword version: Specifies the version of the operation to use for this request. The default
     value is "2021-06-08". Note that overriding this default value may result in unsupported
     behavior.
    :paramtype version: str
    :keyword file_range_write_from_url: Only update is supported: - Update: Writes the bytes
     downloaded from the source url into the specified range. The default value is "update". Note
     that overriding this default value may result in unsupported behavior.
    :paramtype file_range_write_from_url: str
    """

    def __init__(
        self,
        url,  # type: str
        base_url="",  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        self._config = AzureFileStorageConfiguration(url=url, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.service = ServiceOperations(self._client, self._config, self._serialize, self._deserialize)
        self.share = ShareOperations(self._client, self._config, self._serialize, self._deserialize)
        self.directory = DirectoryOperations(self._client, self._config, self._serialize, self._deserialize)
        self.file = FileOperations(self._client, self._config, self._serialize, self._deserialize)


    def _send_request(
        self,
        request,  # type: HttpRequest
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpResponse
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AzureFileStorage
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
