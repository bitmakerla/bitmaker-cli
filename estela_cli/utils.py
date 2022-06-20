import os
import yaml
import json
import click

from datetime import datetime
from estela_cli.templates import (
    ESTELA_AUTH_NAME,
    ESTELA_YAML_NAME,
    ESTELA_DIR,
    DATA_DIR,
    DOCKERFILE_NAME,
)


def get_project_path():
    return os.path.abspath(".")


def get_home_path():
    return os.path.expanduser("~")


def get_estela_yaml_path():
    project_path = get_project_path()
    return os.path.join(project_path, ESTELA_YAML_NAME)


def get_estela_dockerfile_path():
    project_path = get_project_path()
    return os.path.join(project_path, ESTELA_DIR, DOCKERFILE_NAME)


def get_host_from_env():
    return os.environ.get("ESTELA_API_HOST")


def get_username_from_env():
    return os.environ.get("ESTELA_USERNAME")


def get_password_from_env():
    return os.environ.get("ESTELA_PASSWORD")


def get_estela_settings():
    estela_yaml_path = get_estela_yaml_path()

    assert os.path.exists(estela_yaml_path), "{} not found.".format(ESTELA_YAML_NAME)

    with open(estela_yaml_path, "r") as estela_yaml:
        estela_config = yaml.full_load(estela_yaml)

    return estela_config


def get_estela_auth():
    home_path = get_home_path()
    estela_auth_path = os.path.join(home_path, ESTELA_AUTH_NAME)

    if not os.path.exists(estela_auth_path):
        return None

    with open(estela_auth_path, "r") as estela_auth_yaml:
        estela_auth = yaml.full_load(estela_auth_yaml)

    return estela_auth


def format_time(date):
    date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
    return date.strftime("%Y-%m-%d %H:%M")


def format_key_value_pairs(key_value_pairs):
    if not key_value_pairs:
        return ""

    result = ""
    for key_value in key_value_pairs[:-1]:
        result += "{}: {}\n".format(key_value["name"], key_value["value"])

    result += "{}: {}".format(key_value_pairs[-1]["name"], key_value_pairs[-1]["value"])
    return result


def format_tags(tags):
    if not tags:
        return ""
    result = ""
    for tag in tags[:-1]:
        result += "{}\n".format(tag["name"])
    result += "{}".format(tags[-1]["name"])
    return result


def save_data(filename, data):
    project_path = get_project_path()
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    filename = os.path.join(project_path, DATA_DIR, filename)
    with open(filename, "w", encoding="utf-8") as F:
        if "json" in filename:
            json.dump(data, F, ensure_ascii=False, indent=4)
        elif "csv" in filename:
            F.write(data)


def validate_key_value_format(ctx, param, value):
    try:
        key_value_pairs = []
        for pair in value:
            key, value = pair.split("=", 1)
            key_value_pairs.append({"name": key, "value": value})
        return key_value_pairs
    except:
        raise click.BadParameter("format must be 'NAME=VALUE'")


def set_tag_format(ctx, param, value):
    tags = []
    for tag_name in value:
        tags.append({"name": tag_name})
    return tags


def _in(path, ignore_files):
    for file in ignore_files:
        if path.startswith(file):
            return True