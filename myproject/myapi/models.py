from django.db import models
from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo, BooleanProperty

# Create your models here.


class PERSON(StructuredNode):
    

    rationCardNo = StringProperty()
    genderCode = StringProperty()
    relationsipCode = StringProperty()
    relationshipName = StringProperty()
    uid = StringProperty(unique_index=True)
    membernameEn = StringProperty()
    membernameLL = StringProperty()
    memberDOB = StringProperty()
    motherNameEn = StringProperty()
    motherNameLL =StringProperty()
    fatherNameEN = StringProperty()
    fatherNameLl = StringProperty()
    SpouseEn = StringProperty()
    SpouseLL = StringProperty()
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
    #hasFam = StringProperty(default=False)


class FAMILY(StructuredNode):

    name = StringProperty(unique_index=True)

    #RELATIONSHIP
    HOF = RelationshipTo(PERSON,'HOF')
    wife = RelationshipTo(PERSON,'WIFE')
    son  = RelationshipTo(PERSON,'SON')
    daughter = RelationshipTo(PERSON,'DAUGHTER')



