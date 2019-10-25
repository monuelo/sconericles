ARG SCONE_IMAGE

FROM ${SCONE_IMAGE}

RUN apk add --update --no-cache python3 py3-pip git gcc

RUN git clone https://github.com/hericlesme/sconericles --recursive

RUN cd /sconericles/cast-sh && pip3 install -r requirements.txt
