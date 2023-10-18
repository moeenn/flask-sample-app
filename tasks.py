from invoke import task
import os


PI = "python"
PIP = "pip"
APP = "./app"
HOST = "0.0.0.0"
PORT = 3000
ENTRYPOINT = "wsgi:app"
PROD_WORKERS = 4

"""
Project task commands: Tasks can be executed using command `invoke <task-name>`
Example: invoke dev  
"""

@task
def dev(c, docs=False) -> None:
    c.run(f"dotenv flask --app {ENTRYPOINT} run --host={HOST} --port={PORT} --debug")


@task
def prod(c, docs=False) -> None:
    c.run(f"gunicorn {ENTRYPOINT} --workers {PROD_WORKERS} --bind {HOST}:{PORT} --log-level info")


@task
def shell(c, docs=False) -> None:
    c.run(f"dotenv flask --app {ENTRYPOINT} shell")


@task
def dbinit(c, docs=False) -> None:
    c.run(f"dotenv flask --app {ENTRYPOINT} db init")


@task 
def dbmigrate(c, docs=False) -> None:
    print("Generating migrations")
    c.run(f"dotenv flask --app {ENTRYPOINT} db migrate")
    print("\n\nApplying migrations")
    c.run(f"dotenv flask --app {ENTRYPOINT} db upgrade")


@task
def gensecret(c, docs=False) -> None:
    c.run(f"{PI} {APP}/scripts/generate_secret.py")


@task
def test(c, docs=False) -> None:
    c.run(f"dotenv {PI} -m unittest {APP}/**/test_*.py")


@task
def fmt(c, docs=False) -> None:
    c.run(f"black {APP}")


@task
def lint(c, docs=False) -> None:
    c.run(f"{PI} -m ruff check {APP}")


@task 
def clean(c, docs=False) -> None:
    # recursively remove __pycache__ directories from project
    print("Removing cache files...")
    c.run("find . -type d -name  '__pycache__' -exec rm -r {} +")
    c.run("rm -r .*_cache >& /dev/null")
    c.run("rm -r *.egg-info >& /dev/null")

    build_dir = os.path.join(os.getcwd(), "build")
    if os.path.exists(build_dir):
        c.run(f"rm -r {build_dir}")

