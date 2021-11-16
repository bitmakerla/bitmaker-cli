<h1 align="center"> Bitmaker Cloud CLI </h1>

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Bitmaker Cloud CLI is the command line client to interact with Bitmaker Cloud API. Allows the user to perform the following actions:
- Link a Scrapy project with a project in Bitmaker Cloud.
- Create projects, jobs and cronjobs in Bitmaker Cloud.
- Get the data of a job.

```bash
$ bitmaker
Usage: bitmaker [OPTIONS] COMMAND [ARGS]...

Options:
  --version   Show the version and exit.
  -h, --help  Show this message and exit.
  -l, --local When init a project, indicate that you use local-registry       

Commands:
  context  Show your current context
  create   Create a resource
  delete   Delete a resource
  deploy   Deploy Scrapy project to Bitmaker Cloud
  data     Returns all the data of a job and saves it in a json file
  init     Initialize bitmaker project for existing scrapy project
  list     Display the available resources
  login    Save your credentials
  logout   Remove your credentials
  stop     Stop an active job or cronjob

Args:
  project  All projects or a project if it is followed by the ID of that project
  spider   All the spiders or a spider if it is followed by the ID of that spider
  job      All jobs or a job if the ID of that job follows
  cronjob  All cronjobs or a cronjob if it is followed by the ID of that cronjob 
```

## Installation

```bash
$ python setup.py install
```

## Testing

```bash
$ pip install -r requirements/test.txt
$ python tests.py
```

## Formatting 

```bash
$ pip install -r requirements/dev.txt
$ black .
```
