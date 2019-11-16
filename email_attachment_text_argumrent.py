import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from datetime import date



#

def arg():
    file1 = open("arguments.ini", "r+")

    t = file1.read()
    arggs = t.split("\n")
    # print(arggs)
    return arggs
# global cam

def switch_alpha(argument):

    # for capital LETTERS ,special case just write same IN ALTERNET MANNER AND FOR small letters write numbers in alternet manner...

    pass_dict = {'$': '$', '0': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
                 'k': 11, 'l': 12, 'm': 13
        , 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
                 'z': 26,'@':'@','!':'!','~':'~','*':'*','(':'(',')':')','-':'-','_':'_','+':'+','=':'=','<':'<',
                 ',':',','>':'>','[':'[','{':'{','}':'}',']':']',':':':','"':'"',';':';','?':'?','/':'/',
                 '.':'.','^':'^','#':'#','&':'&',

                 'Q':'Q','W':'W','E':'E','R':'R','T':'T','Y':'Y','U':'U','I':'I','O':'O','P':'P','A':'A','S':'S','D':'D','F':'F','G':'G',
                 'H':'H','J':'J','K':'K','L':'L','Z':'Z','X':'X','C':'C','V':'V','B':'B','N':'N','M':'M'}          # in practice we need only nos 0-9 and special char.

    pass_dict.get(argument, "invalid argument...")
    return (pass_dict.get(argument))

def password_check(sender_email_password):

    j = 0
    password = ''
    end_pass_reconstructed = []
    while (j < len(sender_email_password)):
        if j % 2 == 1:
            end_pass_reconstructed.append(sender_email_password[j])
        j += 1


    for i in range(len(end_pass_reconstructed)):
        password += str(end_pass_reconstructed[i])

    x = 0
    full_pass = ''
    while (x < len(password)):
        full_pass  = str(switch_alpha(str(password[x]))) + str(full_pass)
        x += 1

    check_pass = full_pass[::-1]

    # print("password is ", check_pass)

    return (str(check_pass))


cam=0
def send_email_attachment(filepath):
    today = date.today()
    global cam
    arggs = []
    arggs = arg()
    cam = arggs[1]
    cam = str(cam)

    sender_email = arggs[3]

    sender_email_password = arggs[5]
    receiver_email = arggs[7]
    final_pass=password_check(sender_email_password)



    fromaddr=str(sender_email)
    toaddr=str(receiver_email)

      # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "daily report in csv"

    # string to store the body of the mail
    body = str(today)+"  alpr report...please find attachment..."

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    filename = str(today)+".csv"
    attachment = open(filepath, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, final_pass)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()












filepath ="/home/vinayak/demo/waiting_status/2019-09-23.csv"
send_email_attachment(filepath)