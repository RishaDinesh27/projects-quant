def compute_zscore(residuals,window):
    return (residuals - residuals.rolling(window).mean())/residuals.rolling(window).std()


def generate_signals(zscore, entry = 2, exit = 0.1):
    current_position = 0
    daily_signals = []

    #zscore series of the zscores per day, gs deviated from ms
    # signal = 1, short the spread (short MS, long GS)
    # signal = -1, long the spread (long MS, short GS)
    # signal = 0, flat

    for  z in zscore:
        if current_position == 0 and z > entry:
            current_position = 1
            daily_signals.append(1)

        elif current_position == 0 and z < -entry:
            current_position = -1
            daily_signals.append(-1)
        elif current_position != 0 and abs(z) <= exit:
            current_position = 0
            daily_signals.append(0)

        else:
            daily_signals.append(current_position)

    return daily_signals

def generate_postions(signal, close_prices, beta, capital,ticker_x, ticker_y):
    shares_x = 0
    shares_y = 0
    shares_x_list = []
    shares_y_list = []

    for i in range(len(signal)):
        price_x = close_prices[ticker_x].iloc[i]
        price_y = close_prices[ticker_y].iloc[i]

        if i == 0:
            shares_x = 0
            shares_y = 0
            shares_x_list.append(shares_x)
            shares_y_list.append(shares_y)
        else:
            if signal[i] == 1 and signal[i-1] != 1:
                n = capital / (price_y + beta * price_x)
                shares_x = n * beta
                shares_y = -n
                shares_x_list.append(shares_x)
                shares_y_list.append(shares_y)
                
            elif signal[i] == -1 and signal[i-1] != -1:
                n = capital / (price_y + beta * price_x)
                shares_x = -n * beta
                shares_y = n
                shares_x_list.append(shares_x)
                shares_y_list.append(shares_y)

            elif signal[i] == 0 and signal[i-1] != 0:
                shares_x = 0
                shares_y = 0
                shares_x_list.append(shares_x)
                shares_y_list.append(shares_y)

            else:
                shares_x_list.append(shares_x)
                shares_y_list.append(shares_y)

    return shares_x_list, shares_y_list