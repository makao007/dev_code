#-*- coding:utf-8 -*-
import os
import web
from dtree.decision_tree_class import D_tree

urls = (
    '/', 'index',
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)


class index:
    def GET(self):
        return render.index()

if 'SERVER_SOFTWARE' in os.environ:         #in BAE server
    app = web.application(urls, globals()).wsgifunc()
    from bae.core.wsgi import WSGIApplication
    application = WSGIApplication(app)

elif __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

