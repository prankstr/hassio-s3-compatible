"""Constants for the S3 compatible integration."""

from collections.abc import Callable
from typing import Final

from homeassistant.util.hass_dict import HassKey

DOMAIN: Final = "s3_compatible"

CONF_ACCESS_KEY_ID = "access_key_id"
CONF_SECRET_ACCESS_KEY = "secret_access_key"
CONF_ENDPOINT_URL = "endpoint_url"
CONF_BUCKET = "bucket"

DEFAULT_ENDPOINT_URL = f""

DATA_BACKUP_AGENT_LISTENERS: HassKey[list[Callable[[], None]]] = HassKey(
    f"{DOMAIN}.backup_agent_listeners"
)

DESCRIPTION_BOTO3_DOCS_URL = "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html"
