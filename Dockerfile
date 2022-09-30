FROM python:3.10

WORKDIR /usr/src/app
COPY *.py *.txt ./

RUN echo "python -B split.py    -or-    python -B merge.py"

CMD ["sh"]
