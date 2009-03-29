#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import rapidsms

# a pointless app to demonstrate the structure
# of sms applications without magic decorators
class App(rapidsms.app.App):

    def start(self):
        self.name = 'alpha'

    def handle(self, message):
        self.info("Alpha app got messge!")
        message.respond("Alpha!")