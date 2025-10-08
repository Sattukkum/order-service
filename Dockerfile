FROM python:3.12-slim

RUN pip install uv

WORKDIR /app
COPY . .

RUN uv sync

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "order_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
