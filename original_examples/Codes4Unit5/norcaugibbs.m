%norcaugibbs.m
clear all
close all force
randn('state',4);
%
x=2;
sigma2 = 1;
tau2 = 1;
mu = 0;
%
theta = 0;
thetas =[theta];
lambda = 1;
lambdas=[lambda];
burn =1000;
ntotal = 10000 + burn;
tic
for i = 1: ntotal
  theta = (tau2/(tau2 + lambda * sigma2) * x + ...
    lambda * sigma2/(tau2 + lambda * sigma2) * mu) + ...
    sqrt(tau2 * sigma2/(tau2 + lambda *sigma2)) * randn;
  lambda =  exprnd( 1/((tau2 + (theta - mu)^2)/(2*tau2)));
thetas =[thetas theta];
lambdas =[lambdas lambda];
end
toc
%
 mean(thetas(burn+1:end))
 hist(thetas(burn+1:end), 40)