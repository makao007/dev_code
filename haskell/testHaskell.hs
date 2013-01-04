doubleMe x=x+x
doubleUs a b = a+a+b+b
doubleSmallNumber x = if x > 100 
    then x
    else x+x
doubleSmallNumber' x = (if x > 100 then x else x+x) + 1


lucky :: (Integral a) => a -> String
lucky 7 = "Lucky Number seven"
lucky x = "Sorry, you're out of luck, pal!"
