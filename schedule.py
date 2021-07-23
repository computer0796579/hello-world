myteam = {
  "emp1" : {
    "name" : "X",
    "schedule" : "A/T"
  },
  "emp2" : {
    "name" : "Y",
    "schedule" : "B"
  },
  "emp3" : {
    "name" : "Z",
    "schedule" : "C"
  }
}

d = iter(myteam.items())

print(next(d))
