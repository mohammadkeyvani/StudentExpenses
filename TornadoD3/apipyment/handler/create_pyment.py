# -*- coding: utf-8 -*-
# !/usr/bin/env python
__author__ = 'Elf'

from base import WebBaseHandler
from models import *
import json


class CreateHandler(WebBaseHandler):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        create_post = json.loads(self.request.body)
        try:

            create_item = Buy().create(amount=create_post['amount'], concern=create_post['concern'],
                                       payer_id=create_post['payer_'],per_share=create_post['per_share'],date=create_post['date'])

        except:
            print "error"
            self.result['message'] = "user id not found !!!!!"
            self.finish(self.result)
