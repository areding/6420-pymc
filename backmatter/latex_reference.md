# Latex Reference

I'm going to experiment with this auto-generated Latex reference based on all the macros used in this Jupyter Book. You can see the code used to generate it at [this Github repo](https://github.com/areding/latexref). To use any of the macros below, just put a backslash (```\```) in front of them. One other useful thing I want to add is the align environment for aligning equations. Here's an example:

```latex
\begin{align*}
	y_i | \theta, X &\sim \text{Poisson}(\lambda_i) \\
	\lambda_i &= g^{-1}(\eta_i) \\
	\eta_i &= \beta_0 + \sum_{j=1}^p \beta_j x_{ij} \\
	\beta &\sim \mathcal{N}\left(0, \sigma^2\right)
\end{align*}					
```

This displays:

$$
\begin{align*}
y_i | \theta, X &\sim \text{Poisson}(\lambda_i) \\
\lambda_i &= g^{-1}(\eta_i) \\
\eta_i &= \beta_0 + \sum_{j=1}^p \beta_j x_{ij} \\
\beta &\sim \mathcal{N}\left(0, \sigma^2\right)
\end{align*}
$$

Once you've opened align, you just put an ```&``` symbol before the character you want to align on. Then end each line with two slashes: ```\\```.


The remainder of this document was automatically created by OpenAI's GPT-4 on July 15, 2023. 

## Greek Letters

- alpha, $\alpha$, represents the lowercase Greek letter alpha. Example: $\alpha = 0.05$.
- beta, $\beta$, represents the lowercase Greek letter beta. Example: $\beta = 0.5$.
- gamma, $\gamma$, represents the lowercase Greek letter gamma. Example: $\gamma = 0.7$.
- delta, $\delta$, represents the lowercase Greek letter delta. Example: $\delta = 0.1$.
- theta, $\theta$, represents the lowercase Greek letter theta. Example: $\theta = 1.2$.
- lambda, $\lambda$, represents the lowercase Greek letter lambda. Example: $\lambda = 2.3$.
- xi, $\xi$, represents the lowercase Greek letter xi. Example: $\xi = 3.4$.
- pi, $\pi$, represents the lowercase Greek letter pi. Example: $\pi \approx 3.14159$.
- sigma, $\sigma$, represents the lowercase Greek letter sigma. Example: $\sigma = 0.25$.
- tau, $\tau$, represents the lowercase Greek letter tau. Example: $\tau = 0.5$.
- phi, $\phi$, represents the lowercase Greek letter phi. Example: $\phi = 1.61803$.
- Delta, $\Delta$, represents the uppercase Greek letter Delta. Example: $\Delta = 5$.
- Gamma, $\Gamma$, represents the uppercase Greek letter Gamma. Example: $\Gamma(1) = 1$.
- Sigma, $\Sigma$, represents the uppercase Greek letter Sigma. Example: $\Sigma x_i = \sum_{i=1}^{n} x_i$.
- Phi, $\Phi$, represents the uppercase Greek letter Phi. Example: $\Phi(x)$ is the cumulative distribution function of a standard normal distribution.
- Nu, $\nu$, represents the lowercase Greek letter nu. Example: $\nu$ is often used to denote degrees of freedom in statistics.

## Operators

- arg, $\arg$, represents the argument of a complex number. Example: $\arg(z)$.
- binom, $\binom{n}{k}$, represents the binomial coefficient. Example: $\binom{5}{2} = 10$.
- sqrt, $\sqrt{x}$, represents the square root of x. Example: $\sqrt{4} = 2$.
- frac, $\frac{a}{b}$, represents the fraction a divided by b. Example: $\frac{1}{2} = 0.5$.
- max, $\max$, represents the maximum value. Example: $\max\{1, 2, 3\} = 3$.
- int, $\int$, represents the integral symbol. Example: $\int x dx = \frac{1}{2}x^2$.
- prod, $\prod$, represents the product symbol. Example: $\prod_{i=1}^{n} x_i$.
- sum, $\sum$, represents the summation symbol. Example: $\sum_{i=1}^{n} x_i$.

## Symbols

- infty, $\infty$, represents the symbol for infinity. Example: $\lim_{x\to\infty} f(x)$.
- ldots, $\ldots$, represents the symbol for ellipsis. Example: $1, 2, 3, \ldots, n$.
- approx, $\approx$, represents the symbol for approximately equal to. Example: $\pi \approx 3.14$.
- sim, $\sim$, represents the symbol for distributed as. Example: $X \sim N(\mu, \sigma^2)$.
- propto, $\propto$, represents the symbol for proportional to. Example: $y \propto x$.
- mid, $\mid$, represents the symbol for such that. Example: $\{x \mid x > 0\}$.
- neq, $\neq$, represents the symbol for not equal to. Example: $1 \neq 2$.
- in, $\in$, represents the symbol for element of. Example: $x \in \mathbb{R}$.
- mapsto, $\mapsto$, represents the symbol for mapping. Example: $f: x \mapsto x^2$.

## Formatting

- text, \text{your text here}, allows you to insert normal text into math mode. Example: $x = 2$ \text{ and } $y = 3$.
- mathbf, $\mathbf{x}$, makes the letter bold. Example: $\mathbf{x}$ is often used to denote a vector.
- hat, $\hat{x}$, puts a hat over the letter. Example: $\hat{x}$ is often used to denote an estimate.
- bar, $\bar{x}$, puts a bar over the letter. Example: $\bar{x}$ is often used to denote the sample mean.
- mathcal, $\mathcal{A}$, creates a calligraphic letter. Example: $\mathcal{A}$ is often used to denote a set.
- quad, \quad, creates a space in math mode. Example: $a = b \quad \text{and} \quad c = d$.
- left and right, $\left(\frac{a}{b}\right)$, creates scalable delimiters. Example: $\left(\frac{a}{b}\right)$.

## Comparisons

- lt, $<$, represents the less than symbol. Example: $1 < 2$.
- le, $\leq$, represents the less than or equal to symbol. Example: $1 \leq 2$.
- gt, $>$, represents the greater than symbol. Example: $3 > 2$.
- ge, $\geq$, represents the greater than or equal to symbol. Example: $3 \geq 2$.

## Arrows

- rightarrow, $\rightarrow$, represents the rightward arrow. Example: $x \rightarrow y$.
- mapsto, $\mapsto$, represents the mapsto arrow. Example: $f: x \mapsto x^2$.
- nabl, $\nabla$, represents the del or nabla symbol, used in vector calculus. Example: $\nabla f$.

## Functions

- log, $\log$, represents the logarithm function. Example: $\log_{2}(8) = 3$.
- arctan, $\arctan$, represents the inverse tangent function. Example: $\arctan(1) = \frac{\pi}{4}$.

## Others

- times, $\times$, represents the multiplication symbol. Example: $2 \times 3 = 6$.
- cdot, $\cdot$, represents the dot product symbol. Example: $\mathbf{a} \cdot \mathbf{b}$.
- inf, $\inf$, represents the infimum or greatest lower bound of a set. Example: $\inf\{x \mid x > 0\} = 0$.
