class distance:
  def __init__(self, x=5,y=5):
    self.ft=x
    self.inch=y

  def __eq__(self, other):
    if self.ft==other.ft and self.inch==other.inch:
      return("both objects are equal")
    else:
      return("both objects are not equal")

  def __lt__(self, other):
    in1=self.ft*12+self.inch
    in2=other.ft*12+other.inch
    if in1<in2:
      return("first object smaller than other")
    else:
      return("first object not smaller than other")

  def __gt__(self, other):
    in1=self.ft*12+self.inch
    in2=other.ft*12+other.inch
    if in1<in2:
      return("first object greater than other")
    else:
      return("first object not greater than other")