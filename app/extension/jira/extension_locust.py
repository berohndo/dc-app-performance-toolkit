import re
from locustio.common_utils import init_logger, jira_measure, run_as_specific_user  # noqa F401

logger = init_logger(app_type='jira')


@jira_measure("locust_app_specific_action")
@run_as_specific_user(username='admin', password='admin')  # run as specific user
def app_specific_action(locust):
    r = locust.get('/rest/viableissues/latest/checkFields?projectId=10396&issueType=10334&fields=priority', catch_response=True)  # call app-specific GET endpoint
    content = r.content.decode('utf-8')   # decode response content

    if 'screenFields' not in content:
        logger.error(f"'assertion string' was not found in {content}")
    assert 'screenFields' in content  # assert specific string in response content
