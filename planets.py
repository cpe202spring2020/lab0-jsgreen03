def weight_on_planets():
   weight = int(input("What do you weigh on earth? "))
   mweight = weight * 0.38
   jweight = weight * 2.34
   print("\nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds.".format(mweight , jweight))

   
   
if __name__ == '__main__':
   weight_on_planets()