#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cherrypy
import json
import procesador

sec_collatz = procesador.collatz()

class WS(object):

	@cherrypy.expose
	@cherrypy.tools.json_in()
	
	def calcular_collatz(self):
		num = cherrypy.request.json
		output = json.dumps(sec_collatz.collatz(num))
		return output

if __name__ == '__main__':
	cherrypy.config.update({'server.socket_host': '0.0.0.0'})
	cherrypy.quickstart(WS())
