#jython-standalone-2.7.1
#reference https://github.com/PortSwigger/example-event-listeners
#by NFS

from burp import IBurpExtender
from burp import IHttpListener
from burp import IExtensionStateListener
from java.io import PrintWriter
import sys, os
import re

class BurpExtender(IBurpExtender, IHttpListener):

    def	registerExtenderCallbacks(self, callbacks): #something to create an extension
        self._callbacks = callbacks
        callbacks.setExtensionName("Anti-captcha")
        self._stdout = PrintWriter(callbacks.getStdout(), True)
        callbacks.registerHttpListener(self)
      

    def processHttpMessage(self, toolFlag, messageIsRequest, RequestInfo):
        if  RequestInfo.getHttpService().toString()=="https://www.gsctx.org" and messageIsRequest: #condition to recieve get of gsctx.org

            aux=RequestInfo.getUrl().toString() #get the url of the request/message
            url_captcha=re.findall(r'https://www\.gsctx\.org:443/en/our-council/web-to-case/jcr:content/content/middle/par/captcha\.captcha\.png\?id=[0-9]+',str(aux))
            #^- filter to send url's captchas
            if len(url_captcha) >0:
                ocr_captcha=os.popen('python ocr-captcha.py {}'.format(url_captcha[0])).read() # this is to avoid import problems
                self._stdout.println(ocr_captcha)


