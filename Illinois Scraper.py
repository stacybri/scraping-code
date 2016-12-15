 
import requests
from bs4 import BeautifulSoup
import pandas as pd

url='http://www.dhs.state.il.us/page.aspx?item=51101'
r=requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

# Create variables to score the scraped data in
county = []
January = []
February = []
March = []
April = []
May = []
June = []
July = []
August = []
September = []
October = []
November = []
December = []

# Create an object of the first object that is class=dataframe
table = soup.find(class_='tableStyle3')



# Find all the <tr> tag pairs, skip the first one, then for each.
for row in table.find_all('tr')[1:]:
    # Create a variable of all the <td> tag pairs in each <tr> tag pair,
    col = row.find_all('td')
    col1=row.find('th').find_all('strong')

    # Create a variable of the string inside 1st <td> tag pair,
    column_1 = col1[0].string.strip()
    # and append it to  variable
    county.append(column_1)

    # Create a variable of the string inside 2nd <td> tag pair,
    column_2 = col[0].string.strip()
    # and append it to  variable
    January.append(column_2)

    # Create a variable of the string inside 2nd <td> tag pair,
    column_3 = col[1].string.strip()
    # and append it to  variable
    February.append(column_3)

    # Create a variable of the string inside 2nd <td> tag pair,
    column_4 = col[2].string.strip()
    # and append it to  variable
    March.append(column_4)

    # Create a variable of the string inside 2nd <td> tag pair,
    column_5 = col[3].string.strip()
    # and append it to  variable
    April.append(column_5)

    # Create a variable of the string inside 2nd <td> tag pair,
    column_6 = col[4].string.strip()
    # and append it to  variable
    May.append(column_6)
 
    # Create a variable of the string inside 2nd <td> tag pair,
    column_7 = col[5].string.strip()
    # and append it to  variable
    June.append(column_7)

    # Create a variable of the string inside 2nd <td> tag pair,
    column_8 = col[6].string.strip()
    # and append it to  variable
    July.append(column_8)

    # Create a variable of the string inside 2nd <td> tag pair,
    column_9 = col[7].string.strip()
    # and append it to  variable
    August.append(column_9)

    # Create a variable of the string inside 2nd <td> tag pair,
    column_10 = col[8].string.strip()
    # and append it to  variable
    September.append(column_10)

    # Create a variable of the string inside 2nd <td> tag pair,
    column_11 = col[9].string.strip()
    # and append it to  variable
    October.append(column_11)

    # Create a variable of the string inside 2nd <td> tag pair,
    column_12 = col[10].string.strip()
    # and append it to  variable
    November.append(column_12)

    # Create a variable of the string inside 2nd <td> tag pair,
    column_13 = col[11].string.strip()
    # and append it to  variable
    December.append(column_13)


# Create a variable of the value of the columns
columns = {'county': county, 'January': January, 'February': February, 'March': March, 'April': April, 'May': May, 'June': June, 'July': July, 'August': August, 'September': September, 'October': October, 'November': November, 'December': December}

# Create a dataframe from the columns variable
df = pd.DataFrame(columns)
df=df[['county','January','February','March','April','May','June','July','August','September','October','November','December']]


df.to_csv('U:\Documents\SNAP Data 2010.csv')
