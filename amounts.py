def get_tok_amts(liquidity, sqrt_price_x96, lo_tick, hi_tick, token0_decimals, token1_decimals):
    """
    Calculate the amount of each token that could be withdrawn from
    a Uniswap V3 liquidity position.
    """
    q96 = 2 ** 96
    
    def _get_tick_at_sqrt_ratio():
        return np.floor(np.log((sqrt_price_x96 / q96) ** 2)/ np.log(1.0001))
    
    sqrt_ratio_a = (1.0001 ** lo_tick) ** 0.5
    sqrt_ratio_b = (1.0001 ** hi_tick) ** 0.5
    current_tick = _get_tick_at_sqrt_ratio()
    sqrt_price = sqrt_price_x96 / q96
    
    amount0wei = 0
    amount1wei = 0
    if current_tick <= lo_tick:
        amount0wei = np.floor(liquidity * ((sqrt_ratio_b - sqrt_ratio_a) / (sqrt_ratio_a * sqrt_ratio_b)))
    if current_tick > hi_tick:
        amount1wei = np.floor(liquidity * (sqrt_ratio_b - sqrt_ratio_a))
    if (current_tick >= lo_tick) and (current_tick < hi_tick):
        amount0wei = np.floor(liquidity * ((sqrt_ratio_b - sqrt_price) / (sqrt_price * sqrt_ratio_b)))
        amount1wei = np.floor(liquidity * (sqrt_price - sqrt_ratio_a))

    amount0Human = amount0wei / (10 ** token0_decimals)
    amount1Human = amount1wei / (10 ** token1_decimals)

    return dict(
        amt0=amount0Human, amt1=amount1Human,
    )
