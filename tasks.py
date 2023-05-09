from invoke import task

@task
def start(ctx):
    ctx.run("python3 pathfinding/src/main.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest ./pathfinding//src", pty=True)

@task
def lint(ctx):
    ctx.run("pylint ./pathfinding/src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest ./pathfinding//src", pty=True)
    ctx.run("coverage report -m", pty=True)
    ctx.run("coverage html", pty=True)

@task
def clean(ctx):
    ctx.run("autopep8 --in-place --aggressive ./pathfinding/src/*.py", pty=True)
    ctx.run("autopep8 --in-place --aggressive ./pathfinding/src/**/*.py", pty=True)
