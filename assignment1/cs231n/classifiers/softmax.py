from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    num_train = X.shape[0]
    num_classes = W.shape[1]

    for i in range(num_train):
        score_i = X[i].dot(W)
        score_i_max = np.max(score_i)
        score_i -= score_i_max  # for numeric stability
        loss += -np.log(np.exp(score_i[y[i]]) / np.sum(np.exp(score_i)))
        for j in range(num_classes):
            prob = np.exp(score_i[j]) / sum(np.exp(score_i))
            if j == y[i]:
                dW[:, j] += (-1 + prob) * X[i]  # how to work out?
            else:
                dW[:, j] += prob * X[i]  # how to work out?

    loss /= num_train
    loss += 0.5 * reg * np.sum(W*W)

    dW = dW / num_train + reg * W

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    num_train = X.shape[0]
    num_classes = W.shape[1]

    scores = X.dot(W)
    scores -= np.max(scores, axis=1, keepdims=True)
    prob = np.exp(scores)/np.sum(np.exp(scores), axis=1, keepdims=True)  # (N, C)

    correct_class_log = -np.log(prob[range(num_train), y])  # [1, y[1]], ... for n pics

    loss = np.sum(correct_class_log) / num_train + 0.5 * reg * np.sum(W * W)

    dscores = prob
    dscores[range(num_train), y] -= 1  # only [1, y[1]], ... for n pics minus 1.

    dW = X.T.dot(dscores) / num_train + reg * W

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW
