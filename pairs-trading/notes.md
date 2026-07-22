# Correlation vs. Cointegration

Correlation is not enough to tell you if two stocks are co-integrated,
because two stocks could have high correlation just by chance. For
example, if both are trending up independently. This is the spurious
regression problem.

Unlike correlation, co-integration means the spread between the two stocks
bounces around a mean with no trend. If a pair is only correlated but not
co-integrated, the spread can still trend instead of reverting. True
co-integration means the spread shows mean reversion and lacks wandering or trends.

## ADF and the Generated-Regressor Bias

Engle-Granger requires picking an independent (x) and dependent (y)
variable, making it an asymmetric test. You regress series 1 on series 2
to get alpha, beta, and residuals (the spread), then run ADF on those
residuals to test for stationarity.

However, since the residuals come from an estimated regression rather
than raw observed data, standard ADF critical values aren't actually
correct for this case. They're built for testing raw series, not
regression-generated residuals. Using the standard critical values anyway
makes the test too lenient, which can make a pair look co-integrated
(p < 0.05) when it actually isn't. The corrected `coint()` test and the
Johansen test both account for this and are more reliable.

## Half Life Derivation

Starting equation:
dS(t) = θ(μ − S(t))dt + σ dW(t)

For the expected path, we drop the noise term (σ dW(t)) since it averages to zero over time, leaving:
dS(t)/dt = θ(μ − S(t))

Substitution

Let x(t) = S(t) − μ, so dx(t)/dt = dS(t)/dt (μ is constant).

dx/dt = −θx

dx/x = −θdt

After Integration:

ln x = −θt + c

x = e^−θt * e^c (notated as x(initial))

x = e^−θt * x(initial)

Solving for Half Life:

0.5 * x(initial) = x(initial) * e^−θt

0.5 = e^−θt

ln(0.5) = −θt

-ln(0.5)/θ = t

ln(2)/θ = t
