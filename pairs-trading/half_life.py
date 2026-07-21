
import pandas as pd
import statsmodels.api as sm
import numpy as np

#ΔS(t) = θμ − θS(t−1) + error
#ΔS(t) = y
#S(t−1) = x
#−θ beta or slope
#θμ intercept or alpha

def estimate_half_life(residuals):

    lagged_res = residuals.shift(1)
    diff_res = residuals.diff()
    df = pd.DataFrame({"Lagged_Residuals": lagged_res, "Differenced_Residuals": diff_res}).dropna() # this will line up and handle any missing mismathced columns by aligned by date and then removing nan 


    lagged_res_const = sm.add_constant(df["Lagged_Residuals"])
    model = sm.OLS(df["Differenced_Residuals"],lagged_res_const).fit()

    alpha = model.params['const']
    beta = model.params['Lagged_Residuals']

    theta = -beta
    return np.log(2) / theta