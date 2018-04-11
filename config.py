import os


class Config(object):
    ENVIRONMENT = os.environ['ENVIRONMENT']
    NOTIFY_ADMIN_URL = os.environ.get(os.environ.get('ENVIRONMENT') + '_NOTIFY_ADMIN_URL')
    NOTIFY_API_URL = os.environ.get(os.environ.get('ENVIRONMENT') + '_NOTIFY_API_URL')
    TEST_NUMBER = os.environ.get(os.environ.get('ENVIRONMENT') + '_TEST_NUMBER')
    FUNCTIONAL_TEST_NAME = os.environ.get('ENVIRONMENT') + '_Functional Test_'
    FUNCTIONAL_TEST_EMAIL = os.environ.get(os.environ.get('ENVIRONMENT') + '_FUNCTIONAL_TEST_EMAIL')
    FUNCTIONAL_TEST_PASSWORD = os.environ.get(os.environ.get('ENVIRONMENT') + '_FUNCTIONAL_TEST_PASSWORD')
    NOTIFICATION_RETRY_TIMES = 15
    NOTIFICATION_RETRY_INTERVAL = 5
    PROVIDER_RETRY_TIMES = 12
    PROVIDER_RETRY_INTERVAL = 22
    VERIFY_CODE_RETRY_TIMES = 8
    VERIFY_CODE_RETRY_INTERVAL = 9
    FUNCTIONAL_TEST_SERVICE_NAME = os.environ.get('ENVIRONMENT') + '_Functional Test Service_'
    JENKINS_BUILD_SMS_TEMPLATE_ID = os.environ.get(os.environ.get('ENVIRONMENT') + '_JENKINS_BUILD_SMS_TEMPLATE_ID')
    JENKINS_BUILD_EMAIL_TEMPLATE_ID = os.environ.get(os.environ.get('ENVIRONMENT') + '_JENKINS_BUILD_EMAIL_TEMPLATE_ID')
    JENKINS_BUILD_LETTER_TEMPLATE_ID = os.environ.get(
        os.environ.get('ENVIRONMENT') + '_JENKINS_BUILD_LETTER_TEMPLATE_ID')
    NOTIFY_SERVICE_API_KEY = os.environ.get(os.environ.get('ENVIRONMENT') + '_NOTIFY_SERVICE_API_KEY')
    NOTIFY_RESEARCH_MODE_EMAIL = os.environ.get(os.environ.get('ENVIRONMENT') + '_NOTIFY_RESEARCH_MODE_EMAIL')
    NOTIFY_RESEARCH_MODE_EMAIL_PASSWORD = os.environ.get(
        os.environ.get('ENVIRONMENT') + '_NOTIFY_RESEARCH_MODE_EMAIL_PASSWORD')
    NOTIFY_RESEARCH_SERVICE_EMAIL_AUTH_ACCOUNT = os.environ.get(
        os.environ.get('ENVIRONMENT') + '_NOTIFY_RESEARCH_SERVICE_EMAIL_AUTH_ACCOUNT')
    NOTIFY_RESEARCH_SERVICE_ID = os.environ.get(os.environ.get('ENVIRONMENT') + '_NOTIFY_RESEARCH_SERVICE_ID')
    NOTIFY_RESEARCH_SERVICE_API_TEST_KEY = os.environ.get(
        os.environ.get('ENVIRONMENT') + '_NOTIFY_RESEARCH_SERVICE_API_TEST_KEY')
    NOTIFY_RESEARCH_SERVICE_API_KEY = os.environ.get(os.environ.get('ENVIRONMENT') + '_NOTIFY_RESEARCH_SERVICE_API_KEY')
    NOTIFY_RESEARCH_SERVICE_NAME = os.environ.get(os.environ.get('ENVIRONMENT') + '_NOTIFY_RESEARCH_SERVICE_NAME')
    NOTIFY_RESEARCH_EMAIL_REPLY_TO = os.environ.get(os.environ.get('ENVIRONMENT') + '_NOTIFY_RESEARCH_EMAIL_REPLY_TO')
    NOTIFY_RESEARCH_ORGANISATION_ID = os.environ.get(os.environ.get('ENVIRONMENT') + '_NOTIFY_RESEARCH_ORGANISATION_ID')
    NOTIFY_RESEARCH_SMS_SENDER = 'func tests'
    NOTIFY_RESEARCH_LETTER_CONTACT = {"address_line_1": "test", "address_line_2": "London", "postcode": "N1"}
    REGISTRATION_TEMPLATE_ID = 'ece42649-22a8-4d06-b87f-d52d5d3f0a27'
    INVITATION_TEMPLATE_ID = '4f46df42-f795-4cc4-83bb-65ca312f49cc'
    VERIFY_CODE_TEMPLATE_ID = '36fb0730-6259-4da1-8a80-c8de22ad4246'
    EMAIL_AUTH_TEMPLATE_ID = '299726d2-dba6-42b8-8209-30e1d66ea164'
    ORG_INVITATION_TEMPLATE_ID = '203566f0-d835-47c5-aa06-932439c86573'

    DOCUMENT_DOWNLOAD_API_HOST = os.environ.get(os.environ.get('ENVIRONMENT') + '_DOCUMENT_DOWNLOAD_API_HOST')
    DOCUMENT_DOWNLOAD_API_KEY = os.environ.get(os.environ.get('ENVIRONMENT') + '_DOCUMENT_DOWNLOAD_API_KEY')


