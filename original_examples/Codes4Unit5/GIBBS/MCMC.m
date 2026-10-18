 close all
 clear all
  randn("state",1)
  randg("state",1)
  n=100;
  y = 2 * randn(1,n) + 1;
%------------------------------------------
NN = 10000;
mus = []; taus = [];
sumdata = sum(y);
%hyperparameters
mu0=0.5; tau0 = 1/100;
a= 1/2; b= 2;
% start, initial values
mu = 0.5;   tau = 0.5; %
for i = 1 : NN
  newmu  = sqrt(1/(tau0+n*tau)) * randn + (tau * sumdata+tau0*mu0)/(tau0+n*tau);
  %par   = b+1/2 * sum ( (y - mu).^2);
  par   = b+1/2 * sum ( (y - newmu).^2);
  newtau = gamrnd(a + n/2, 1/par); %par is rate
  mus = [mus newmu];
  taus = [taus newtau];
  mu=newmu;
  tau=newtau;
end
 
burn =200;
mus = mus(burn+1:end);
taus=taus(burn+1:end);

mean(mus)
mean(taus)
figure(1)
subplot(211)
hist(mus, 40)
subplot(212)
hist(taus, 40)

