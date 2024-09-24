from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    merchantID: str
    userID: str
    distributorID: str
    salesmemberID: str
    merchantewalletID: str
    merchantCode: str
    merchantAddress: str
    odFlowLevelID: str
    merchantMaximumODAmount: str
    merchantODDuration: str
    MerchantHaveActiveOD: str
    MerchantODLastUpdated: str
    consignmentMerchant: str
    merchantCreatedON: str
    merchantStatus: str
    merchantWalletStatus: str
    merchantWalletLastUpdate: str
    Address: Optional[str]
    StreetName: Optional[str]
    Area: Optional[str]
    POBox: Optional[str]
    Zone: Optional[str]
    City: Optional[str]
    State: Optional[str]
    Country: Optional[str]
    NFC: Optional[str]
    GPSLat: Optional[str]
    GPSLong: Optional[str]
    Website: Optional[str]
    ContactPerson: Optional[str]
    Designation: Optional[str]
    ContactPersonEmail: Optional[str]
    WorkPhone: Optional[str]
    TimeZone: Optional[str]
    Building: Optional[str]
    StreetNumber: Optional[str]
    ZoneNumber: Optional[str]
    BuildingNumber: Optional[str]
    UnitNumber: Optional[str]
    userTypeID: str
    userName: str
    userPhone: str
    userEmail: str
    userPassword: str
    userCreatedON: str
    userLastLogin: Optional[str]
    userVerified: str
    userStatus: str
    SPID: Optional[str]
    loginEmail: Optional[str]
    isSubuserType: Optional[str]

class Transaction(BaseModel):
    ledgerID: str
    transactionReferenceNo: str
    userID: str
    debitOrCredit: str
    amount: str
    previousBalance: str
    currentBalance: str
    transactionCreatedOn: str
    transactionUpdateOn: Optional[str]
    note: str
    transactionBilled: str
    transactionBilledON: Optional[str]
    transactionStatus: str
    transactionID: str
    transactionUID: str
    senderID: Optional[str]
    receiverID: Optional[str]
    transactionTypeID: str
    transactionCreatedON: str
    status: str
    clientReferenceid: Optional[str]
    transactionType: str
    transactionTypeStatus: str

class ConsignmentDetails(BaseModel):
    pass

class JSONData(BaseModel):
    userID: str
    balance: str
    fromdate: str
    todate: str
    user: User
    transactions: List[Transaction]
    consignment_details: List[ConsignmentDetails]
    # distributor: Optional[str]
    # sales_team: Optional[str]
    # current_year: int
