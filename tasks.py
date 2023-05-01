from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/main.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest ./src", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest ./src", pty=True)

@task
def report(ctx):
    ctx.run("coverage report -m", pty=True)

@task
def html(ctx):
    ctx.run("coverage html", pty=True)

@task
def clean(ctx):
    ctx.run("autopep8 --in-place --recursive src/*.py", pty=True)