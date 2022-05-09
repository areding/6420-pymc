function [Y] = randMVN(n, mu, sigma) 
% Simulation of multivariate normal
% Usage
%   [Y] = rand_MVN(n, mu, sigma)
% Input
%   n - number of observations to generate
%   mu - dx1 mean column vector
%   sigma - dxd covariance matrix
% Output
%   Y - an nxd matrix of row vectors with mean mu and covariance sigma
%       if mu is a matrix, a matrix of the same size will be returned 
%       with row Y(i,:) having mean mu(i,:).
% Example
%   randMVN(2,[0 0]',[1 0; 0 1])
%   ans =
%    -0.7345    0.3719
%    -0.1882    0.0322
% Brani 10/20/02
 
Ch = chol(sigma)';
X = randn(n,length(mu));
Y = X*Ch' + ones(n,1)*mu' ;