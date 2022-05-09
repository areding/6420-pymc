%    A small company improved a product and
% wants to infer about the proportion of 
% potential customers who will buy the product
% if the new product is preferred to the old one.
%    The company is certain that this proportion will
% exceed 0.5, i.e. and uses uniform priorn [0.5, 1].
%    Out of 20 customers surweyed, 12 prefer the new product.
% Approximate the posterior for p.
clear all
close all force
%-----------------figure defaults
lw = 2;  
set(0, 'DefaultAxesFontSize', 15);
fs = 14;
msize = 5;
randn('seed',3)
%--------------------------------
nn = 40000; %     nn=number of metropolis iterations
s=10; %     s = std of normal proposal density
%s=0.1
burn=2000; %     burn = burnin amount 
%---------------------------------------------
ps=[];
thetas=[]; %transformed p's
old = 0; % start, theta_0
for i = 1:nn
    prop = old + s*randn(1,1); %proposal from N(theta_old, s^2)
    u = rand(1,1);
    ep=exp(prop); eo=exp(old);
    post_p=((1/2 + ep)^12 * ep)/((1+ep)^22);
    post_o=((1/2 + eo)^12 * eo)/((1+eo)^22);
    new = old;
    if u <= min(post_p/post_o, 1) 
        new = prop; %accept proposal as 'new'
        old = new;  % and set 'old' to be the 'new'
        % for the next iteration;
    end
        thetas = [thetas, new]; %collect all theta's
        ps=[ps, (1/2+exp(new))/(1+exp(new))]; %back-transformation to p's.
    end  
    figure(1)
    subplot(2,1,1)
    hist(thetas(1+burn:nn),50)
    subplot(2,1,2)
     hist(ps(1+burn:nn),50)
       %print -depsc 'C:\Brani\Courses\Bayes\Handouts\Working10\Figs\albert21.eps'
    %----------------------------------------------------------------------
    figure(2)
    plot( (nn-500:nn) , thetas(nn-500:nn),'b-')
      %print -depsc 'C:\Brani\Courses\Bayes\Handouts\Working10\Figs\albert22.eps'