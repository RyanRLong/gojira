import configparser

import click
from prompt_toolkit import prompt
from tabulate import tabulate
from prompt_toolkit.completion import Completer, Completion

from gojira.lib.gateway import Gateway
from gojira.lib.jirautils import JiraUtils

config = configparser.ConfigParser()
config.read('./config.ini')
jira_username = config['jira']['username']
jira_password = config['jira']['password']
jira_url = config['jira']['url']
gj = JiraUtils(jira_url, jira_username, jira_password, Gateway())


class CommandCompleter(Completer):
    def get_completions(self, document, complete_event):
        command_list = gj.get_commands_list()
        for command in command_list:
            yield Completion(command, start_position=0)


@click.group()
def cli():
    pass


@cli.command()
def list_commands():
    click.echo(tabulate(gj.get_commands_list(), headers="keys"))


@cli.command()
@click.option('-c','--command_name')
@click.option('-q', '--query_params')
def run(command_name, query_params):
    if command_name is None:
        command_name = prompt("Which command?> ", completer=CommandCompleter())
    query_params = query_params.replace(" ", "").split(",") if query_params is not None else []
    results = gj.run_command(command_name, query_params)
    click.echo(tabulate(results, headers="keys", tablefmt="fancy_grid", showindex="always"))

