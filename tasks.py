from invoke import task


@task
def clean(c, docs=False, bytecode=False, extra=''):
    patterns = ['build']
    if docs:
        patterns.append('docs/_build')
    if bytecode:
        patterns.append('**/*.pyc')
    if extra:
        patterns.append(extra)
    for pattern in patterns:
        c.run("rm -rf {}".format(pattern))


@task
def build(c, docs=False):
    c.run("python setup.py build")
    if docs:
        c.run("sphinx-build docs docs/_build")


@task
def update(c):
    print("Updating requirements file")
    c.run("pip list >> requirements.txt")


@task
def lint(c):
    print("Creating lint report")
    c.run("pylint src > lint_results.txt")
