#-*- coding:utf-8 -*-
import os
import web
from dtree.decision_tree_class import D_tree

urls = (
    '/dtree', 'index'
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)


class index:
    def GET(self):
        return render.dtree(None,None)

    def POST(self):
        data_train = web.input(data_train=None).get('data_train')
        data_test  = web.input(data_test=None).get('data_test')
        if not data_train:
            return render.dtree(None,None)
        
        tmp = data_train.split('\n')
        if len(tmp) < 2:
            return render.dtree('','please split the dataset into different lines')

        dtree = D_tree () 
        dataset1 = dtree.string_to_dataset (data_train)
        dataset2 = dtree.string_to_dataset (data_test)
        if data_train and data_test :
            if len(dataset1[0]) != len(dataset2[0])+1:
                return render.dtree('','the length of feature not match')

        dtree.make_tree (dataset1)
        #tree = dtree.string_dict(dtree.fill_tree(dtree.tree))
        tree = dtree.html_dict(dtree.fill_tree(dtree.tree))

        
        labels = []
        for i in dataset2:
            if not i:
                continue
            labels.append (dtree.classify(i)) 
        return render.dtree(tree, labels)



if 'SERVER_SOFTWARE' in os.environ:         #in BAE server
    app = web.application(urls, globals()).wsgifunc()
    from bae.core.wsgi import WSGIApplication
    application = WSGIApplication(app)
elif __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

