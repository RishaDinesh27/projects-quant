from statsmodels.tsa.vector_ar.vecm import coint_johansen


def run_johansen(close_prices, det_order=0, k_ar_diff=1):

    result = coint_johansen(close_prices, det_order = det_order, k_ar_diff = k_ar_diff)
    return result

