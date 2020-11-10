# this script is responsible for framing each individual squat

from csv import reader
import sys

def chop(File):
# open file in read mode
  f = None
  flag = 0
  with open(File, 'r') as read_obj:
      # pass the file object to reader() to get the reader object
      csv_reader = reader(read_obj)
      # Iterate over each row in the csv using reader object
      count = 0
      old = 0
      first_time = 0.0
      for row in csv_reader: # For each row
          if count != 0: # Skip the First Row
             # Use = -1.0 for Knees use -0.6 for squat
             # use row[2] for Y axis >=0.0
              if not (float(row[1]) <= -0.6): # start recording
                  # check if f exists
                  if f is None:
                      first_time = 0.0
                      filename = "%d_%s.csv" % (count, File)
                      f = open(filename, "w")
                      f.write("time,X_value,Y_value,Z_value\n")
                  else:
                      num = float(row[1]) #x
                      num2 = float(row[2]) #y 
                      num3 = float(row[3]) # z
                      if first_time == 0.0:
                          time = 0.0
                          first_time = float(row[0])
                      else:
                          time = float(row[0]) - first_time
                      print("Time: %f\n" % first_time)
                      f.write("%.5f,%.5f,%.5f,%.5f\n" % (time, num, num2, num3))

            # capture until it goes back neg
                  print(float(row[1]))
              elif (float(row[1]) <= -0.6):
                  flag = 0
                  first_time = 0.0
                  if f is not None:
                      f.close()
                  f = None
           

          count = count + 1

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        if i > 0:
            chop(arg)