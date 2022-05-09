
%
% 
%
close all force
clear all

rand('state', 10);
randn('state', 20);
ii = 0;
thetas=[];
taus=[];
theta  = 100;  %set initial as theta=100
tau = 0.001;  %set initial  
while (length(thetas) < 35000)
  ii = ii+1;
  % Generate a candidate draw.
  thetaprop = theta  +  75*tan(pi*rand(1,1)-pi/2);
 %tauprop =  1/sqrt(tau) * (- log(rand(1,1)));
 % tauprop =  max(0.0001, tau + 0.001* randn);
  tauprop =  abs(tau + 0.0007* randn);
  %  
  y = 98;
  num= sqrt(tauprop) * exp(-tauprop/2 *(y - thetaprop)^2 )*  ...
            exp(- 1/(2* 120) *(thetaprop-110)^2) * ...
            exp(-0.01 * tau);
  denom= sqrt(tau) * exp(-tau/2*(y - theta)^2 )*  ...
       exp(- 1/(2 * 120)  *(theta-110)^2) * ...
       exp(-0.01* tauprop);
  f = min(1, num/denom);
  %Make a randomized decision to accept the proposal
  if (rand(1,1) <= f)
     theta = thetaprop;
     tau= tauprop;
  end 
thetas=[thetas theta];
taus = [taus  tau];
end 
figure(1)
subplot(211)
plot(thetas,'-.')
subplot(212)
plot(taus,'-.')
%
burn=15000;
thetass = thetas(burn:end);
tauss = taus(burn:end);
figure(2)
  subplot(121)
  hist(thetass, 20)
  xlabel('\theta')
  subplot(122)
  hist(tauss, 20)
  xlabel('\tau')

  thetahat = mean(thetass)
  stdtheta = std(thetass)
  [prctile(thetass, 2.5) prctile(thetass, 50) prctile(thetass, 97.5)]
  
  tauhat = mean(tauss)
  stdtau = std(tauss)
  sigmahat1 = mean(1./tauss)
  sigmahat2 = 1/tauhat