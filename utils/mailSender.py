import smtplib, os
from config import *
from flask_redmail import RedMail
from urllib.parse import urlparse
from flask import request
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


app.config["EMAIL_HOST"] = 'premium10.web-hosting.com'
app.config["EMAIL_PORT"] = 587
app.config["EMAIL_USERNAME"] = os.getenv('SENDER_MAIL')
app.config["EMAIL_PASSWORD"] = os.getenv('SENDER_PASSWORD')
mail = RedMail(app)



def mail_sender(email, orderId, domain, role):

    parsed_uri = urlparse(request.url)
    result = f'{domain}/{role}/order-info.html?id={orderId}'.format(uri=parsed_uri)
    mail.send(
        subject="New Order",
        receivers=["mustafaabbas@webnike.com"],

        html = f"""
        <h2>You have been included in ORDER # {orderId}</h2>
        <p style="font-size:17px;">Please Click the Button below to redirect to order</p>
        
        <table width="100%" cellspacing="0" cellpadding="0">
        <tr>
            <td>
                <table cellspacing="0" cellpadding="0">
                    <tr>
                        <td style="border-radius: 2px;" bgcolor="#ED2939">
                            <a href="{result}" target="_blank" style="padding: 8px 12px; border: 1px solid #ED2939;
                            border-radius: 30px;font-family: Helvetica, Arial, sans-serif;font-size: 14px; color: #ffffff;
                            text-decoration: none;font-weight:bold;display: inline-block;">
                                Go To Order             
                            </a>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
      </table>
        
        """
    )