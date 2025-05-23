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
from google.cloud.advisorynotifications import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.advisorynotifications_v1.services.advisory_notifications_service.async_client import (
    AdvisoryNotificationsServiceAsyncClient,
)
from google.cloud.advisorynotifications_v1.services.advisory_notifications_service.client import (
    AdvisoryNotificationsServiceClient,
)
from google.cloud.advisorynotifications_v1.types.service import (
    Attachment,
    Csv,
    GetNotificationRequest,
    GetSettingsRequest,
    ListNotificationsRequest,
    ListNotificationsResponse,
    LocalizationState,
    Message,
    Notification,
    NotificationSettings,
    NotificationType,
    NotificationView,
    Settings,
    Subject,
    Text,
    UpdateSettingsRequest,
)

__all__ = (
    "AdvisoryNotificationsServiceClient",
    "AdvisoryNotificationsServiceAsyncClient",
    "Attachment",
    "Csv",
    "GetNotificationRequest",
    "GetSettingsRequest",
    "ListNotificationsRequest",
    "ListNotificationsResponse",
    "Message",
    "Notification",
    "NotificationSettings",
    "Settings",
    "Subject",
    "Text",
    "UpdateSettingsRequest",
    "LocalizationState",
    "NotificationType",
    "NotificationView",
)
