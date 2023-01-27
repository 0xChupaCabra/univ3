function getAmountsForLiquidity(

        uint160 sqrtRatioX96,

        uint160 sqrtRatioAX96,

        uint160 sqrtRatioBX96,

        uint128 liquidity

    ) internal pure returns (uint256 amount0, uint256 amount1) {

        if (sqrtRatioAX96 > sqrtRatioBX96) (sqrtRatioAX96, sqrtRatioBX96) = (sqrtRatioBX96, sqrtRatioAX96);

        if (sqrtRatioX96 <= sqrtRatioAX96) {

            amount0 = getAmount0ForLiquidity(sqrtRatioAX96, sqrtRatioBX96, liquidity);

        } else if (sqrtRatioX96 < sqrtRatioBX96) {

            amount0 = getAmount0ForLiquidity(sqrtRatioX96, sqrtRatioBX96, liquidity);

            amount1 = getAmount1ForLiquidity(sqrtRatioAX96, sqrtRatioX96, liquidity);

        } else {

            amount1 = getAmount1ForLiquidity(sqrtRatioAX96, sqrtRatioBX96, liquidity);

        }

    }
    
//https://github.com/Uniswap/v3-periphery/blob/main/contracts/libraries/LiquidityAmounts.sol
