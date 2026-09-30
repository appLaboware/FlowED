FROM docker:27-cli

ARG PORTER_VERSION=v1.6.1
ARG DOCKER_MIXIN_VERSION=v1.0.6
ARG DOCKER_COMPOSE_MIXIN_VERSION=v1.0.6
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
    && porter mixin install docker --version "${DOCKER_MIXIN_VERSION}" \
    && porter mixin install docker-compose --version "${DOCKER_COMPOSE_MIXIN_VERSION}"

COPY config.yaml /root/.porter/config.yaml

WORKDIR /workspace/IDEOS

CMD ["bash"]
