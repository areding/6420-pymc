 
close all
clear all
 %Random Number Seed
rand('state', 10);
 
 
y = 98;
%------------------------------------------
NN = 50000;
mus = []; taus = [];
mu = 110;  % set the parameters as prior means
tau = 0.01; %
alpha =  0.01;
beta =    0.8;
for i = 1 : NN
  newmu  = sqrt((120/tau)/(120+1/tau)) * randn + ...
         120/(120+1/tau) * y + (1/tau)/(120 + 1/tau)*110;
  par   = beta+1/2 *(y - mu).^2 ;
  newtau = gamrnd(alpha + 1/2, 1/par); %par is rate
  mus = [mus newmu];
  taus = [taus newtau];
  mu=newmu;
  tau=newtau;
end
burn=1000;
mean(mus(burn:end))
mean(taus(burn:end))
mean( 1./taus(burn:end))


figure(1)
subplot(211)
 hist(mus(burn:end), 60)
 xlabel('mu')
 subplot(212)
 hist(taus(burn:end), 60)
 xlabel('tau')
 
 figure(2)
 plot(mus(burn:end), taus(burn:end),'o')