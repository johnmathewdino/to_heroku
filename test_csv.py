import csv

filename = 'facultynew.csv'

# header = []
# rows = []
#
# with open(filename, 'r') as file:
#
# #     header
#     header.append(next(file))
#
# #     row
#     for row in file:
#         rows.append(row)
#
#
# print(rows)

def process_csv(filename):
    # INPUT - Filaname
    # OUTPUT - Rows of the csv (except header)

    with open(filename, 'r') as file:

        header = next(file)

        # print(header.lower().replace(" ", "").strip())

        if header.lower().replace(" ", "").strip() == "firstname,lastname,username,emailaddress":
            rows = []

            for row in file:
                rows.append(row)
            return rows

def process_names(namelist):

    # INPUT = string of unprocessed name ('Jonel,Prado,jprado,jprado@gmail.com\n')
    # OUTPUT = DICT = first name, last name, username, email
    info = namelist.replace("\n", "").split(',')
    # print(info)

    tempdict = {}

    tempdict['firstname'] = info[0]
    tempdict['lastname'] = info[1]
    tempdict['username'] = info[2]
    tempdict['email'] = info[3]


    return tempdict

processed_csv = process_csv('facultynew.csv')

for infos in processed_csv:
    dictinfo = process_names(infos)
    print(dictinfo['username'])


