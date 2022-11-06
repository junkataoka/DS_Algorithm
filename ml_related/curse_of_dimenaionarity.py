def __main__():
   def distance(cord1, cord2):
      val = 0
      for elem1, elem2 in zip(cord1, cord2):
        val += (elem1 - elem2)**2
      return val**1/2

   cord1 = [0.1  for i in range(1, 10)]
   cord2 = [0.3  for i in range(1, 10)]
   cord3 = [0.1  for i in range(1, 100)]
   cord4 = [0.3  for i in range(1, 100)]
   cord5 = [0.1  for i in range(1, 1000)]
   cord6 = [0.3  for i in range(1, 1000)]
   cord7 = [0.1  for i in range(1, 10000)]
   cord8 = [0.3  for i in range(1, 10000)]
   print("distance in 10D" )
   print(distance(cord1, cord2))
   print("distance in 100D" )
   print(distance(cord3, cord4))
   print("distance in 1000D" )
   print(distance(cord5, cord6))
   print("distance in 10000D" )
   print(distance(cord7, cord8))
   print("Interestingly, increase is not linear :) As dimension gets increased, two points become sparser and sparser :)")

if __name__ == "__main__":
   __main__()