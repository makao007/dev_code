#-*- coding:utf-8 -*-
import os
import web
import web_extract_context

urls = (
    '/', 'index'
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)


class index:
    def GET(self):
        i = web.input(url=None)
        url = i.url
        if url:
            context = web_extract_context.extract_context(url.strip())
        else:
            context = None 
        return render.extract_content(context)



if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

