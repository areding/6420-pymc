%COIN
close all
p = 0:0.01:1;
P10T = @(p) 11 * (1-p).^10; % 11 to normalize to a density
figure(1)
plot(p, P10T(p), '-', 'LineWidth',2)
% 
quad(P10T, 0, 1)
%
%for the mean
pP10T = @(p)  11 * p .* (1-p).^10;
quad(pP10T, 0, 1) %0.083333 (1/12)
hold on
scatter([0 0],[0 11],200,'r','filled')
scatter([1/12 1/12],[0  P10T(1/12)],200,'g','filled')
% for the median
quad(P10T, 0, 0.061069)  %0.50000
scatter([0.061069 0.061069],[0  P10T(0.061069)],...
        200,'b','filled')
    title ('Coin');
xlabel ('p');
ylabel ('f(p)');
  text (0.05, 11, '\fontsize{14} mode');
legend ('\fontsize{12} Likelihood','\fontsize{12} MAP',...
    '\fontsize{12} Mean','\fontsize{12} Median');    