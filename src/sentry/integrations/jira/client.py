from __future__ import absolute_import

from six.moves.urllib.parse import urlparse

from sentry.integrations.atlassian_connect import integration_request
from sentry.utils.http import absolute_uri

JIRA_KEY = '%s.jira' % (urlparse(absolute_uri()).hostname, )


class JiraApiClient(object):
    COMMENT_URL = '/rest/api/2/issue/%s/comment'
    ISSUE_URL = '/rest/api/2/issue/%s'

    def __init__(self, base_url, shared_secret):
        self.base_url = base_url
        self.shared_secret = shared_secret

    def get_issue(self, issue_id):
        return integration_request('GET', self.ISSUE_URL % (issue_id,))

    def create_comment(self, issue_key, comment):
        return integration_request('POST', self.COMMENT_URL % issue_key, data={'body': comment})
