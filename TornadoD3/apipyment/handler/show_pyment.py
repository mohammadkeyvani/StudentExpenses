#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Elf'

from base import WebBaseHandler
from models import *


class ShowHandler(WebBaseHandler):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):

        id_user = self.get_argument("user_id", None)
        id_payment = self.get_argument("payment_id", None)
        print
        try:
            id_user = int(id_user)
            id_payment = int(id_payment)
        except:
            self.result['message'] = "Invalid INT size."
            self.finish(self.result)
            return
        if id_user:
            try:
                list_pay = []
                show_user = User().select().where(User.id == id_user)
                show_pay = Payment().select().where(Payment.User == id_user) | (Payment.id == id_payment)
                for item in show_pay:
                    list_pay.append({'id_payment': item.id, 'amount': item.amount, 'type': item.type,
                                     'payer_id': item.payer_id, 'date': item.date})
                for item in show_user:
                    list_pay.append({'user_id': item.id, 'name_user': item.name})

                self.result['value'] = list_pay
                self.result['status'] = True
                self.result['message'] = "operation is success "
                self.finish(self.result)
            except:
                print "error"
                self.result['message'] = "user id not found !!!!!"
                self.finish(self.result)


class ShowAllHandler(WebBaseHandler):
    def get(self, *args, **kwargs):
        try:
            list_pay = []
            show_pay = Payment().select()
            for item in show_pay:
                show_user = User().select().where(User.id == item.User)
                list_pay.append({'id_payment': item.id, 'amount': item.amount, 'type': item.type,
                                 'payer_id': item.payer_id, 'date': item.date})
                for item1 in show_user:
                    list_pay.append({'user_id': item1.id, 'name_user': item1.name})

            self.result['value'] = list_pay
            self.result['status'] = True
            self.result['message'] = "operation is success "
            self.finish(self.result)
        except:
            print "error"
            self.result['message'] = "user id not found !!!!!"
            self.finish(self.result)

    def post(self, *args, **kwargs):
        pass
