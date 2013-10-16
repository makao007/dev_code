from decision_tree_class import *

def test_1 ():
    feature_names = ['no surfacing','flippers']
    dataset1 = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no'], [1, 1, 'yes'], [1, 1, 'yes'], [1, 1, 'no']]

    d = D_tree()
    d.set_feature (feature_names)      # option
    #d.set_with_percentage (False)
    d.make_tree (dataset1)

    #d.show_dict(d.fill_tree(d.tree))
    d.show_dict (d.tree)
    
    print d.classify ([0,0])
    print d.classify ([0,1])
    print d.classify ([1,0])
    print d.classify ([1,1])


def test_2 ():
    d = D_tree()
    #d.make_tree('../german_credit_data/german-numeric.txt')
    d.make_tree('a.txt')
    d.show_dict (d.fill_tree(d.tree))
    d.save_tree ('a.dat')

def test_3 ():
    d = D_tree ('a.dat')  # load the tree data
    print d.tree
    print d.feature
    d.show_dict(d.fill_tree(d.tree))

    
test_1()
test_2()
test_3()
