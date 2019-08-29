FROM [put here a scone image]

RUN apk add --update --no-cache python3 py3-pip git gcc

RUN git clone https://github.com/hericlesme/cast.sh \
    && git clone https://github.com/hericlesme/sconericles

RUN cd /cast.sh && pip3 install -r requirements.txt
