%
clear all
close all
%--------------------------------
  lw = 2.5; 
  set(0, 'DefaultAxesFontSize', 16);
  fs = 16;
  msize = 10;
%----------------------------------------
disp('Gibbs for Mixture')
rand('seed', 1)   %initialize
randn('seed',1)   %random number generators
% simulate data---------------------------
n=400; us = rand(1,n);
for i=1:n
    if us(i) < 0.1
          x(i) = 2 * randn +  1; %0.1 of N(1,2^2)
    elseif us(i) > 0.8
          x(i) = 2 * randn + 20; %0.2 of N(20,2^2)
    else  x(i) = 2 * randn +  9; %0.7 of N(9,2^2)
    end
end
x = sort(x);
%fixed (hyper)parameters
k=3; 
tau =     12; 
alpha =   5;
delta =   30;
gamma =   10;
iterations = 5000;
burn = 1000;
%--------------------------
% initial parameters
sig2 = 5;
s0=repeat((1:k)', ceil(n/k));
s1 = s0'; s2 = s1(:); s = s2(1:n); %s is latent variable
w  = repeat(1/k, k);  %equal weight
mu = repeat(10,k);
%
%---------for iter = 1:iterations
mus=[]; sig2s=[]; ws=[];
  h=waitbar(0,'Simulation in progress');
for iter=1: burn + iterations
for i=1:n
   for j=1:k
    sij(i,j)= (s(i)==j);
   end
end
nj=sum(sij);
w = (rand_dirichlet(alpha + nj, 1))';
%---------------------------
for j = 1:k
    sj(j) = sum(x(s==j));
end
mu = sqrt( 1./( nj/sig2 + 1/tau^2)) .* randn(1,k) + (tau^2.*sj)./(nj*tau^2+sig2);
%---------------------------
for j = 1:k
    sm2j(j) = sum ( (x(s==j) - mu(j)).^2 );
end
sig2 = 1./rand_gamma( gamma + n/2,   delta + 1/2 * sum(sm2j), 1, 1);
%-------------------------------------------------------------

pr = zeros(n,k);
for i = 1:n
    for j=1:k
        pr(i,j) = w(j)*exp( - (x(i) - mu(j))^2 /(2 * sig2));
    end
end
tot= repeat((sum(pr'))',3);
pr=pr./tot;
for i=1:n
 [aa,bb]=rand_multinomial(1,pr(i,:));
  s(i) = find(bb==1);
end
%--------------------------------------------------------------
mus=[mus; mu];
sig2s=[sig2s, sig2];
ws = [ws; w];
  waitbar(iter/(burn+iterations))
end
close(h)
muss=mus(burn+1:end, :);
mmu= mean(muss)
sig2ss = sig2s(burn+1: end);
msig2= mean(sig2ss)
wss = ws(burn+1:end, :);
mw = mean(wss)

figure(1)
subplot(3,1,1)
hist(muss(:,1),50)
subplot(3,1,2)
hist(muss(:,2),50)
subplot(3,1,3)
hist(muss(:,3),50)
%print -depsc 'C:\Brani\Courses\Bayes\Handouts\Working12\Figs\MixGibbs1.eps'

figure(2)
hist(sig2ss, 50)
%print -depsc 'C:\Brani\Courses\Bayes\Handouts\Working12\Figs\MixGibbs2.eps'
figure(3)
subplot(3,1,1)
hist(wss(:,1),50)
subplot(3,1,2)
hist(wss(:,2),50)
subplot(3,1,3)
hist(wss(:,3),50)
%print -depsc 'C:\Brani\Courses\Bayes\Handouts\Working12\Figs\MixGibbs3.eps'

% figure(4)
% [fr, ce]= hist(x,30);
% dist=ce(2)-ce(1);
% cee=linspace(-5,25,300);
% hig = fr./(dist*sum(fr));
% bar(ce,hig);
% hold on
% plot(cee,     mw(1)*1/sqrt(2 * pi * msig2)*exp(-1/2*(cee - mmu(1)).^2),'r-','linewidth',lw)
% plot(cee,     mw(2)*1/sqrt(2 * pi * msig2)*exp(-1/2*(cee - mmu(2)).^2),'r-','linewidth',lw)
% plot(cee,     mw(3)*1/sqrt(2 * pi * msig2)*exp(-1/2*(cee - mmu(3)).^2),'r-','linewidth',lw)

figure(4)
histo(x,30,0,1)
hold on
cee=linspace(-5,25,300);
est=mw(1).*1./sqrt(2 * pi * msig2).*exp(-1/(2*msig2) * (cee - mmu(1)).^2)+...
    mw(2).*1./sqrt(2 * pi * msig2).*exp(-1/(2*msig2) * (cee - mmu(2)).^2)+...
    mw(3).*1./sqrt(2 * pi * msig2).*exp(-1/(2*msig2) * (cee - mmu(3)).^2);
plot(cee, est,'b-')
 theo = 0.1 * 1./sqrt(2 * pi * 4).*exp(-1/(2*4) * (cee - 1).^2)+...
        0.2 * 1./sqrt(2 * pi * 4).*exp(-1/(2*4) * (cee - 20).^2)+...
        0.7 * 1./sqrt(2 * pi * 4).*exp(-1/(2*4) * (cee - 9).^2);
plot(cee, theo,'r--')
%print -depsc 'C:\Brani\Courses\Bayes\Handouts\Working12\Figs\MixGibbs4.eps'
