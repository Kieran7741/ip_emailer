import boto3
from botocore.exceptions import ClientError


def _send_email(sender_email, to_emails, body, subject='NO SUBJECT', aws_region="eu-west-1"):
    """
    Send a email using Amazons SES emailing service.
    :param sender_email: Email sender. Needs to be verified through AWS console
    :param body: dict containing html body and text body
    :param to_emails: list of emails to send to. While using free tier these also need to be verified
    :param subject: Email subject
    :param aws_region: Region the SES is located. Default to Ireland
    :return: Email successfully sent
    :rtype: bool
    """
    encoding = "UTF-8"
    sender = "Sender Name <{sender_email}>".format(sender_email=sender_email)
    # The email body for recipients with non-HTML email clients.
    body_text = body.get('text', 'No body text')
    # The HTML body of the email.
    body_html = body.get('html', """<body>{0}</body>""".format(body_text))

    # Create a new SES resource and specify a region.
    client = boto3.client('ses', region_name=aws_region)

    # Try to send the email.
    try:
        # Provide the contents of the email.
        response = client.send_email(Destination={'ToAddresses': to_emails,},
                                     Message={'Body': {
                                         'Html': {'Charset': encoding, 'Data': body_html,},
                                         'Text': {'Charset': encoding,'Data': body_text,},},
                                         'Subject': {'Charset': encoding,'Data': subject,},},
                                     Source=sender,)
    except ClientError as e:
        print(e.response['Error']['Message'])
        return False
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
        return True
