from typing import List, Optional, Union
from pydantic import BaseModel

class User(BaseModel):
    merchantID: Optional[Union[str, int]]
    userID: Optional[Union[str, int]]
    distributorID: Optional[Union[str, int]]
    salesmemberID: Optional[Union[str, int]]
    merchantewalletID: Optional[Union[str, int]]
    merchantCode: Optional[Union[str, int]]
    merchantAddress: Optional[Union[str, int]]
    odFlowLevelID: Optional[Union[str, int]]
    merchantMaximumODAmount: Optional[Union[str, int]]
    merchantODDuration: Optional[Union[str, int]]
    MerchantHaveActiveOD: Optional[Union[str, int]]
    MerchantODLastUpdated: Optional[Union[str, int]]
    consignmentMerchant: Optional[Union[str, int]]
    merchantCreatedON: Optional[Union[str, int]]
    merchantStatus: Optional[Union[str, int]]
    merchantWalletStatus: Optional[Union[str, int]]
    merchantWalletLastUpdate: Optional[Union[str, int]]
    Address: Optional[Union[str, int]]
    StreetName: Optional[Union[str, int]]
    Area: Optional[Union[str, int]]
    POBox: Optional[Union[str, int]]
    Zone: Optional[Union[str, int]]
    City: Optional[Union[str, int]]
    State: Optional[Union[str, int]]
    Country: Optional[Union[str, int]]
    NFC: Optional[Union[str, int]]
    GPSLat: Optional[Union[str, int]]
    GPSLong: Optional[Union[str, int]]
    Website: Optional[Union[str, int]]
    ContactPerson: Optional[Union[str, int]]
    Designation: Optional[Union[str, int]]
    ContactPersonEmail: Optional[Union[str, int]]
    WorkPhone: Optional[Union[str, int]]
    TimeZone: Optional[Union[str, int]]
    Building: Optional[Union[str, int]]
    StreetNumber: Optional[Union[str, int]]
    ZoneNumber: Optional[Union[str, int]]
    BuildingNumber: Optional[Union[str, int]]
    UnitNumber: Optional[Union[str, int]]
    userTypeID: Optional[Union[str, int]]
    userName: Optional[Union[str, int]]
    userPhone: Optional[Union[str, int]]
    userEmail: Optional[Union[str, int]]
    userPassword: Optional[Union[str, int]]
    userCreatedON: Optional[Union[str, int]]
    userLastLogin: Optional[Union[str, int]]
    userVerified: Optional[Union[str, int]]
    userStatus: Optional[Union[str, int]]
    SPID: Optional[Union[str, int]]
    loginEmail: Optional[Union[str, int]]
    isSubuserType: Optional[Union[str, int]]

class Transaction(BaseModel):
    ledgerID: Optional[Union[str, int]]
    transactionReferenceNo: Optional[Union[str, int]]
    userID: Optional[Union[str, int]]
    debitOrCredit: Optional[Union[str, int]]
    amount: Optional[Union[str, int]]
    previousBalance: Optional[Union[str, int]]
    currentBalance: Optional[Union[str, int]]
    transactionCreatedOn: Optional[Union[str, int]]
    transactionUpdateOn: Optional[Union[str, int]]
    note: Optional[Union[str, int]]
    transactionBilled: Optional[Union[str, int]]
    transactionBilledON: Optional[Union[str, int]]
    transactionStatus: Optional[Union[str, int]]
    transactionID: Optional[Union[str, int]]
    transactionUID: Optional[Union[str, int]]
    senderID: Optional[Union[str, int]]
    receiverID: Optional[Union[str, int]]
    transactionTypeID: Optional[Union[str, int]]
    transactionCreatedON: Optional[Union[str, int]]
    status: Optional[Union[str, int]]
    clientReferenceid: Optional[Union[str, int]]
    transactionType: Optional[Union[str, int]]
    transactionTypeStatus: Optional[Union[str, int]]

class ConsignmentDetails(BaseModel):
    # Define any fields here as Optional if needed
    pass

class JSONData(BaseModel):
    userID: Optional[Union[str, int]]
    balance: Optional[Union[str, int]]
    fromdate: Optional[Union[str, int]]
    todate: Optional[Union[str, int]]
    user: Optional[User]
    transactions: Optional[List[Transaction]]
    consignment_details: Optional[List[ConsignmentDetails]]

class JSONData1(BaseModel):
    userName: Optional[Union[str, int]]
    merchantCode: Optional[Union[str, int]]
    transactions: Optional[List[Union[str, int]]]