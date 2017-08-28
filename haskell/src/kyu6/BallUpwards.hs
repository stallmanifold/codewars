module Codewars.G964.Ball where

g_MPerSSquared :: Double
g_MPerSSquared = 9.81

-- Calculate in SI units first.
maxBallSeconds :: Int -> Double
maxBallSeconds v0_KmPerH = 
    let v0_MPerS = fromIntegral v0_KmPerH * 1000.0 / 3600.0
    in v0_MPerS / g_MPerSSquared

maxBall :: Int -> Int
maxBall v0_KmPerH = 
    let timeDeciSeconds = 10.0 * maxBallSeconds v0_KmPerH
    in round timeDeciSeconds
