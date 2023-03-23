import numpy as np
import matplotlib.pyplot as plt
class ID3():
    def __init__(self):
        self.root = None

    def fit(self, X, y):
        self.root = DecisionTreeNode().split(X, y)
        return self

    def __str__(self):
        return str(self.root)


def entropy(labels):
    """returns the same as scipy.stats.entropy([positive, negative], base=2)"""
    n = len(labels)
    if n == 0:
        return 0.0
    positive = sum(labels) / n
    negative = 1 - positive
    if positive == 0 or negative == 0:
        return 0.0
    return -positive * np.log2(positive) - negative * np.log2(negative)


# def plot_split(optimal_split,X,y):
#     colormap = {1:'blue', 0:'red'}
#     y_colors = [colormap[i] for i in y]
#     fig = plt.figure(dpi=90)
#     plt.xlabel('x1')
#     plt.ylabel('x2')

#     for i,sample in enumerate(X):
#         plt.scatter(x=sample[0], y=sample[1], c=y_colors[i], alpha=0.4)
#     if optimal_split[0] == 0:
#         plt.axvline(optimal_split[1], color='r', linestyle='-')
#     else:
#         plt.axhline(optimal_split[1], color='r', linestyle='-')
#     plt.show()

class DecisionTreeNode():
    def __init__(self):
        self.label = None
        self.split_point = None
        self.split_feature = None
        self.left_child = None
        self.right_child = None

    def get_all_possible_split_points(self, features, labels):
        nr_samples, nr_features = features.shape
        split_points = [] # this should be a list of tuples (f_idx, split_at) where split_at is the value to split feature f_idx
        # add tuples using: split_points.append((f_idx, split_at))
        for f_idx in range(nr_features):
            idx_sort = features[:, f_idx].argsort()
            features = features[idx_sort, :]
            labels = labels[idx_sort]
            for i in range(len(features)-1):
                if features[i][f_idx] != features[i+1][f_idx] and labels[i] != labels[i+1]:
                    split_value = (features[i][f_idx] + features[i+1][f_idx]) / 2
                    split_points.append((f_idx,split_value))
            # TODO: check for consecutive samples whether the labels and features are different
            # be careful to not compare the 0th sample with the last sample when indexing
            # if labels and feature values are different, compute splitting values and add to list as shown above
        return split_points

    def get_optimal_split_point(self, features, labels):
        split_feature, split_point = None, None
        possible_split_points = self.get_all_possible_split_points(features, labels)
        current_best_ig = -np.Inf
        ig = list()
        for split_point in possible_split_points:
            ig.append(self.get_information_gain(features,labels,split_point))
        current_best_ig = np.argmax(ig)
        split_feature,split_point = possible_split_points[current_best_ig][0],possible_split_points[current_best_ig][1]
        return split_feature, split_point

    def get_information_gain(self, x, y, split_point):
        ig = 0.0
        gen_entropy = entropy(y)
        right_split_y = list()
        left_split_y = list()
        left_split = list()
        right_split = list()
        for i,feature in enumerate(x):
            if feature[split_point[0]] <= split_point[1]:
                left_split_y.append(y[i])
                left_split.append(feature)
            else:
                right_split_y.append(y[i])
                right_split.append(feature)
        top_split_entropy = entropy(right_split_y)
        bottom_split_entropy = entropy(left_split_y)
        ig = gen_entropy - (len(right_split_y)/len(y))*top_split_entropy - (len(left_split_y)/len(y))*bottom_split_entropy
        #ig = gen_entropy - ((top_split_entropy*top_sum)/len(y)) - ((bottom_split_entropy*bottom_sum)/len(y))
        # TODO: implement the information gain as described in the slides
        # use the provided entropy() function
        # use <= and > for comparison (to get a comparable result)
        return ig

    def split(self, X, y):
        if np.all(y == y[0]):
            #ALL LABELS ARE THE SAME
            self.label = int(y[0])
        right_split_y = list()
        left_split_y = list()
        left_split = list()
        right_split = list()
        if not np.all(y == y[0]):
            self.split_feature, self.split_point = self.get_optimal_split_point(np.asarray(X),np.asarray(y))
            for i,feature in enumerate(X):
                if feature[self.split_feature] <= self.split_point:
                    left_split_y.append(y[i])
                    left_split.append(feature)
                else:
                    right_split_y.append(y[i])
                    right_split.append(feature)
            
            self.left_child, self.right_child = DecisionTreeNode(), DecisionTreeNode()
            self.left_child.split(left_split,left_split_y)
            self.right_child.split(right_split,right_split_y)
        # TODO: implement the ID3 algorithm
        # if you reach a node that only contains samples with the same label store the label
        # otherwise compute the optimal split point using get_optimal_split_point
        # and create the child nodes (store them in self.left_child and self.right_child)
        # call split(X_left, y_left) and split(X_right, y_right) to recursively create the tree
        # again: use <= and > for comparison

        return self

    def __str__(self):
        if self.label is not None: return "(" + str(self.label) + ")"

        str_value = str(self.split_feature) + ":" + str(self.split_point) + "|"
        str_value = str_value + str(self.left_child) + str(self.right_child)
        return str_value