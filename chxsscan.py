
'''
######################################################################################
# About :                                                                            #
#                                                                                    #
# Description: This Program Powered By Charon Security Agency                        #
# Made for: Finding XSS Vulnerabilities In WebSites By Crawling.                     #
# Programmer: Ch4120n                                                                #
#                                                                                    #
# Copyright :                                                                        #
#                                                                                    #
# Charon XSSCAN (C) <2024> <Charon Security Agency>                                  #
# This Program Is Free Software: You Can Redistribute It                             #
# It Under The Terms Of The  `Charon General Black License`  As Published By         #
# The Black Hacking Software Foundation , Either Version 1 Of The License.           #
# This Program Is Distributed In The Hope That It Will Be Useful,                    #
# But Without Any Warranty .  See The                                                #
# `Charon General Black License` For More Details.                                   #
# You Should Have Received A Copy Of The  `Charon General Black License`             #
# Along With This Program. If Not, See <http://charonsecurityagency.github.io/cgbl>  #
#                                                                                    #
######################################################################################
'''

import argparse
from lib.helper.helper import *
from lib.helper.Log import *
from lib.core import *
from random import randint,choice
from lib.crawler.crawler import *
from pystyle import Colors, Colorate
from colorama import Fore, init
init()
def check(getopt):
	payload=int(getopt.payload_level)
	if payload > 6 and getopt.payload is None:
		Log.info("Do you want use custom payload (Y/n)?")
		answer=input("> "+W) 
		if answer.lower().strip() == "y":
			Log.info("Write the XSS payload below")
			payload=input("> "+W)
		else:
			payload=core.generate(randint(1,6))
	
	else:
		payload=core.generate(payload)
			
	return payload if getopt.payload is None else getopt.payload

def Diagonal(logo=None):
	return Colorate.Diagonal(Colors.rainbow, logo)
def Vertical(logo=None):
	return Colorate.Vertical(Colors.rainbow, logo)
def Horizontal(logo=None):
	return Colorate.Horizontal(Colors.rainbow, logo)
def start():
	parse=argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,usage="Chxsscan --url <target> [options]",add_help=False)
	
	pos_opt=parse.add_argument_group("Options")
	pos_opt.add_argument('-h',"--help",action="store_true",default=False,help="Show usage and help parameters")
	pos_opt.add_argument("-u",'--url',metavar="",help="Target url (e.g. http://testphp.vulnweb.com)")
	pos_opt.add_argument('-d', "--depth",metavar="",help="Depth web page to crawl. Default: 2",default=2)
	pos_opt.add_argument('-pl', "--payload-level",metavar="",help="Level for payload Generator, 7 for custom payload. {1...6}. Default: 6",default=6)
	pos_opt.add_argument('-p', "--payload",metavar="",help="Load custom payload directly (e.g. <script>alert(2005)</script>)",default=None)
	pos_opt.add_argument('-m', "--method",metavar="",help="Method setting(s): \n\t0: GET\n\t1: POST\n\t2: GET and POST (default)",default=2,type=int)
	pos_opt.add_argument("--user-agent",metavar="",help="Request user agent (e.g. Chrome/2.1.1/...)",default=agent)
	pos_opt.add_argument('-s', "--single",metavar="",help="Single scan. No crawling just one address")
	pos_opt.add_argument("--proxy",default=None,metavar="",help="Set proxy (e.g. {'https':'https://10.10.1.10:1080'})")
	pos_opt.add_argument('-a', "--about",action="store_true",help="Print information about `Charon XSSCAN` tool")
	pos_opt.add_argument('-c', "--cookie",help="Set cookie (e.g {'ID':'1094200543'})",default='''{"ID":"1094200543"}''',metavar="")
	
	getopt=parse.parse_args()
	ranbows = [Vertical, Horizontal]
	ranbows = choice(ranbows)

	print(ranbows(logo))
	Log.info("Starting Charon XSSCAN...")
	if getopt.url:
		try:
			core.main(getopt.url,getopt.proxy,getopt.user_agent,check(getopt),getopt.cookie,getopt.method)
			
			crawler.crawl(getopt.url,int(getopt.depth),getopt.proxy,getopt.user_agent,check(getopt),getopt.method,getopt.cookie)
		except KeyboardInterrupt:
			print(Fore.RED + '\n[-] Canceling By User.')
	elif getopt.single:
		core.main(getopt.single,getopt.proxy,getopt.user_agent,check(getopt),getopt.cookie,getopt.method)
		
	elif getopt.about:
		print("""
**************
Project: Charon XSS Scanner
License: CGBL
Author: Ch4120N
Last updated: February 26, 2024
Note: Use your own risk
****************
""")
	else:
		parse.print_help()
		
if __name__=="__main__":
	start()
	# console.print("Danger, Will Robinson!", style="blink bold red underline on white")
 
# import pystyle
	
