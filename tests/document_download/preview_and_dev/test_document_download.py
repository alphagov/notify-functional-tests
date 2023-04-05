import os
import re
from io import BytesIO
from urllib.parse import urlparse

import pytest
import requests
from notifications_python_client import prepare_upload
from retry import retry
from selenium.webdriver.common.by import By

from config import config
from tests.pages import (
    DocumentDownloadConfirmEmailPage,
    DocumentDownloadLandingPage,
    DocumentDownloadPage,
)
from tests.test_utils import RetryException


def _get_test_doc_dl_url(client_live_key, prepare_upload_kwargs):
    file = prepare_upload(
        BytesIO("foo-bar-baz".encode("utf-8")), **prepare_upload_kwargs
    )
    personalisation = {"build_id": file}
    email_address = config["service"]["seeded_user"]["email"]
    template_id = config["service"]["templates"]["email"]

    resp_json = client_live_key.send_email_notification(
        email_address, template_id, personalisation
    )

    download_link = re.search(r"(https?://\S+)", resp_json["content"]["body"])

    assert download_link

    return download_link.group(0)


@retry(
    RetryException,
    tries=10,
    delay=1,
)
def get_downloaded_document(download_directory, filename):
    """
    Wait up to ten seconds for the file to be downloaded, checking every second
    """
    for file in download_directory.iterdir():
        if file.is_file() and file.name == filename:
            return file
    raise RetryException(f"{filename} not found in downloads folder")


@pytest.mark.antivirus
def test_document_upload_and_download(driver, client_live_key):
    download_link = _get_test_doc_dl_url(
        client_live_key,
        {"confirm_email_before_download": False},
    )

    driver.get(download_link)

    landing_page = DocumentDownloadLandingPage(driver)
    assert "Functional Tests" in landing_page.get_service_name()

    landing_page.go_to_download_page()

    download_page = DocumentDownloadPage(driver)
    document_url = download_page.get_download_link()

    headers = {}
    if os.getenv("NOTIFY_ECS_ORIGIN"):
        headers = {"x-notify-ecs-origin": "true"}

    downloaded_document = requests.get(document_url, headers=headers)

    assert downloaded_document.text == "foo-bar-baz"


@pytest.mark.antivirus
def test_document_download_with_email_confirmation(
    driver, client_live_key, download_directory
):
    download_link = _get_test_doc_dl_url(
        client_live_key,
        {"confirm_email_before_download": True},
    )

    driver.get(download_link)
    landing_page = DocumentDownloadLandingPage(driver)
    assert "Functional Tests" in landing_page.get_service_name()

    landing_page.go_to_download_page()

    email_confirm_page = DocumentDownloadConfirmEmailPage(driver)
    email_confirm_page.input_email_address(config["service"]["seeded_user"]["email"])
    email_confirm_page.click_continue()

    download_page = DocumentDownloadPage(driver)

    file_url = download_page.get_download_link()
    download_page.click_download_link()

    # the file _might_ have downloaded, or alternatively it might have rendered in browser.
    # Lets check either way.
    if file_url == driver.current_url:
        # chrome has rendered the file in browser
        body = driver.find_element(By.TAG_NAME, "body")
        assert body.text == "foo-bar-baz"
    else:
        # chrome has downloaded the file

        # get the filename out of the download URL
        filename = urlparse(file_url).path.split("/")[-1]

        document_path = get_downloaded_document(download_directory, filename)

        with open(document_path) as f:
            assert f.read() == "foo-bar-baz"


def test_document_download_with_email_confirmation_rejects_bad_email(
    driver, client_live_key
):
    download_link = _get_test_doc_dl_url(
        client_live_key,
        {"confirm_email_before_download": True},
    )

    driver.get(download_link)
    landing_page = DocumentDownloadLandingPage(driver)
    assert "Functional Tests" in landing_page.get_service_name()

    landing_page.go_to_download_page()

    email_confirm_page = DocumentDownloadConfirmEmailPage(driver)
    email_confirm_page.input_email_address("foo@bar.com")
    email_confirm_page.click_continue()

    assert (
        "This is not the email address the file was sent to"
        in email_confirm_page.get_errors()
    )
