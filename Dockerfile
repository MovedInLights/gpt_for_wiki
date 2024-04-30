FROM python:3.10-slim
WORKDIR /app
RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock ./
RUN poetry install
COPY . .
EXPOSE 8000
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
