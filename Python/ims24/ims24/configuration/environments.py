#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#
# environments.py
# @Author : Gustavo F (gustavo@gmf-tech.com)
# @Link   : https://github.com/sharkguto
# @Date   : 17/02/2019 10:21:52
import os

# for local tests https://github.com/localstack/localstack

# elastic search variables
ES_SERVER = os.getenv("ES_SERVER") or "localhost"
ES_SERVER_PORT = int(os.getenv("ES_SERVER_PORT") or 4571)

# environment name
ENVIRONMENT = os.getenv("ENVIRONMENT") or "DEVELOPMENT"

# database variables
IMS_HOSTNAME = os.getenv("IMS_HOSTNAME")
IMS_USERNAME = os.getenv("IMS_USERNAME")
IMS_PASSWORD = os.getenv("IMS_PASSWORD")
IMS_DB_NAME = os.getenv("IMS_DB_NAME")
IMS_PORT = int(os.getenv("IMS_PORT") or 5432)

BASE_URL_CRAWLER = "http://www.immobilienscout24.de/Suche/S-T/P-{pagination}/Wohnung-Miete/Berlin/Berlin"

