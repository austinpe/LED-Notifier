import imaplib, re, time
from email.parser import HeaderParser

#Subject Line Disabled by default
#Need to add formating and char length limit

#to do!
#impliment char length limit

#known bugs
#if any edit is made to unchecked mail (read/deleted)
#script will display current newest email

#imap_server = raw_input("Enter the imap address of the mail server: ")
#imap_nickname = raw_input("Enter a nickname for this account: ")
#imap_username = raw_input("Enter your username for this account: ")
#imap_pass = raw_input("Enter your password for this account: ")

imap_server = "imap.gmail.com"
imap_nickname = "GMAIL"
imap_username = "techxpotest"
imap_pass = "mobilet3ch"


#Imap Server Info
mail = imaplib.IMAP4_SSL(imap_server, 993)
mail.login(imap_username, imap_pass)

#Get unread count
unread_count_initial = re.search("UNSEEN (\d+)", mail.status("INBOX", "(UNSEEN)")[1][0]).group(1)

#Checking for New Mail
def gmail_for_techxpo_test_refresh():
    global imap_server
    global imap_nickname
    global imap_username
    global imap_pass
    global mail
    global unread_count_initial
    unread_count_current = re.search("UNSEEN (\d+)", mail.status("INBOX", "(UNSEEN)")[1][0]).group(1)
    if unread_count_current != unread_count_initial:
        mail.select()
        #finding total mail count where latest email = mail count
        status, mail_count = mail.search(None, 'ALL')
        mail_count = mail_count[0].split()
        mail_count = int(mail_count[-1])
        
        #getting data from latest email
        email_data = mail.fetch(mail_count, '(BODY.PEEK[])')
        header_data = email_data[1][0][1]
        parser = HeaderParser()
        email_info = parser.parsestr(header_data)

        #email sender
        email_from = email_info['From']
        email_from = email_from.split("<")[0]

        #email subject line
        email_subject = email_info['Subject']

        #print to prompt for debugging purposes
        unread_count_initial = unread_count_current
        return "New " + imap_nickname +" from " + email_from

    return None
        
        
