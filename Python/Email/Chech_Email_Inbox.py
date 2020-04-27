# https://automatetheboringstuff.com/chapter16/
import imapclient
import pyzmail
conn = imapclient.IMAPClient('imap.gmail.com',ssl=True)
"""Gmail imap.gmail.com
Outlook.com/Hotmail.com imap-mail.outlook.com
Yahoo Mail imap.mail.yahoo.com
AT&T imap.mail.att.net
Comcast imap.comcast.net
Verizon incoming.verizon.net

"""

conn.login('brucewayne18112000@gmail.com','pfvatzktlfxjaxeo')
conn.select_folder('INBOX',readonly=True)
UIDs = conn.search(['SINCE' ,'05-Apr-2019'])
# print(UIDs)
rawMessage = conn.fetch([180],['BODY[]','FLAGS'])
# print(rawMessage)
message = pyzmail.PyzMessage.factory(rawMessage[180][b'BODY[]'])
# print(message)
# print(message.get_subject())
# print(message.get_addresses('from'))
# print(message.get_addresses('to'))
# print(message.get_addresses('bcc'))

# print(message.text_part)
# print(message.html_part)

# print(message.text_part.get_payload().decode('UTF-8'))
# print(message.text_part.charset)

# print(conn.list_folders())

conn.select_folder('INBOX',readonly=False)
UIDs = conn.search(['ON','24-Apr-2020'])
print(UIDs)
# conn.delete_messages([180])
conn.logout()
