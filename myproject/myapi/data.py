# import pandas as pd


# df = pd.read_csv('people.csv')
# people_dict = df.to_dict()


# peopledata = {}
# completedIds = []
# numpeople = len(people_dict['RationcardNo.'])

# for i in range(0, numpeople):
#     persondata = {}
#     for j in people_dict:
#         persondata[j] = people_dict[j][i]
#     peopledata[i] = persondata

# count = 2

# for person in peopledata.values():
#     print("Row number :"+str(count))
#     count+=1
#     personUID = (str(person["uid"])).lower().strip()
#     personName = (person["memberNameEN"]).lower().strip()
#     personGender = (person["genderCode"]).lower().strip()
#     personHouseNo = str(person["houseNoEN"]).lower().strip()