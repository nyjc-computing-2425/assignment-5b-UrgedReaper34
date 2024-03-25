# Part 1
def read_csv(filename):
  """
  Reads a .csv file and returns two lists, header and data

  Parameters
  ---------
  filename: str
      the name of the file to be read

  Returns
  ---------
  headers
      a list of headers of the csv file
  data
      nested list containing data of the csv file

  Example:
  >>> read_csv("my_hit_list.csv")
  ["Name", "Gender"], [["Ian Lau", "Male"], ["Mentos Man", "Indeterminate"]] 
  """
    # Type your code below
  with open(filename, "r") as f:
    rawdata = f.readlines()
    
    headers = rawdata[0].rstrip("\n").split(",")
    data = rawdata[1:]
    formattedData = []
    for rawline in data:
      line = rawline.rstrip("\n").split(",")
      line[0] = int(line[0])
      line[3] = int(line[3])
      formattedData.append(line)
   
    return headers, formattedData


# Part 2
def filter_gender(enrolment_by_age, sex):
  """
  Filters records and returns those that matches the parameter sex 
  Excluding the sex column 

  Parameters
  ---------
  enrolment_by_age: nested list
      the records to be sorted
  sex: string
      the sex to which to return records by

  Returns
  ---------
  data
      nested list containing sorted records excluding the sex column

  Example:
  >>> filter_gender([insert records here])
  [['1984', '18 YRS', '3927'], ['1984', '18 YRS', '2155']] 
  """
    # Type your code below
  data = []
  for person in enrolment_by_age:
    #If the sex column atches the sex parameter
    if(person[2] == sex):
      #Remove the sex column
      person.pop(2)
      data.append(person)
  return data


# Part 3
def sum_by_year(enrolment):
  """
  Adds up enrolment for each year, given a list of records

  Parameters
  ---------
  enrolment: nested list
      the records to be sorted
  Returns
  ---------
  data
      nested list containing two columns, the year and the total enrolment of that year

  Example:
  >>> sum_by_year([insert records here])
  [['1984', '3927'], ['1984','2155']] 
  """
    # Type your code below
  data = []
  for person in enrolment:
    # Lets search the database and see if theres an existing list corresponding to the persons year
    
    found_year = False
    for record in data:
      if int(person[0]) == record[0]:
        # There is an existing corresponding list in data!
        record[1] = record[1] + int(person[2])
        found_year = True
        break
    if not found_year:
      # There is no existing corresponding list in data
      # Store the record as an int
      data.append([int(person[0]), int(person[2])])
  return data
      


# Part 4
def write_csv(filename, header, data):
  """
  Writes the header and data to a csv file

  Parameters
  ---------
  filename: str
      name of the file
  header: list
      headers of the csv
  data: nested list
      rows of the csv
  Returns
  ---------
  linesWritten
      number of lines written to the csv

  Example:
  >>> write_csv("ilovecomputingsomuch.csv", ["kill", "me", "now"], [["save", "me", "i"], ["am", "half", "dead"]])
  69420 
  """
    # Type your code below
  with open("total-enrolment-by-year.csv", "w") as f:
    f.write(",".join(header) + "\n")
    for line in data:
      
      f.write(f"{line[0]},{line[1]}\n")
      


# TESTING
# You can write code below to call the above functions
# and test the output
