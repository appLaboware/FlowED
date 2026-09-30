FROM docker:27-cli

ARG PORTER_VERSION=v1.6.1
ARG TARGETARCH

RUN apk add --no-cache \
    bash \
    ca-certificates \
    curl \
    git \
    jq

ENV PORTER_HOME=/root/.porter
ENV PATH="/root/.porter:${PATH}"

RUN test -n "${TARGETARCH}" \
    && curl -fsSL "https://github.com/getporter/porter/releases/download/${PORTER_VERSION}/porter-linux-${TARGETARCH}" -o /usr/local/bin/porter \
    && chmod +x /usr/local/bin/porter \
    && porter version \
    && porter mixin install docker \
    && porter mixin install docker-compose \
    && porter plugins install mongodb

COPY config.yaml /root/.porter/config.yaml

WORKDIR /workspace/IDEOS

CMD ["bash"]
