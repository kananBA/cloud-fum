FROM python:3.10.5-alpine3.16

ADD ./requirements.txt /app/requirements.txt

# libffi-dev for cryptography
# libxml2-dev & libxslt-dev for lxml
# jpeg-dev zlib-dev for Pillow
# gettext django internationalization

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN set -ex \
    && apk add --no-cache --virtual .build-deps postgresql-dev build-base \
    && apk add python3-dev musl-dev libffi-dev libxml2-dev libxslt-dev jpeg-dev zlib-dev gettext \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /app/requirements.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
    | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
    | sort -u \
    | xargs -r apk info --installed \
    | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps

COPY . /app
WORKDIR /app

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
