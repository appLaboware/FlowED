FROM docker:27-cli

ARG PORTER_VERSION=v1.6.1
ARG DOCKER_MIXIN_VERSION=v1.0.6
ARG DOCKER_COMPOSE_MIXIN_VERSION=v1.0.6

RUN apk add --no-cache \
    bash \
    ca-certificates \
    curl \
    git \
    jq \
    tar \
    gzip

ENV PORTER_HOME=/root/.porter
ENV PATH="/root/.porter:${PATH}"

RUN curl -fsSL "https://cdn.porter.sh/${PORTER_VERSION}/install-linux.sh" -o /tmp/install-porter.sh \
    && bash /tmp/install-porter.sh \
    && rm /tmp/install-porter.sh \
    && porter version \
    && test -d "${PORTER_HOME}/runtimes" \
    && porter mixin install docker --version "${DOCKER_MIXIN_VERSION}" \
    && porter mixin install docker-compose --version "${DOCKER_COMPOSE_MIXIN_VERSION}"

COPY config.yaml /root/.porter/config.yaml

WORKDIR /workspace/IDEOS

CMD ["bash"]
