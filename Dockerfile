FROM python:3.10
ENV PYTHONUNBUFFERED 1

RUN mkdir /project
WORKDIR /project
RUN mkdir /project/pipelines
RUN mkdir /project/example_pipeline
COPY /pipelines /project/pipelines
COPY /example_pipeline /project/example_pipeline
COPY pyproject.toml /project
COPY setup.py /project
COPY execute.sh /project
COPY poetry.lock /project
COPY README.md /project

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
ENTRYPOINT ["bash", "/project/execute.sh"]