from retry.api import retry_call

from config import config
from tests.postman import (
    get_notification_by_id_via_api,
    send_notification_via_api,
)
from tests.test_utils import NotificationStatuses, assert_notification_body


def test_provider_sms_delivery_via_api(staging_and_prod_client):
    notification_id = send_notification_via_api(
        staging_and_prod_client,
        config["service"]["templates"]["sms"],
        config["user"]["mobile"],
        "sms",
    )

    notification = retry_call(
        get_notification_by_id_via_api,
        fargs=[
            staging_and_prod_client,
            notification_id,
            NotificationStatuses.DELIVERED,
        ],
        tries=config["provider_retry_times"],
        delay=config["provider_retry_interval"],
    )
    assert_notification_body(notification_id, notification)
