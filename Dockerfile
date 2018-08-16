from python:2.7

ADD . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "tests.py" ]