import re 
from urllib import request

class Spider():
    url = "https://www.panda.tv/cate/hearthstone"
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>(*?)</span>'
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls=str(htmls,encoding='utf-8')
        return htmls
    def __analysis(self,htmls):
        root_html = re.findall(Spider.root_pattern,htmls)   
        print(root_html[0]) 
        a = 1
    
    
    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)
   



spider =  Spider()
spider.go()  