FROM python:3.9-slim AS builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    texlive-latex-base \
    texlive-fonts-recommended \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-xetex \
    ghostscript \
    dvipng \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN python -m venv .venv
COPY requirements.txt ./
RUN .venv/bin/pip install -r requirements.txt

COPY . .

FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    texlive-latex-base \
    texlive-fonts-recommended \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-xetex \
    ghostscript \
    dvipng \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/.venv .venv/
COPY . .

CMD ["/app/.venv/bin/flask", "run", "--host=0.0.0.0", "--port=8080"]

