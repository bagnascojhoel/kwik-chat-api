FROM docker.io/python:3.10-slim-buster AS builder

RUN pip install pipenv

# Tell pipenv to create venv in the current directory
ENV PIPENV_VENV_IN_PROJECT=1

ADD Pipfile.lock Pipfile /usr/src/

WORKDIR /usr/src

RUN pipenv sync

#################################################

FROM docker.io/python:3.10-slim-buster AS runtime

RUN mkdir -v /usr/src/.venv

COPY --from=builder /usr/src/.venv/ /usr/src/.venv/

ADD ./app /usr/src/app

WORKDIR /usr/src/

RUN /usr/src/.venv/bin/pip3 install gunicorn

EXPOSE 5000

CMD ["/usr/src/.venv/bin/python", "-m", "gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:create_app()" ]
