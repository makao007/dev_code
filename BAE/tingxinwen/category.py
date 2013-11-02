#-*- coding:utf-8 -*-
import os
import web
import math
from group_text.TextClassification import TextClassification

urls = (
    '/category', 'index'
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

tc = TextClassification()
tc.load_info_file ('group_text/info.dat')

class index:
    def GET(self):
        return render.category()

    def POST(self):
        global tc
        output_template = """{'result':'%s', 'rank':%s}"""
        content = web.input(article=None).get('article')
        if not content:
            return 'Error, input Empty'
        
        text,result = tc.get_category_text(content)

        result = sorted (result, key=lambda x: x[1], reverse=True)

        if result[0][1] <= 0.0000000001:
            print result
            return output_template % ("对不起，我也不知道这属于什么分类",[])

        output = []
        for i in result:
            x1 = i[0].decode('gbk')
            x2 = (i[1]-result[-1][1])/(result[0][1]-result[-1][1])+0.01
            x3 = i[2]
            output.append ([x1,x2,x3])

        output = output_template  %  (text.decode('gbk'), output)
        return output.encode('utf8')

if 'SERVER_SOFTWARE' in os.environ:         #in BAE server
    app = web.application(urls, globals()).wsgifunc()
    from bae.core.wsgi import WSGIApplication
    application = WSGIApplication(app)
elif __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

