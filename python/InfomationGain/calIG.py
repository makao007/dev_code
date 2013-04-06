import math

data=[['y','y','y','yes'],
      ['y','y','y','yes'],
      ['y','n','n','yes'],
      ['y','n','n','yes'],
      ['y','y','n','yes'],
      ['n','y','y','no'],
      ['n','n','n','no'],
      ['n','n','n','no'],
      ['n','n','n','no'],
      ['n','n','y','yes'],
      ['n','n','y','no']]

data2=[['s','s','no','no'],
       ['s','l','yes','yes'],
       ['l','m','yes','yes'],
       ['m','m','yes','yes'],
       ['l','m','yes','yes'],
       ['m','l','no','yes'],
       ['m','s','no','no'],
       ['l','m','no','yes'],
       ['m','s','no','yes'],
       ['s','s','yes','no']]

# log (data) / log (2)
def log2 (data):
    return math.log(data) / math.log(2)

def not_zero (data):
    min_data = 0.00000001
    return data + min_data

def cal_single_entrophy(labels, labels_size=-1):
    min_data = 0.0001
    if labels_size == -1:
        labels_size = sum(labels.values())
    if labels_size == 0:
        raise 'No data'
        return
    result = - sum ( [((not_zero(label))/labels_size * log2((not_zero(label))/labels_size))  for label in labels.values()] )
    return result

def cal_feature_entrophy (features):
    feature_sum = 0.0
    for values in features.values():
        feature_sum += sum(values.values())

    result = 0.0
    for values in features.values():
        result += cal_single_entrophy (values) * sum(values.values()) / feature_sum
    return result

def gen_labels (data):
    labels = []
    for line in data:
        if line[-1] not in labels:
            labels.append (line[-1])
    return labels

def label_entrophy(data):
    labels = {}
    labels_size = len(data)
    for line in data:
        if labels.has_key(line[-1]):
            labels[line[-1]] += 1
        else:
            labels[line[-1]] = 1
    result = cal_single_entrophy (labels, labels_size)
    return result


def calGI (data):
    line_length = len(data[0])-1
    labels = gen_labels(data)

    attribute_entrophy = []

    # compute every attribute 
    for index in range(line_length):
        features = {}

        #the feature frecuncy
        for line in data:
            cur_label = line[-1]
            if not features.has_key(line[index]):
                tmp = dict( [(label,0) for label in labels])
                features[line[index]] = tmp
            features[line[index]][cur_label] += 1

        attribute_entrophy.append (cal_feature_entrophy (features))
    return attribute_entrophy

a=label_entrophy(data2)
b=calGI (data2)
print a
for i in b:
    print a-i

