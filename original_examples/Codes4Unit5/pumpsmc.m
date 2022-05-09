%pumps MCMC
X=[5 1 5 14 3  19 1 1 4 22];
t = [94.32 15.52 62.88 125.76 ...
    5.24 31.44 1.048 1.048 2.096 10.48];
% data drom Gaver and O'Muircheartaigh, 1987
%
n=10;
c=0.1;
d=1;
%
%Initials
theta = [1 1 1 1 1   1 1 1 1 1];
beta =1;
%
B=50000;
thetas=[]; betas=[];
tic
for i = 1:B
for j=1:n
    theta(j) = gamrnd(X(j)+1, 1./(beta + t(j)) );
end
sumthetas = sum(theta);
  beta =gamrnd(n + c, 1./(sumthetas + d));
  thetas = [thetas; theta];
  betas = [betas; beta];
end
 burn=1000;
 thetasb = thetas(burn+1:end,:);
 betasb = betas(burn+1:end);
 
 thetas_B = mean(thetasb)
 beta_B = mean(betasb)
 
 %std(thetasb)
 %std(betasb)
 
toc

 


% thetas_B =
%     0.0628    0.1189    0.0932    0.1179    0.6074
%     0.6102    0.8718    0.8698    1.4856    1.9504
%     
% beta_B = 1.3368
% 
% Elapsed time is 36.877535 seconds.

% 		mean	sd	MC_error	val2.5pc	median	val97.5pc	start	sample
% 	beta	1.34	0.486	0.002973	0.5896	1.271	2.466	1001	50000
% 	theta[1]	0.06261	0.02552	1.111E-4	0.02334	0.05914	0.1217	1001	50000
% 	theta[2]	0.118	0.08349	3.694E-4	0.01431	0.09888	0.3296	1001	50000
% 	theta[3]	0.09366	0.03829	1.706E-4	0.03439	0.08842	0.1828	1001	50000
% 	theta[4]	0.1178	0.03048	1.472E-4	0.06595	0.115	0.1848	1001	50000
% 	theta[5]	0.6116	0.3097	0.001409	0.1632	0.5589	1.361	1001	50000
% 	theta[6]	0.6104	0.1366	6.453E-4	0.3705	0.6001	0.9058	1001	50000
% 	theta[7]	0.8686	0.6494	0.003059	0.101	0.7124	2.537	1001	50000
% 	theta[8]	0.8692	0.6481	0.003354	0.09784	0.7117	2.513	1001	50000
% 	theta[9]	1.478	0.6897	0.00351	0.4705	1.367	3.128	1001	50000
% 	theta[10]	1.944	0.4133	0.002022	1.223	1.916	2.83	1001	50000
% 
