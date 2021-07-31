def CalculateAllowance(Area,NoOfPeople):
   Area = int()
   NumberOfPeople = int()
   Allowed = bool()
   Ratio = Area/NoOfPeople
    if Ratio >= 2:
      Allowed = True

    elif Ratio < 2:
      Allowed = False
  return Allowed