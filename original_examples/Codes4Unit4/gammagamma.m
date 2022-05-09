% gammagamma.m
close all
figure(1)
f=@(x,a,b)   1/gamma(a) * x.^(a-1) .* b.^a .* exp(- b * x)
%f=@(x,a,b)   gampdf(x, a,  1/b);
xx=0.01:0.001:0.6 ;
plot(xx, f(xx, 4, 29),'k-','linewidth',2)
hold on
plot(xx, 0.857*ones(size(xx)),'r-')
plot(0.0246, f(0.0246, 4, 29), 'o')
plot(0.0246, 0, 'ro')
plot(0.2741, f(0.2741, 4, 29), 'o')
plot(0.2741, 0, 'ro')
plot([0.0246  0.2741],[0  0], 'r-','linewidth',8)
hold off
%%
format long
 k=0.857368863848;
a=4; b=29;
ff=@(x) 1/gamma(4) * x.^3 .* 29.^4 .* exp(- 29 * x) - k
a1=fzero(ff, 0.05)  %0.0246
a2=fzero( ff, 0.4)   %0.2741
gamcdf(a2, 4, 1/29) - gamcdf(a1, 4, 1/29) %0.95
format short
lengthhpd = a2 - a1  %0.24951
%%
% Equi-tailed CS

[gaminv(0.025, 4, 1/29)  gaminv(0.975, 4, 1/29)]
% 0.0376    0.3023
lengtheqt = gaminv(0.975, 4, 1/29) - gaminv(0.025, 4, 1/29) %0.26474

figure(2)
plot(xx, f(xx, 4, 29),'k-','linewidth',2)
hold on
plot(0.037582, f(0.037582, 4, 29), 'o')
plot(0.037582, 0, 'ro')
plot(0.30232, f(0.30232, 4, 29), 'o')
plot(0.30232, 0, 'ro')
plot([0.037582  0.30232],[0  0], 'r-','linewidth',8)
plot([0.037582  0.30232],[f(0.037582,4,29)  f(0.30232,4,29)], ...
         'k-','linewidth',1)
hold off
