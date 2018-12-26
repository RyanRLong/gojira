from jira import JIRA
from datetime import datetime


class JiraUtils:

    def __init__(self, url, username, password, gateway):
        self.jira = JIRA(url, basic_auth=(username, password))
        self.gateway = gateway

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

    def run_command(self, command, args):
        if args is None:
            args = []
        command = self.gateway.getCommand(command)
        print(command.instruction.format(*args))
        result_set = [x for x in (getattr(self.jira, command.type_name)(command.instruction.format(*args)))]

        results = {}
        results['id'] = [x for x in result_set]
        for field in command.fields:
            results[field] = [getattr(x.fields, field) for x in result_set]
            if field in ["updated", "created"]:
                results[field] = [datetime.strptime(x[:19], '%Y-%m-%dT%H:%M:%S') for x in results[field]]
        return results

    def get_detailed_commands_list(self):
        return {
            'Command': [x[0] for x in self.gateway.get_list_of_commands()],
            'Query': [x[1] for x in self.gateway.get_list_of_commands()],
            'Return Fields': [x[2] for x in self.gateway.get_list_of_commands()]
        }

    def get_commands_list(self):
        return [x[0] for x in self.gateway.get_list_of_commands()]

