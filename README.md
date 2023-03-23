# Pipelines — ETL Framework

## Launch with Docker

```shell
> docker build -t pipelines .
> docker run pipelines
```

## Launch with Poetry

```shell
> poetry install
> cd example_pipeline 
> poetry run pipelines run
> poetry run pipelines show
```

## Pytest

```shell
> poetry run pytest tests
```