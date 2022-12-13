#!/usr/bin/env stack
{- stack script
   --verbosity debug
   --resolver lts-13.7
   --package text
 -}

{-# LANGUAGE OverloadedStrings #-}

import qualified Data.Text as T
import Data.List

main :: IO ()
main = do
  content <- readFile "input.txt"
  let groups = T.splitOn "\n\n" (T.pack content)
  let parsed = map (\elf -> map parseToInt (T.splitOn "\n" elf)) groups
  let elves = map (\calories -> sum calories) parsed
  let sorted = reverse $ sort elves

  putStrLn (show $ head sorted)
  putStrLn (show $ sumN 3 sorted)

parseToInt :: T.Text -> Integer
parseToInt "" = 0
parseToInt x = read (T.unpack x) :: Integer

sumN :: Integer -> [Integer] -> Integer
sumN n xs = go 0 xs
  where
  go counter  _ | counter == n = 0
  go counter [] = 0
  go counter (x:xs) = x + go (counter + 1) xs

