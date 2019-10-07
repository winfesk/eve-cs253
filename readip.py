def readIp(request):
    if 'X-Forwarded-For' in request.headers:
        return request.headers['X-Forwarded-For']
    if 'Host' in request.headers:
        return request.headers['Host']
    return 'ip unknown'
