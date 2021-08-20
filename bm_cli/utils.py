import os
import yaml

from datetime import datetime
from bm_cli.templates import (
    BITMAKER_AUTH_NAME,
    BITMAKER_YAML_NAME,
    BITMAKER_DIR,
    DOCKERFILE_NAME,
)


def get_project_path():
    return os.path.abspath(".")


def get_home_path():
    return os.path.expanduser("~")


def get_bm_yaml_path():
    project_path = get_project_path()
    return os.path.join(project_path, BITMAKER_DIR, BITMAKER_YAML_NAME)


def get_bm_dockerfile_path():
    project_path = get_project_path()
    return os.path.join(project_path, BITMAKER_DIR, DOCKERFILE_NAME)


def get_host_from_env():
    return os.environ.get("BM_API_HOST")


def get_username_from_env():
    return os.environ.get("BM_USERNAME")


def get_password_from_env():
    return os.environ.get("BM_PASSWORD")


def get_bm_settings():
    bm_yaml_path = get_bm_yaml_path()

    assert os.path.exists(bm_yaml_path), "{} not found.".format(BITMAKER_YAML_NAME)

    with open(bm_yaml_path, "r") as bm_yaml:
        bm_config = yaml.full_load(bm_yaml)

    return bm_config


def get_bm_auth():
    home_path = get_home_path()
    bm_auth_path = os.path.join(home_path, BITMAKER_AUTH_NAME)

    if not os.path.exists(bm_auth_path):
        return None

    with open(bm_auth_path, "r") as bm_auth_yaml:
        bm_auth = yaml.full_load(bm_auth_yaml)

    return bm_auth


def format_time(date):
    date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
    return date.strftime("%Y-%m-%d %H:%M")


def format_args(args):
    if not args:
        return ""

    result = ""
    for arg in args[:-1]:
        result += "{}: {}\n".format(arg["name"], arg["value"])

    result += "{}: {}".format(args[-1]["name"], args[-1]["value"])
    return result
