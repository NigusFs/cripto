from burp import IBurpExtender
from java.io import PrintWriter
from java.lang import RuntimeException
import sys, os
class BurpExtender(IBurpExtender):
    
    
    def	registerExtenderCallbacks(self, callbacks):
               

        stdout = PrintWriter(callbacks.getStdout(), True)
        stderr = PrintWriter(callbacks.getStderr(), True)
       
       	ocr_captcha=os.popen('python ocr-captcha.py').read()
        stdout.println(ocr_captcha) #print in console

        stderr.println("errors")
        callbacks.issueAlert("alerts")
        raise RuntimeException("exception")