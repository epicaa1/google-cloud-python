# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
from typing import Dict, Type

from .base import MessagesV1Beta3Transport
from .grpc import MessagesV1Beta3GrpcTransport
from .grpc_asyncio import MessagesV1Beta3GrpcAsyncIOTransport
from .rest import MessagesV1Beta3RestInterceptor, MessagesV1Beta3RestTransport

# Compile a registry of transports.
_transport_registry = OrderedDict()  # type: Dict[str, Type[MessagesV1Beta3Transport]]
_transport_registry["grpc"] = MessagesV1Beta3GrpcTransport
_transport_registry["grpc_asyncio"] = MessagesV1Beta3GrpcAsyncIOTransport
_transport_registry["rest"] = MessagesV1Beta3RestTransport

__all__ = (
    "MessagesV1Beta3Transport",
    "MessagesV1Beta3GrpcTransport",
    "MessagesV1Beta3GrpcAsyncIOTransport",
    "MessagesV1Beta3RestTransport",
    "MessagesV1Beta3RestInterceptor",
)
