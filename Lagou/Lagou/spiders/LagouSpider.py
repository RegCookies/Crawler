# -*- coding: utf-8 -*-
import scrapy
import json
from Lagou.items import LagouItem

class LagouspiderSpider(scrapy.Spider):
    name = 'LagouSpider'
    #allowed_domains = ['www.lagou.com/jobs/list_python?city=%E4%B8%8A%E6%B5%B7']
    #start_urls = ['https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false&isSchoolJob=1'] 
    start_urls =  'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false&isSchoolJob=1'
    kd = "python"
    curpage = 1
    total_page = 10
    
    headers = {
       'Accept': 'application/json, text/javascript, */*; q=0.01',
#Cookie: user_trace_token=20181128143718-523f979d-3026-43ee-8278-ceea5a57894e; _ga=GA1.2.15286503.1543387039; LGUID=20181128143719-0da24efc-f2d8-11e8-8c2e-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; _gid=GA1.2.1250438074.1543492435; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22167620db3336a4-03a4adf5a50d5c-24414032-8294400-167620db3349db%22%2C%22%24device_id%22%3A%22167620db3336a4-03a4adf5a50d5c-24414032-8294400-167620db3349db%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22m_cf_cpc_baidu_pc%22%7D%7D; ab_test_random_num=0; hasDeliver=0; JSESSIONID=ABAAABAAADEAAFI3DFF4015389D6252DC087753BC2F07E7; PRE_UTM=; X_HTTP_TOKEN=cb748c0a9716d07b611e82e970511278; LG_LOGIN_USER_ID=1ed64040bd1476d5408d6f104b98d506f0df7b1ba82212fc332cbb533f0362b7; _putrc=417EC13BD65B1B3A123F89F2B170EADC; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B72016; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; gate_login_token=6514dfef6e38aab6e3a9b68ae5aed61208ba586e209f89d7028b028f3ab18a50; LGSID=20181201003311-a0bbb25e-f4bd-11e8-8ca7-5254005c3644; PRE_HOST=coding.imooc.com; PRE_SITE=https%3A%2F%2Fcoding.imooc.com%2Flearn%2Fquestiondetail%2F27042.html; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2FPython%2F%3FlabelWords%3Dlabel; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1543576768,1543591610,1543595592,1543595627; SEARCH_ID=e67e4371df214e10894d61aa718e379f; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1543595823; LGRID=20181201003703-2a94d5df-f4be-11e8-8ca7-5254005c3644; TG-TRACK-CODE=search_code
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?city=%E4%B8%8A%E6%B5%B7&cl=false&fromSearch=true&labelWords=&suginput=&isSchoolJob=1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36',
    } 
    
    my_cookies ={
        'Cookie': 'user_trace_token=20181128143718-523f979d-3026-43ee-8278-ceea5a57894e;LGUID=20181128143719-0da24efc-f2d8-11e8-8c2e-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; _gid=GA1.2.1250438074.1543492435; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22167620db3336a4-03a4adf5a50d5c-24414032-8294400-167620db3349db%22%2C%22%24device_id%22%3A%22167620db3336a4-03a4adf5a50d5c-24414032-8294400-167620db3349db%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22m_cf_cpc_baidu_pc%22%7D%7D; ab_test_random_num=0; hasDeliver=0; JSESSIONID=ABAAABAAADEAAFI3DFF4015389D6252DC087753BC2F07E7; PRE_UTM=; X_HTTP_TOKEN=cb748c0a9716d07b611e82e970511278; LG_LOGIN_USER_ID=1ed64040bd1476d5408d6f104b98d506f0df7b1ba82212fc332cbb533f0362b7; _putrc=417EC13BD65B1B3A123F89F2B170EADC; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B72016; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; gate_login_token=6514dfef6e38aab6e3a9b68ae5aed61208ba586e209f89d7028b028f3ab18a50; LGSID=20181201003311-a0bbb25e-f4bd-11e8-8ca7-5254005c3644; PRE_HOST=coding.imooc.com; PRE_SITE=https%3A%2F%2Fcoding.imooc.com%2Flearn%2Fquestiondetail%2F27042.html; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2FPython%2F%3FlabelWords%3Dlabel; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1543576768,1543591610,1543595592,1543595627; SEARCH_ID=e67e4371df214e10894d61aa718e379f; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1543595823; LGRID=20181201003703-2a94d5df-f4be-11e8-8ca7-5254005c3644'
    }
    def start_requests(self): 
        return [scrapy.http.FormRequest(self.start_urls,method = 'POST',headers=self.headers,cookies=self.my_cookies,formdata={'first':'true','pn':str(self.curpage),'kd':self.kd},callback=self.parse)]
    def parse(self, response):
       # print(response.text) 
        
        result = json.loads(response.body) 
        
        jobs =result['content']['positionResult']['result']
        
        for job in jobs:
            item = LagouItem()
            
            item['city'] = job['city'] 
            item['companyName'] = job['companyFullName'] 
            item['companyShortName'] = job['companyShortName'] 
            item['companySize'] = job['companySize'] 
            item['district'] = job['district']
            item['education'] = job['education']
            item['jobNature'] = job['jobNature']
            item['positionName'] = job['positionName']
            sal = job['salary']
            sal = sal.split('-')
            if len(sal) == 1:
                item['salaryMax'] = int(sal[0][:sal[0].find('k')])
            else:
                item['salaryMax'] = int(sal[1][:sal[1].find('k')])
            item['salaryMin'] = int(sal[0][:sal[0].find('k')])
            item['salaryAvg'] = (item['salaryMin'] + item['salaryMax'])/2
            
            item['positionAdvantage'] = job['positionAdvantage'] 
            
            yield item

        if self.curpage <= self.total_page:
            self.curpage += 1
            yield scrapy.http.FormRequest(self.start_urls,method = 'POST',headers=self.headers,cookies=self.my_cookies,formdata={'first':'true','pn':str(self.curpage),'kd':self.kd},callback=self.parse)
