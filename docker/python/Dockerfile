FROM python:3.10


WORKDIR /app

COPY ../../requirements.txt /app/

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

RUN groupadd --gid 5000 nonroot \
    && useradd --home-dir /home/nonroot --create-home --uid 5000 \
        --gid 5000 --shell /bin/bash --skel /dev/null nonroot

RUN mkdir -p ../../static && \
    chown -R nonroot:nonroot ../../static

USER nonroot

CMD ["bash", "-c", "start.sh"]
