from django.db import models
from neomodel import *#StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo, BooleanProperty

# Create your models here.


class PERSON(StructuredNode):
    

    rationCardNo = StringProperty()
    genderCode = StringProperty()
    relationshipCode = StringProperty()
    #relationshipName = StringProperty()
    uid = StringProperty(unique_index=True)
    membernameEn = StringProperty()
    #membernameLL = StringProperty()
    memberDOB = StringProperty()
    motherNameEn = StringProperty()
    #motherNameLL =StringProperty()
    fatherNameEN = StringProperty()
    #fatherNameLl = StringProperty()
    SpouseEn = StringProperty()
    #SpouseLL = StringProperty()
    nationality = StringProperty()
    mobileNo = StringProperty()
    bankAccountNo = StringProperty()
    ifscCode =StringProperty()
    email = StringProperty()
    divyang = StringProperty()
    divyang_percentage = StringProperty()
    cardTypeID = StringProperty()
    occupationCode = StringProperty()
    casteCategoryID = StringProperty()
    houseNoEN = StringProperty()
    houseNoLL = StringProperty()
    landmarkEn = StringProperty()
    landmarkLL =StringProperty()
    districtCode = StringProperty()
    villageCode = StringProperty()
    lgdBlockTownCode = StringProperty()
    urbanRural = StringProperty()
    lgdWardVillageCode = StringProperty()
    tehsilCode = StringProperty()
    lgdColonyCode = StringProperty()
    pinPalCode = StringProperty()
    isHouseHoldMember1 = StringProperty()
    shareDate = StringProperty()
    reason = StringProperty()
    wife = RelationshipTo('PERSON', 'WIFE')
    husband = RelationshipTo('PERSON', 'HUSBAND')
    son = RelationshipTo('PERSON', 'SON')
    daughter = RelationshipTo('PERSON', 'DAUGHTER')
    


class FAMILY(StructuredNode):

    rationCardNo = StringProperty(unique_index=True)

    #RELATIONSHIP
    spouse = RelationshipTo(PERSON,'SPOUSE')
    children = RelationshipTo(PERSON, 'CHILDREN')
    father = RelationshipTo(PERSON, 'FATHER')
    mother = RelationshipTo(PERSON, 'MOTHER')
    d_i_l = RelationshipTo(PERSON, 'DAUGHTER IN LAW')
    grand_son = RelationshipTo(PERSON, 'GRAND SON')
    grand_daughter = RelationshipTo(PERSON, 'GRAND DAUGHTER')


