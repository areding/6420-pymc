%
% Laplace's Method
% X|theta ~ Ga(r,theta), theta ~ Ga(alpha,beta) 
close all
xx = 0:0.01:16;
r=20; alpha = 5; beta = 1; 
%observed
x=2;
y1 = gampdf(xx, r + alpha, 1/(beta + x));
y2 = normpdf(xx, (r-1+alpha)/(beta + x), sqrt(r - 1 + alpha)/(beta + x));
%
figure(1)
plot(xx, y1, 'r-','linewidth',2)
hold on
plot(xx, y2, 'b-','linewidth',2)
legend('exact posterior','Laplace''s approximation')
%% 
% 95% Credible Set
% exact
 [gaminv(0.025,   r + alpha, 1/(beta + x)) gaminv(0.975,   r + alpha, 1/(beta + x))]
%    5.3929   11.9034
%
% approximate (Laplace's method)
[norminv(0.025, (r-1+alpha)/(beta + x), sqrt(r - 1 + alpha)/(beta + x)), ...
 norminv(0.975, (r-1+alpha)/(beta + x), sqrt(r - 1 + alpha)/(beta + x))]
%
%   4.7994   11.2006
%
% What exact posterior coverage this approximative CS has?

gamcdf(11.2006,  r + alpha, 1/(beta + x)) - gamcdf( 4.7994, r + alpha, 1/(beta + x))   
%  0.9404
%%
% integral of g
% int_R+   x^(u-1) exp(-v x) dx = gamma(u)/v^u
%exact
gamma(r + alpha) / (beta + x)^(r + alpha)  %  7.3228e+11

% approximation by Laplace's method
sqrt(2 * pi) * (r+alpha-1)^(r + alpha -1/2) /((beta + x)^(r +alpha)) * exp(-(r+alpha -1))
 %  7.2974e+11



