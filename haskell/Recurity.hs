maximum' :: (Ord a) => [a] -> a
maximum' [] = error "Error, the list could not be empty"
maximum' [x] = x
maximum' (x:xs) 
    |  x > tmp = x
    | otherwise = tmp
    where tmp = maximum' xs


replicate' :: (Integral a) => a -> a -> a
replicate' a b 
    | a <= 0 = []
    | otherwise = b : replicate' (a-1) b


take' :: (Integral a, Ord b) => a -> [b] -> [b]
take' a [] = []
take' a _  = 
    | a <= 0 = []
take' n (x:xs) = x : take' (n-1) xs

reverse' :: [x] -> [x]
reverse' [] = []
reverse' x:xs = reverse' xs ++ [x]

zip' :: [a] -> [b] -> [(a,b)]
zip' [] _ = []
zip' _ [] = []
zip' (ax:axs) (bx:bxs) = ax:bx:() : zip' axs bxs

elem' 
    

