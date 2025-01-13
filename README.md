[![License](https://shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) 
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](/CONTRIBUTING.md)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)

# Content Security Policy Workshop - (AppSec Series)

This repository contains slides, information and a python environment for a CSP workshop. The workshop explores the basics of using Content Security Policies.

## Agenda

- Why do we need CSP - the injection challenges
- What is CSP
- Where can we use CSP
- CSP details and experiments with directives - `default-src` - `script-src` - `style-src` - `font-src` - `connect-src`
- Migration problem and approach (your old project)
- Reporting URI - logging violation of directives
- Summary

## Requirements

Install and use a Python 3.x environment with flask

- `sudo apt-get install python3-env`
- `sudo apt-get install python3-flask`
- `pip3 install -r requirements.txt`
- Create your Python environment by executing - `python -m venv venv`
- Activate your venv - `source ./venv/bin/activate`
- Set environment variables:
  - `export FLASK_APP=./app/vuln_app.py`
  - `export FLASK_ENV=development`
- Run flask - `flask --debug run`

## gitpod.io

You can also use gitpod.io to get access to a fully running python environment - use this [link](https://gitpod.io/#/https://github.com/Bouvet-deler/csp-workshop)

## Presentation

Genereate html from marp presentation
- Install `marp-cli` 👇
- `brew install marp-cli`
- on root directory run the command 👇
- `marp --theme-set ./themes -w ./content/`


---

[MIT LICENSE](./LICENSE)
