import os
 
# An example in that book, the training set and parameters' sizes are fixed
training_set = [[(3, 3), 1], [(4, 3), 1], [(1, 1), -1]]
 
w = [0, 0]
b = 0
 
# update parameters using stochastic gradient descent
def update(item):
    global w, b
    print w, b # you can uncomment this line to check the process of stochastic gradient descent
    w[0] = w[0] + 1 * item[1] * item[0][0]
    w[1] = w[1] + 1 * item[1] * item[0][1]
    b = b + 1 * item[1]
 
# calculate the functional distance between 'item' an the dicision surface
def cal(item):
    global w, b
    res = 0
    for i in range(len(item[0])):
        res += item[0][i] * w[i]
    res += b
    res *= item[1]
    return res
 
# check if the hyperplane can classify the examples correctly
def check():
    flag = False
    for item in training_set:
        if cal(item) <= 0:
            flag = True
            update(item)
    if not flag:
        print "RESULT: w: " + str(w) + " b: "+ str(b)
        os._exit(0)
    flag = False
 
if __name__=="__main__":
    for i in range(1000):
        check()
    print "The training_set is not linear separable. "

