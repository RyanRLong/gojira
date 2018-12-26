from prompt_toolkit import PromptSession

session = PromptSession()
while True:
        try:
            text = session.prompt('gojira> ')
        except KeyboardInterrupt:
            break  # Control-C pressed.
        except EOFError:
            break  # Control-D pressed.