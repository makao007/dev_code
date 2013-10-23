#-*- coding:utf-8 -*-
import os
import web
from context.web_extract_context import extract_context

urls = (
    '/extract_context', 'index'
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)


class index:
    def GET(self):
        i = web.input(url=None)
        url = i.url
        if url:
            context = extract_context(url.strip())
        else:
            context = None 
        return render.extract_content(context)

if 'SERVER_SOFTWARE' in os.environ:         #in BAE server
    app = web.application(urls, globals()).wsgifunc()
    from bae.core.wsgi import WSGIApplication
    application = WSGIApplication(app)

elif __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
