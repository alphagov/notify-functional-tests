from tests.postman import (
    send_notification_via_api,
    get_notification_by_id_via_api
)

from tests.utils import assert_notification_body


def test_send_sms_and_email_via_api(driver, profile, client):
    notification_id = send_notification_via_api(client, profile.email_template_id, profile.email, 'email')
    notification = get_notification_by_id_via_api(client, notification_id, ['delivered'])
    assert_notification_body(notification_id, notification)