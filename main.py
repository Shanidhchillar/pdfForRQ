from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates
import pdfkit
import io
import json
from fastapi.responses import HTMLResponse
from schemas.pdfschema import JSONData

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/read_pdf")
async def read_pdf(request: Request, json_data: JSONData):
    # Load and encode image
    logo_base64 = image_to_base64("images/loginnew.png")

    # Access data from the Pydantic model
    opening_balance = json_data.transactions[0].currentBalance
    closing_balance = json_data.transactions[-1].currentBalance

    # Calculate total credit and debit entries
    total_credit_entries = sum(1 for transaction in json_data.transactions if transaction.debitOrCredit == "1")
    total_debit_entries = sum(1 for transaction in json_data.transactions if transaction.debitOrCredit == "2")

    # Render the HTML template
    html_content = templates.TemplateResponse(
        "newpdf_file.html", 
        {
            "request": request, 
            **json_data.dict(),  # Convert Pydantic model to a dictionary
            "base64_image": logo_base64,
            "opening_balance": opening_balance,
            "closing_balance": closing_balance,
            "total_credit_entries": total_credit_entries,
            "total_debit_entries": total_debit_entries
        }
    ).body.decode()

    # Generate PDF from the rendered HTML
    pdf = pdfkit.from_string(html_content, False)

    # Return the PDF as a streaming response
    return StreamingResponse(io.BytesIO(pdf), media_type='application/pdf', headers={"Content-Disposition": "inline; filename=statement.pdf"})




@app.get("/generate_pdf", response_class=HTMLResponse)
async def generate_pdf(request: Request):
    # Example JSON data with 'null' values
    logo_base64 = image_to_base64("images/loginnew.png")
    json_data_str = '''
    {
        "userID": "530",
        "balance": "307.23",
        "fromdate": "2024-07-01",
        "todate": "2024-08-01",
        "user": {
            "merchantID": "53",
            "userID": "530",
            "distributorID": "36",
            "salesmemberID": "15",
            "merchantewalletID": "MEWID0000530",
            "merchantCode": "AVA_05",
            "merchantAddress": "Test, Test, Test",
            "odFlowLevelID": "2",
            "merchantMaximumODAmount": "1000",
            "merchantODDuration": "5",
            "MerchantHaveActiveOD": "0",
            "MerchantODLastUpdated": "2024-02-28 21:29:24",
            "consignmentMerchant": "0",
            "merchantCreatedON": "2024-02-20 12:43:43",
            "merchantStatus": "1",
            "merchantWalletStatus": "1",
            "merchantWalletLastUpdate": "2024-04-29 10:07:27",
            "Address": null,
            "StreetName": null,
            "Area": null,
            "POBox": null,
            "Zone": null,
            "City": null,
            "State": null,
            "Country": null,
            "NFC": null,
            "GPSLat": null,
            "GPSLong": null,
            "Website": null,
            "ContactPerson": null,
            "Designation": null,
            "ContactPersonEmail": null,
            "WorkPhone": null,
            "TimeZone": null,
            "Building": null,
            "StreetNumber": null,
            "ZoneNumber": null,
            "BuildingNumber": null,
            "UnitNumber": null,
            "userTypeID": "4",
            "userName": "Justin",
            "userPhone": "8675545342",
            "userEmail": "jyothi.r@chillarcards.com",
            "userPassword": "MTIzNDU2",
            "userCreatedON": "2024-02-20 12:43:43",
            "userLastLogin": null,
            "userVerified": "0",
            "userStatus": "1",
            "SPID": null,
            "loginEmail": null,
            "isSubuserType": null
        },
        "transactions": [
            {
                "ledgerID": "410",
                "transactionReferenceNo": "RCHX709119329lUq",
                "userID": "530",
                "debitOrCredit": "2",
                "amount": "4.00",
                "previousBalance": "189.23",
                "currentBalance": "185.23",
                "transactionCreatedOn": "2024-07-29 15:24:12",
                "transactionUpdateOn": null,
                "note": "sale",
                "transactionBilled": "0",
                "transactionBilledON": null,
                "transactionStatus": "1",
                "transactionID": "853",
                "transactionUID": "RCHX709119329lUq",
                "senderID": "530",
                "receiverID": null,
                "transactionTypeID": "6",
                "transactionCreatedON": "2024-07-29 15:24:12",
                "status": "1",
                "clientReferenceid": "we346tt7",
                "transactionType": "merchant_sale",
                "transactionTypeStatus": "1"
            }
        ],
        "consignment_details": [],
        "distributor": null,
        "sales_team": null,
        "current_year": 2024
    }
    '''

    # Convert JSON string to Python dictionary
    json_data = json.loads(json_data_str)

    return templates.TemplateResponse("newpdf_file.html", {"request": request, **json_data, "base64_image": logo_base64})


import base64

def image_to_base64(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
