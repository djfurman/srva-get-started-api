FROM lambci/lambda:build-python3.6
LABEL maintianer="djfurman@gmail.com"

COPY . /var/task
WORKDIR /var/task

ENV SHELL=/bin/bash
ENV PACKAGE_NAME="serverless-rva-api"

RUN pipenv install && \
    zip ${PACKAGE_NAME}.zip *.py && \
    rm -rf `pipenv --venv`/lib/python3.6/site-packages/boto* && \
    rm -rf `pipenv --venv`/lib/python3.6/site-packages/pip* && \
    rm -rf `pipenv --venv`/lib/python3.6/site-packages/setuptools* && \
    rm -rf `pipenv --venv`/lib/python3.6/site-packages/wheel* && \
    rm -rf `pipenv --venv`/lib/python3.6/site-packages/six* && \
    zip -r /var/task/${PACKAGE_NAME}.zip `pipenv --venv`/lib/python3.6/site-packages/

CMD ["echo", "Complete"]
