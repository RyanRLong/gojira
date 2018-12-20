from jira import JIRA
import csv


class JiraUtils:

    def __init__(self, url, username, password):
        self.jira = JIRA(url, basic_auth=(username, password))

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

    def new_thing(self, command):
        with open('./macros.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                print(getattr(self.jira, row[0])(row[2]).format(row[3]))



