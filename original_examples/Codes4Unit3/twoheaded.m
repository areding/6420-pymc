% "Two-headed coin"
%
% Out of N coins one is with two heads. A coin is selected
% at random and flipped k times and k times heads appeared.
% What is the probability that the coin with two heads was
% selected?
% 
%
clear all
close all


  disp('Two Headed Coin')
  lw = 3; 
  set(0, 'DefaultAxesFontSize', 16);
  fs = 15;
  msize = 10;
  

N=1000000; %number of coins N-1 fair, 1 two-headed
%
pro = @(k, N) 2.^k./(2.^k + N - 1);
 p=[];  %keep posterior probs here
for k=1:40
     p = [p  pro(k, N)];
     %or simply: p = [p  2^k/(2^k + N - 1)];  
end
figure(1)
plot((1:40), p, 'linewidth', lw)
hold on
plot((1:40), p, 'o', 'markersize', msize,...
                'MarkerEdgeColor','k',...
                'MarkerFaceColor','g')

plot(16, p(16), 'ro', 'markersize', msize,...
                'MarkerEdgeColor','k',...
                'MarkerFaceColor','r')
   
plot(24, p(24), 'ro', 'markersize', msize,...
                'MarkerEdgeColor','k',...
                'MarkerFaceColor','r')   
plot([16,16],[0,1],'r:')
plot([24,24],[0,1],'r:')
ylabel('Posterior probability of a 2H coin')
xlabel('Number of flips all resulting in H')
%print -depsc 'C:\STAT\Probs\Probseps\twoheaded.eps'

% figure(2)
% op =  p./(1-p);
% semilogy((1:40),op, 'linewidth', lw)
% hold on
% semilogy((1:40), op, 'o', 'markersize', msize)
% ylabel(' Posterior Odds')
% xlabel('Number of flips all resulting in H')
%print -depsc 'C:\Springer\Probs\Probseps\twoheaded.eps'
k=[4  16 24 40 70];
format long
pro(k, N)
%   0.000015999760004   0.061505253229598   0.943748275531347   
%   0.999999090507035   0.999999999999999
pro(21,N)-pro(19, N)
%   0.333166719521469
format short
