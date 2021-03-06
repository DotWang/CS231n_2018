import numpy as np
from random import shuffle

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
  num_train=X.shape[0]
  num_class=W.shape[1]
  for i in range(0,num_train):
    score=np.dot(X[i,:],W)
    score_exp=np.exp(score)
    loss-=np.log(score_exp[y[i]]/np.sum(score_exp))
    for j in range(0,num_class):
      if j==y[i]:
        dW[:,j]+=X[i,:].T*score_exp[j]/np.sum(score_exp)-X[i,:].T
      else:
        dW[:,j]+=X[i,:].T*score_exp[j]/np.sum(score_exp)
  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  loss=loss/num_train+reg*np.sum(W*W)
  dW=dW/num_train+reg*2*W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  score_mat=np.exp(X.dot(W))#N*C
  loss=np.sum(-np.log(score_mat[np.arange(X.shape[0]),y]/np.sum(score_mat,axis=1)))
  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  loss=loss/X.shape[0]+reg*np.sum(W*W)
  constant=score_mat/np.reshape(np.sum(score_mat,axis=1),[X.shape[0],-1])#broadcast
  constant[np.arange(X.shape[0]),y]-=1
  dW=np.dot(X.T,constant)
  dW=dW/X.shape[0]+reg*2*W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

