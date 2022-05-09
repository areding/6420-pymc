
% mcmc1
% full conditional distributions available
% 
%  y_i ~ N(mu, 1/tau), i=1,...,n
%  mu  ~ N(0,1);
%  tau ~ Ga(2,1);
%------------------------------------------
% This example implements Simple Example 5.2.1
% from Walter Gilks: Full conditional distributions,
% Chapter 5 in MCMC in Practice, Gilks, Richardson, and
% Spiegelhalter, Chapman & Hall pages 75-76.
% Model: y_i \sim N(\mu, \tau^{-1}), i=1, \dots, n 
%       tau=precision parameter (1/variance)
%        Priors: \mu \sim N(0,1); \tau \sim Gamma(2,1)
%  DATA simulated, n=200 from N(1,4^2).
%
clear all
close all force
%-----------------figure defaults
lw = 2;  
set(0, 'DefaultAxesFontSize', 17);
fs = 14;
msize = 5;
%--------------------------------
 n=30; % sample size
 randn('state', 10);
 y = 4 * randn(1,n) + 1;
%------------------------------------------
nn = 10000;
thetas = [];
taus = [];
suma = sum(y)
theta = 0;  % set the parameters as prior means
tau = 2;
h=waitbar(0,'Simulation in progress');
for i = 1 : nn
   new_theta  = sqrt(1/(1+n*tau)) * randn + (tau * suma)/(1+n*tau);
  %new_theta  = normrnd( (tau * suma)/(1+n*tau),   sqrt(1/(1+n*tau)) );
  par     = 1+ 1/2 * sum ( (y - theta).^2 );
  new_tau =gamrnd(2 + n/2, 1/par);
  thetas = [thetas new_theta];
  taus = [taus new_tau];
  tau=new_tau;
  theta=new_theta;
                     if i/50==fix(i/50)           % Shows wait bar
                        waitbar(i/nn)
                     end
end
 close(h)
figure(1)
subplot(2,1,1)
plot((nn-500:nn), thetas(nn-500:nn))
subplot(2,1,2)
plot((nn-500:nn), taus(nn-500:nn))
%
figure(2)
burnin = 1000;
subplot(2,1,1)
hist(thetas(burnin:nn), 70)
  xlabel('\theta')
subplot(2,1,2)
hist(taus(burnin:nn), 70)
  xlabel('\tau')
%
figure(3)
plot( thetas(burnin:nn), taus(burnin:nn), '.') 
muhat = mean(thetas(burnin:nn))
tauhat = mean(taus(burnin:nn))
%
sigma2hat = mean(1./taus(burnin:nn))
