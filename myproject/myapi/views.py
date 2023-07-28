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
from neomodel import *
from py2neo import *




class AddPerson(generics.GenericAPIView):
    
    
    def post(self,request):
    
        df = pd.read_csv('people.csv')
        family_dict = {}
        for i in range(len(df)):
            person_data = df.iloc[i]

            try:
                person = PERSON.nodes.get(rationCardNo = person_data['RationcardNo.'],
                                          genderCode = person_data['genderCode'],
                                          uid = person_data['uid'],
                                          memberNameEn = person_data['memberNameEN'],
                                          memberDOB = person_data['memberDOB'],
                                          motherNameEn = person_data['motherNameEn'],
                                          fatherNameEN = person_data['fatherNameEN'],
                                          SpouseEn = person_data['SpouseEN'],
                                          nationality = person_data['nationality'],
                                          mobileNo = person_data['mobileNo'],
                                          houseNoEN = person_data['houseNoEN'])
            except:
                person = PERSON(
                    rationCardNo = person_data['RationcardNo.'],
                    genderCode = person_data['genderCode'],
                    relationshipCode = person_data['relationshipCode'],
                    uid = person_data['uid'],
                    membernameEn = person_data['memberNameEN'],
                    memberDOB = person_data['memberDOB'],
                    motherNameEn = person_data['motherNameEN'],
                    fatherNameEN = person_data['fatherNameEN'],
                    SpouseEn = person_data['SpouseEN'],
                    nationality = person_data['nationality'],
                    MobileNo = lambda x:0 if person_data['mobileNo'] is 'NaN' else person_data['mobileNo'],
                    bankAcc = lambda x:0 if person_data['bankAccountNo'] is 'NaN' else person_data['bankAccountNo'],
                    ifscCode = person_data['ifscCode'],
                    email = person_data['email'],
                    divyangFlag = person_data['divyang'],
                    divyangPercentage = person_data['divyang_percentage'],
                    cardTypeId = person_data['cardTypeID'], 
                    occupationCode = person_data['occupationCode'], 
                    castCategoryId = person_data['casteCategoryId'], 
                    houseNoEN = person_data['houseNoEN'],
                    houseNoLl = lambda x:0 if person_data['houseNoLL'] is 'NaN' else person_data['houseNoLL'],
                    landmarkEn = lambda x:0 if person_data['landmarkEn'] is 'NaN' else person_data['landmarkEn'],
                    landmarkLL = lambda x:0 if person_data['landmarkLL'] is 'NaN' else person_data['landmarkLL'],
                    districtCode = person_data['districtCode'],
                    villageCode = lambda x:0 if person_data['villageCode'] is 'NaN' else person_data['villageCode'],
                    lgdBlockTownCode = person_data['lgdBlockTownCode'],
                    urbanRural = person_data['urbanRural'],
                    lgdWardVillageCode = lambda x:0 if person_data['lgdWardVillageCode'] is 'NaN' else person_data['lgdWardVillageCode'],
                    tehsilCode = lambda x:0 if person_data['tehsilCode'] is 'NaN' else person_data['tehsilCode'],
                    lgdColonyCode = lambda x:0 if person_data['lgdColonyCode'] is 'NaN' else person_data['lgdColonyCode'],
                    pinPalCode = person_data['pinPalCode'],
                    isHouseHoldMember = lambda x:0 if person_data['isHouseHoldMember'] is 'NaN' else person_data['isHouseHoldMember'],
                    shareDate = person_data['sharedate'],
                    reason = person_data['Reason']
                )

                person.save()
            

            try:
                family = FAMILY.nodes.get(rationCardNo = person.rationCardNo)
            except:
                family = FAMILY(rationCardNo = person.rationCardNo)
                if person.rationCardNo not in family_dict.keys(): 
                    family_dict [person.rationCardNo] = {}
                family.save()
                '''
                key as rationcard value as a empty dict
                '''
            
            if(11 == person_data['relationshipCode'] and 'M' == person.genderCode):
                family.father.connect(person)
                family_dict[person.rationCardNo]['father'] = person
                #print(family_dict)
                family.save()
                
            if(11 == person_data['relationshipCode'] and 'F' == person.genderCode):
                family.mother.connect(person)
                family_dict[person.rationCardNo]['mother'] = person
                family.save()
                
            elif(12 == person_data['relationshipCode'] and 'M' == person.genderCode):
                family.children.connect(person)
                family.save()
                

            elif(13 == person_data['relationshipCode'] and 'F' == person.genderCode):
                family.children.connect(person)
                family.save()
            
            elif(18 == person_data['relationshipCode'] and 'F' == person.genderCode):
                family.grand_daughter.connect(person)
                family.save()
            elif(19 == person_data['relationshipCode'] and 'M' == person.genderCode):
                family.grand_son.connect(person)
                family.save()
            
            #print(family_dict)
            fam = family_dict.values()
            for f in fam:
                print(f)
                break
                # f['father'].wife.connect(f['mother'])
                # f['mother'].husband.connect(f['father'])




            # for f in fam:
            #     for key in f[1]:
            #         if key == 'father':
            #             father_list.append(f[1][key])
            #         else:
            #             mother_list.append(f[1][key])

            # #print(family_dict)
            # for father in father_list:
            #     for mother in mother_list:
            #         if((person.membernameEn == mother.membernameEn) and (person.membernameEn == father.membernameEn)) and (father.houseNoEN == mother.houseNoEN):
            #             husb = PERSON.nodes.get(membernameEn = father.membenameEn)
            #             wif = PERSON.nodes.get(membernameEn = mother.membernameEn)
            #             # person.husband.connect(husb)
            #             # person.wife.connect(wif)
            #             print(type(husb))
              
           

           
            
        return Response(200)
            

        


       
        
    

    



