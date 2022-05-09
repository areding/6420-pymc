% Dorn (1954): American Statistician, 8, 7-13.
% 86 lung cancer patients; 86 controls//smokers, nonsmokers
%            Cancer Control
%   ---------------------
%   Smokers      83   72
%   ---------------------
%   Nonmokers     3   14
%------------------------
% 
% Let p_L and p_C describe proportion of smokers
% in population of lung canncer
% patients and in the control.
% We are interested in making inference about p_L and p_C
% and, in particular, on p_L-p_C.


clear all
close all
%-----------------figure defaults
lw = 2;  
set(0, 'DefaultAxesFontSize', 18);
fs = 14;
msize = 5;
randn('seed',3)
%---------
nn = 20000; %     nn=number of metropolis iterations
burn=2000; %     burn = burnin amount 
%---------------------------------------------
% lokelihood propto p_L^83 * (1-p_L)^3 * p_C^72 * (1-p_C)^14,
% prior p_L^(-1) * (1-p_L)^(-1) * p_C^(-1) * (1-p_C)^(-1),
% alpha=log(p_L/(1-p_L) * (1-p_C)/p_C);
% eta = log(p_L/(1-p_L) * p_C/(1-p_C));
% --------------------------------------------
% If ep=exp((eta+alpha)/2); em=exp((eta-alpha)/2);
% then the posterior is proportional to
% ep^83/(1+ep)^86 * em^72/(1+em)^86 *  (1-ep)^2/ep * (1+em)^2/em   *
% ep/(1-ep)^2 * em/(1+em)^2 =  ep^83/(1+ep)^86 * em^72/(1+em)^86 
% (as lik*prior*jacobian)
rand('seed',1); randn('seed',1)
alphas=[]; etas=[]; pLs=[]; pCs=[];
alpha_old = 0;
eta_old = 0;
Sigma=[1 0.5; 0.5 1];
for i = 1:nn
    prop = randMVN(1, [eta_old, alpha_old]', Sigma)'; %proposal from 
    eta_prop = prop(1);
    alpha_prop = prop(2);
    u = rand(1,1);
    epp=exp((eta_prop+alpha_prop)/2); emp=exp((eta_prop-alpha_prop)/2);
    epo=exp((eta_old+alpha_old)/2); emo=exp((eta_old-alpha_old)/2);
    post_p = (epp)^83/(1+epp)^86 * (emp)^72/(1+emp)^86; 
    post_o = (epo)^83/(1+epo)^86 * (emo)^72/(1+emo)^86; 
    eta_new = eta_old; alpha_new = alpha_old;
    if u <= min(post_p/post_o, 1) 
        eta_new = eta_prop; alpha_new = alpha_prop;
        eta_old = eta_prop; alpha_old = alpha_prop;
    end
    etas=[etas eta_new];
    alphas=[alphas, alpha_new]; %collect all theta's
        pLs=[pLs, exp( (eta_new+alpha_new)/2)/(1+exp( (eta_new+alpha_new)/2))];
        pCs=[pCs, exp( (eta_new-alpha_new)/2)/(1+exp( (eta_new-alpha_new)/2))];   
    end  
figure(1)
plot(etas(burn+1:nn), alphas(burn+1:nn),'.')
xlabel('\eta'); ylabel('\alpha')
  %print -depsc 'C:\Brani\Courses\Bayes\Handouts\Working10\Figs\albert31.eps'
figure(2)
plot(pLs(burn+1:nn),pCs(burn+1:nn),'.')
xlabel('p_L'); ylabel('p_C')
  %print -depsc 'C:\Brani\Courses\Bayes\Handouts\Working10\Figs\albert32.eps'
figure(3)
hist(pLs(burn+1:nn)-pCs(burn+1:nn),50)
title('Histogram of differences: p_L - p_C')
  %print -depsc 'C:\Brani\Courses\Bayes\Handouts\Working10\Figs\albert33.eps'