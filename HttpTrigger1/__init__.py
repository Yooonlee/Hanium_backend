import logging
import sys
sys.path.insert(0, '/Users/kylee/Desktop/azure_practice/dj_pr')


import azure.functions as func
from dj_pr.wsgi import application
wsgi = func.WsgiMiddleware(app=application)


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return wsgi.main(req, context)