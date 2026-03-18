from invoke.tasks import task


@task
def dev(ctx):
    cmd = "uvicorn app:app --host 127.0.0.1 --port 8000 --reload"
    ctx.run(cmd)


@task
def build(ctx):
    cmd = "pyinstaller"
    cmd += " --clean"
    cmd += " --onefile"
    cmd += " main.py"
    ctx.run(cmd)
