% Modified from C. Robert Bayesian Choice
% Springer, 2nd edition Page 305

% Weibull lifetimes
% f(t|alpha, eta) = alpha eta t^(alpha-1) exp(- eta t^alpha)
% Prior on (alpha, eta) is proportional to 
%    exp(-alpha) eta^(beta-1) exp(-xi eta)
% As proposal conditional density for alpha' and eta' use 
% the product of two exponential densities with means alpha and eta.
close all force
clear all
%
data = [0.200 0.100 0.250];%

n=length(data);

alpha = 2; %initial values
eta =   2;
alphas = [alpha]; etas = [eta];


%hyperparameters
beta=2; xi = 2;

tic
 for i = 1:50000
alpha_prop = - alpha * log(rand);
eta_prop   = -   eta * log(rand);
%--------------------------------------------------------------------------
    prod1 = prod(data);
    prod2 = prod( exp( eta * data.^alpha - eta_prop * data.^alpha_prop));
%--------------------------------------------------------------------------
rr = (eta_prop/eta)^(beta-1) * exp(alpha - alpha_prop - xi * (eta_prop - eta)) * ...
      exp(- alpha/alpha_prop - eta/eta_prop + alpha_prop/alpha + eta_prop/eta)   * ...
      prod1.^(alpha_prop - alpha) * prod2 * ((alpha_prop * eta_prop)/(alpha * eta))^(n-1);
%--------------------------------------------------------------------------
rho = min( rr ,1);
   if (rand < rho)
       alpha = alpha_prop; eta =  eta_prop;
   end
alphas =  [alphas alpha];
etas   =  [etas eta];
end
toc
%Burn in 500
 alphas = alphas(500:end);
 etas = etas(500:end);
figure(1)
 hist(alphas, 50)
 xlabel('alpha')
figure(2)
 hist(etas, 50)
 xlabel('eta')
alpha_B = mean(alphas)
eta_B = mean(etas)
var_alphaB = var(alphas)
var_etaB = var(etas)
 