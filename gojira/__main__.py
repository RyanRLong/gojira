from tabulate import tabulate
from src.lib.gateway import Gateway

if __name__ == "__main__":
    from src.lib.jirautils import JiraUtils
    import configparser

    config = configparser.ConfigParser()
    config.read('./config.ini')
    jira_username = config['jira']['username']
    jira_password = config['jira']['password']
    jira_url = config['jira']['url']

    # print(JiraUtils(jira_url, jira_username, jira_password).get_issues_with_status('review'))
    # print(JiraUtils(jira_url, jira_username, jira_password).get_projects_assigned_to('Ryan Long'))
    gj = JiraUtils(jira_url, jira_username, jira_password, Gateway())
    results = gj.run_command('Review', ('Review',))
    print(tabulate(results, headers="keys", tablefmt="grid"))
    print(tabulate(gj.get_commands_list(), headers="keys"))

