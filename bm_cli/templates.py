# Auth templates

BITMAKER_AUTH_NAME = ".bitmaker.yaml"

BITMAKER_AUTH = """\
token: $bm_token
host: $bm_host
"""


# Init project templates

BITMAKER_DIR = ".bitmaker"

DATA_DIR = "project_data"

DOCKER_APP_DIR = "/usr/src/app"

DOCKER_DEFAULT_REQUIREMENTS = "requirements.txt"

DOCKERFILE_NAME = "Dockerfile-bitmaker"

DOCKERFILE = """\
FROM python:$python_version

# must be in base image
RUN pip install git+https://github.com/bitmakerla/bitmaker-entrypoint.git

RUN mkdir -p {app_dir}
WORKDIR {app_dir}
COPY . {app_dir}

RUN pip install --no-cache-dir -r $requirements_path
RUN mkdir /fifo-data
""".format(
    app_dir=DOCKER_APP_DIR
)

BITMAKER_YAML_NAME = "bitmaker.yaml"

BITMAKER_YAML = """\
project:
  pid: $project_pid
deploy:
  ignore: [$project_data_path]
"""

# General templates

OK_EMOJI = "\U00002705"
BAD_EMOJI = "\U0000274C"
CLOCK_EMOJI = "\U000023F3"