class PreviewConfig(Config):
    SMS_TEMPLATE_ID = os.environ.get('preview_SMS_TEMPLATE_ID')
    EMAIL_TEMPLATE_ID = os.environ.get('preview_EMAIL_TEMPLATE_ID')
    JENKINS_BUILD_SMS_TEMPLATE_ID = os.environ.get('preview_JENKINS_BUILD_SMS_TEMPLATE_ID')
    JENKINS_BUILD_EMAIL_TEMPLATE_ID = os.environ.get('preview_JENKINS_BUILD_EMAIL_TEMPLATE_ID')
    NOTIFY_RESEARCH_MODE_EMAIL = os.environ.get('preview_NOTIFY_RESEARCH_MODE_EMAIL')
    NOTIFY_RESEARCH_MODE_EMAIL_PASSWORD = os.environ.get('preview_NOTIFY_RESEARCH_MODE_EMAIL_PASSWORD')
    NOTIFY_RESEARCH_SERVICE_ID = os.environ.get('preview_NOTIFY_RESEARCH_SERVICE_ID')
    NOTIFY_RESEARCH_SERVICE_API_KEY = os.environ.get('preview_NOTIFY_RESEARCH_SERVICE_API_KEY')
    NOTIFY_RESEARCH_SERVICE_NAME = os.environ.get('preview_NOTIFY_RESEARCH_SERVICE_NAME')
    NOTIFY_RESEARCH_EMAIL_REPLY_TO = os.environ.get('preview_NOTIFY_RESEARCH_EMAIL_REPLY_TO')
    # seeded organisation
    NOTIFY_RESEARCH_ORGANISATION_ID = '63b9557c-22ea-42ac-bcba-edaa50e3ae51'


class StagingConfig(Config):
    FUNCTIONAL_TEST_SERVICE_NAME = 'Staging FunctionalTest'
    SMS_TEMPLATE_ID = os.environ.get('staging_SMS_TEMPLATE_ID')
    EMAIL_TEMPLATE_ID = os.environ.get('staging_EMAIL_TEMPLATE_ID')
    JENKINS_BUILD_SMS_TEMPLATE_ID = os.environ.get('staging_JENKINS_BUILD_SMS_TEMPLATE_ID')
    JENKINS_BUILD_EMAIL_TEMPLATE_ID = os.environ.get('staging_JENKINS_BUILD_EMAIL_TEMPLATE_ID')
    SERVICE_ID = os.environ.get('staging_SERVICE_ID')
    SERVICE_API_KEY = os.environ.get('staging_API_KEY')


class LiveConfig(Config):
    FUNCTIONAL_TEST_SERVICE_NAME = 'Live FunctionalTest'
    SMS_TEMPLATE_ID = os.environ.get('live_SMS_TEMPLATE_ID')
    EMAIL_TEMPLATE_ID = os.environ.get('live_EMAIL_TEMPLATE_ID')
    JENKINS_BUILD_SMS_TEMPLATE_ID = os.environ.get('live_JENKINS_BUILD_SMS_TEMPLATE_ID')
    JENKINS_BUILD_EMAIL_TEMPLATE_ID = os.environ.get('live_JENKINS_BUILD_EMAIL_TEMPLATE_ID')
    SERVICE_ID = os.environ.get('live_SERVICE_ID')
    SERVICE_API_KEY = os.environ.get('live_API_KEY')
