from telnetlib import DO
from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import generics, permissions, viewsets, generics
from rest_framework.response import Response
import pandas as pd
from neomodel import Q

def getData(self):
        
    df = pd.read_csv('people.csv')
    people_dict = df.to_dict()


    peopledata = {}
    numpeople = len(people_dict['RationcardNo.'])

    for i in range(0, numpeople):
        persondata = {}
        for j in people_dict:
            persondata[j] = people_dict[j][i]
        peopledata[i] = persondata

    return peopledata

class AddPerson(generics.GenericAPIView):
    
    
    def post(self,request):
    
        peoples = getData(self)
        # for people in peoples.values():
        #     print("1")

        # person = PERSON()
        for people in peoples.values():
            for i in people:
                if pd.isna(people[i]):
                    people[i] = None
            person = PERSON()
            person.rationCardNo = str(people["RationcardNo."]).lower().strip()
            person.genderCode = str(people["genderCode"]).lower().strip()
            person.relationsipCode = str(people["relationshipCode"]).lower().strip()
            person.relationshipName = str(people["relationshipName"]).lower().strip()
            person.uid = str(people["uid"]).lower().strip()
            person.membernameEn = str(people["memberNameEN"]).lower().strip()
            person.membernameLL = str(people["memberNameLL"]).lower().strip()
            person.memberDOB = str(people["memberDOB"]).lower().strip()
            person.motherNameEn = str(people["motherNameEN"]).lower().strip()
            person.motherNameLL = str(people["motherNameLL"]).lower().strip()
            person.fatherNameEN = str(people["fatherNameEN"]).lower().strip()
            person.fatherNameLl = str(people["fatherNameLL"]).lower().strip()
            person.SpouseEn = str(people["SpouseEN"]).lower().strip()
            person.SpouseLL = str(people["SpouseLL"]).lower().strip()
            person.nationality = str(people["nationality"]).lower().strip()
            person.mobileNo = str(people["mobileNo"]).lower().strip()
            if pd.isna(str(people["bankAccountNo"]).lower().strip()):
                person.bankAccountNo = None
            else:
                person.bankAccountNo = str(people["bankAccountNo"]).lower().strip()
            person.ifscCode = str(people["ifscCode"]).lower().strip()
            person.email = str(people["email"]).lower().strip()
            person.divyang = str(people["divyang"]).lower().strip()
            person.divyang_percentage = str(people["divyang_percentage"]).lower().strip()
            person.cardTypeID = str(people["cardTypeID"]).lower().strip()
            person.occupationCode = str(people["occupationCode"]).lower().strip()
            person.casteCategoryID = str(people["casteCategoryId"]).lower().strip()
            person.houseNoEN = str(people["houseNoEN"]).lower().strip()
            person.houseNoLL = str(people["houseNoLL"]).lower().strip()
            person.landmarkEn = str(people["landmarkEN"]).lower().strip()
            person.landmarkLL = str(people["landmarkLL"]).lower().strip()
            person.districtCode = str(people["districtCode"]).lower().strip()
            if pd.isna(str(people["villageCode"]).lower().strip()):
                person.villageCode = None
            else:
                person.villageCode = str(people["villageCode"]).lower().strip()
            person.lgdBlockTownCode = str(people["lgdBlockTownCode"]).lower().strip()
            person.urbanRural = str(people["urbanRural"]).lower().strip()
            person.lgdWardVillageCode = str(people["lgdWardVillageCode"]).lower().strip()
            if pd.isna(str(people["tehsilCode"]).lower().strip()):
                person.tehsilCode = None
            else:
                person.tehsilCode = str(people["tehsilCode"]).lower().strip()
            if pd.isna(str(people["lgdColonyCode"]).lower().strip()):
                person.lgdColonyCode = None
            else:
                person.lgdColonyCode = str(people["lgdColonyCode"]).lower().strip()
            person.pinPalCode = str(people["pinPalCode"]).lower().strip()
            person.isHouseHoldMember1 = str(people["IsHouseHoldMember1"]).lower().strip()
            person.shareDate = str(people["sharedate"]).lower().strip()
            person.reason = str(people["Reason"]).lower().strip()
            
            person.save()
        

        return Response(200)

# class AddFamily(generics.GenericAPIView):
#     def post(self,request):
        
#         #familyName = request.data.get('name')
#         person = PERSON()
#         peoples = peopledata

#         # for people in peoples.values():

#             if person.genderCode == 'M':
#                 Husband = person.membernameEn
#             else:
#                 Wife = person.membernameEn
            
#             if Husband == people
        
#         if person.relationshipName == 'SELF' and person.houseNoEN = HoF
#         spouse = request.data.get('wife')
#         son = request.data.get('son')
#         daughter = request.data.get('daughter')
        
#         # Head = PERSON.nodes.get(name=HoF)
#         # w = Wife = PERSON.nodes.get(name=wife)

#         # family = FAMILY(name=familyName)
        
#         family.save()

#         # person2 = family.HOF.connect(Head)
#         # person1 = family.wife.connect(w)
    
#         return Response(200)

class AddFamily(generics.GenericAPIView):

    def post(self, request):

        peoples = getData(self)
        completed_Ids = []

        for people in peoples.values():
            for i in people:
                if pd.isna(people[i]):
                    people[i] = None
            #person_obj = PERSON()
            personUID = (str(people["uid"])).lower().strip()
            personName = (people["memberNameEN"]).lower().strip()
            personGender = (people["genderCode"]).lower().strip()
            personHouseNo = str(people["houseNoEN"]).lower().strip()

            if (personUID in completed_Ids):
                continue
            uidList = [personUID]
            if(personGender == 'm'):
                father = personName
            else: 
                mother = personName

            family_list = []
            family = PERSON.nodes.filter(Q(Q(fatherNameEN=personName) | Q(motherNameEn=personName) | Q(SpouseEn=personName)) & Q(houseNoEN=personHouseNo))                    #(houseNoEN=personHouseNo) 
            for i in family.all():
                family_list.append(i)
            #print(family_list)
            spouse = ""
            children=[]
            for person in family_list:
                #print(f'{person}\n--------------------------------------------------------------------')
                print(type(person))
                # check if person is spouse
                spouse = str(person.get('SpouseEN')).lower().strip()
                # print(spouse)
            #     spouse = person['SpouseEn']
            #     uidList.append((str(person["uid"])).lower().strip())
        
            #     if(spouse == personName):
            #         if(personGender == 'm'):
            #             mother = str(person['memberNameEN']).strip().lower()
            #         else:
            #             father = str(person['memberNameEN']).strip().lower()
            #     else:
            #         children.append(str(person['memberNameEN']).lower().strip())
            # print("Father: ",father," | Mother: ",mother)
            # for child in children:
            #     print("Child: ",child)
            # print(uidList)
            # print("--------------------------------------------------------------")
            # print("spouse: ",spouse)








        return Response(200)
# class DeletePerson(generics.GenericAPIView):
#     def post(self,request):
        
#         name = request.data.get('name')
        
#         person = PERSON.nodes.get(name=name)

#         person.delete()
            #family_list = person_obj.nodes.get( Q( Q(personName=person_obj.fatherNameEN) | Q(personName=person_obj.motherNameEn) | Q(personName=person_obj.SpouseEn)) & Q(personHouseNo=person_obj.houseNoEN) )
#         return Response(200)