# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import sys
from .._serialize import _SUPPORTED_API_VERSIONS


X_MS_VERSION = _SUPPORTED_API_VERSIONS[-1]

# Socket timeout in seconds
CONNECTION_TIMEOUT = 20
READ_TIMEOUT = 20

# for python 3.5+, there was a change to the definition of the socket timeout (as far as socket.sendall is concerned)
# The socket timeout is now the maximum total duration to send all data.
if sys.version_info >= (3, 5):
    # the timeout to connect is 20 seconds, and the read timeout is 80000 seconds
    # the 80000 seconds was calculated with:
    # 4000MB (max block size)/ 50KB/s (an arbitrarily chosen minimum upload speed)
    READ_TIMEOUT = 80000

DEFAULT_OAUTH_SCOPE = "/.default"
STORAGE_OAUTH_SCOPE = "https://storage.azure.com/.default"

SERVICE_HOST_BASE = 'core.windows.net'
