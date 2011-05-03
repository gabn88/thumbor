#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

from thumbor.handlers.eventlet.base import Handler
from thumbor.cli import Cli

class HealthCheckHandler(Handler):

    def get(self):
        cli = Cli()
        return cli.health_check()
