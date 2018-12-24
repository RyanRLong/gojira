from jira import JIRA


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
        command = self.gateway.getCommand(command)
        result_set = [x for x in (getattr(self.jira, command.type_name)(command.instruction.format(*args)))]

        results = {}
        for field in command.fields:
            results['id'] = [x for x in result_set]
            results[field] = [getattr(x.fields, field) for x in result_set]

        return results

    def get_commands_list(self):
        return {
            'Command': [x[0] for x in self.gateway.get_list_of_commands()],
            'Query': [x[1] for x in self.gateway.get_list_of_commands()],
            'Return Fields': [x[2] for x in self.gateway.get_list_of_commands()]
        }
