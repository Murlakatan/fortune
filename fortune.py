#!/usr/bin/python
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------- #
#                                                                                 #
#       Plugin for iSida Jabber Bot                                               #
#       Especially for the conference elastic@conference.jabber.ru                #
#       Copyright (C) 2012 Cloud <rain@xabber.de>                                 #
#                                                                                 #
#  This program is free software: you can redistribute it and/or modify           #
#  it under the terms of the GNU General Public License as published by           #
#  the Free Software Foundation, either version 3 of the License, or              #
#  (at your option) any later version.                                            #
#                                                                                 #
#  This program is distributed in the hope that it will be useful,                #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of                 #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                  #
#  GNU General Public License for more details.                                   #
#                                                                                 #
#  You should have received a copy of the GNU General Public License              #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.          #
#                                                                                 #
# ------------------------------------------------------------------------------- #

fortServer = 'fortune plugins/fortune/server'
fortAll = 'fortune plugins/fortune/other/'
fortComp = 'fortune plugins/fortune/other/computer'

def fortune(type, jid, nick, text):
	if text == '':
        	msg = shell_execute(fortServer)
	elif text == 'all':
		msg = shell_execute(fortAll)
	elif text == 'pc':
		msg = shell_execute(fortComp)
	else: msg = 'The unknown parameters. For more information, type "help fortune".'
	
        send_msg(type, jid, nick, '\n' + msg)

global execute

execute = [(4, 'fortune', fortune, 2, L('\nThe plugin provides a variety of phrases on demand.\nHow to use:\nfortune - tell good advice about working in ubuntu server in Russian.\nfortune pc - tell a joke on the subject of "computer" in Russian.\nfortune all - tell a quote or aphorism in Russian.'))]
