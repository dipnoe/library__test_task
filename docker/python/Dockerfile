FROM python:3.10


WORKDIR /app

COPY ../../requirements.txt /app/

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

RUN groupadd --gid 5000 nonrootuser \
    && useradd --home-dir /home/nonrootuser --create-home --uid 5000 \
        --gid 5000 --shell /bin/bash --skel /dev/null nonrootuser

USER nonrootuser

CMD ["bash", "-c", "start.sh"]
