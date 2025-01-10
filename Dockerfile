################################
# BASE
################################
FROM python:3.12.8-slim-bookworm AS python-base

RUN apt-get update && \
    apt-get install -y \
    apt-transport-https \
    gnupg \
    ca-certificates \
    build-essential \
    git \
    nano \
    curl
ENV VENV_PATH="/opt/.venv"
################################
# DEPENDENCIES
################################
FROM python-base AS dependencies
WORKDIR /opt

ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH" \
    UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1

# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev
    
################################
# PRODUCTION
################################
FROM python-base AS production

WORKDIR /opt

# Enable bytecode compilation
# Copy from the cache instead of linking since it's a mounted volume
ENV PATH="$VENV_PATH/bin:$PATH"

COPY . .
COPY --from=dependencies --chown=opt:opt $VENV_PATH $VENV_PATH
