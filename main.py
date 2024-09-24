from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates
import pdfkit
import io
import json
import base64
from schemas.pdfschema import JSONData
import os

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.post("/read_pdf_RQ")
async def read_pdf(request: Request, json_data: JSONData):
    # Load and encode image
    logo_base64 = image_to_base64("images/loginnew.png")
    print(logo_base64, "base 64 encoded image")
    
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

    # Generate the PDF with headers and footers
    header_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "templates", "header.html"))
    footer_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "templates", "footer.html"))

    print("Header path:", header_path)
    print("Footer path:", footer_path)


    # pdf = pdfkit.from_string(
    #     html_content, 
    #     False,
    #     options={
    #         "header-html": header_path,
    #         "footer-html": footer_path,
    #         "margin-top": "25mm",
    #         "margin-bottom": "25mm",
    #         "margin-left": "15mm",
    #         "margin-right": "15mm",
    #         "footer-spacing": "5",
    #         "header-spacing": "5",
    #         "disable-smart-shrinking": "",
    #     }
    # )


    # simple_html = "<h1>Hello, PDF!</h1>"
    # pdf = pdfkit.from_string(simple_html, False)

    pdf = pdfkit.from_string(
        html_content,
        False,
        options={
            "header-html": header_path,
            "footer-html": footer_path,
            "margin-top": "25mm",
            "margin-bottom": "25mm",
            "margin-left": "15mm",
            "margin-right": "15mm",
        }
    )


    # Return the PDF as a streaming response
    return StreamingResponse(
        io.BytesIO(pdf), 
        media_type='application/pdf', 
        headers={"Content-Disposition": "inline; filename=statement.pdf"}
    )

def image_to_base64(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
