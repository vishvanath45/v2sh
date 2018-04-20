import smtplib

sender = 'support@v2sh.in'



def sent_mail (message , to_email):
    smtpobj = smtplib.SMTP(host='smtpout.asia.secureserver.net', port=80)
    print ("1")
    smtpobj.login(sender, 'Br@zzers007')
    print ("2")
    smtpobj.sendmail(sender , to_email , message)
    print ("done!")
