from jira import JIRA


class JiraUtils:

    def __init__(self, url, username, password):
        self.jira = JIRA(url, basic_auth=(username, password))

    def get_available_statuses(self):
        issues = self.jira.search_issues('assignee="Ryan Long"')
        return list(set([(issue.fields.status.id, issue.fields.status.name) for issue in issues]))