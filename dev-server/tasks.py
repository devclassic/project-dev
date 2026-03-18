from invoke.tasks import task


@task
def dev(ctx):
    cmd = "uvicorn app:app --host 127.0.0.1 --port 8000 --reload"
    ctx.run(cmd)
