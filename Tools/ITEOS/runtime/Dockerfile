FROM docker:27-cli

ARG PORTER_VERSION=v1.1.0

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

RUN curl -fsSL "https://cdn.porter.sh/${PORTER_VERSION}/install-linux.sh" | bash \
    && porter version \
    && porter mixin install docker \
    && porter mixin install docker-compose

WORKDIR /workspace/ITEOS

CMD ["bash"]
