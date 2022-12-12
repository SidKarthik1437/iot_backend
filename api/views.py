from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import functions as fn
from threading import Thread


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/scripts/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of scripts'
        },

    ]

    return Response(routes)


@api_view(['POST'])
def led(req):

    type = req.data['fn']
    # fn.led.switch(type)
    # fn.led.setup()
    if type == 'blink':
        # global t
        fn.led.start()
    elif type == 'stop':
        # global t
        fn.led.stop()

    return Response("LED - %s Executed!" % type)
