#!/usr/bin/env python   

from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware


class CustomUserAgent(UserAgentMiddleware):
    def process_request(self,request,spider):
        ua = 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36'
        request.headers.setdefault('User-Agent',ua)

        