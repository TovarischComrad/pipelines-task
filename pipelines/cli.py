import click

from . import tasks
from .core import Pipeline
from .load import load_pipeline
import pandas as pd


# TASKS = [
#     tasks.CopyToFile(table='data', output_file='data.csv'),
#     tasks.RunSQL(sql_query='select 1;', title="Useless SQL query"),
# ]
#
# pipeline = Pipeline(tasks=TASKS)


@click.group()
def cli():
    pass


@cli.command()
def explore():
    click.echo(f"Explore")


@cli.command()
def list():
    pipeline = load_pipeline()
    pipeline.list()


@cli.command()
def run():
    pipeline = load_pipeline()
    pipeline.run()


@cli.command()
def show():
    file = 'norm.csv'
    data = pd.read_csv(file)
    print(data)


def main():
    cli()
