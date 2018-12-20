from jira import JIRA
from src.lib.gateway import Command, Gateway
import csv


class JiraUtils:

    def __init__(self, url, username, password):
        self.jira = JIRA(url, basic_auth=(username, password))
        self.gateway = Gateway()

    def get_available_statuses(self):
        issues = self.jira.search_issues('assignee="Ryan Long"')
        return list(set([(issue.fields.status.id, issue.fields.status.name) for issue in issues]))

    def get_issues_with_status(self, status):
        issues = self.jira.search_issues('project= "Affiliate Network" AND status={}'.format(status))
        return issues

    def get_projects_assigned_to(self, assignee):
        issues = self.jira.search_issues('project= "Affiliate Network" and assignee="{}"'.format(assignee))
        return issues

    def boards(self):
        return self.jira.boards()

    def run_command(self, command):
        command = self.gateway.getCommand(command)
        return getattr(self.jira, command.type_name)(command.instruction)



