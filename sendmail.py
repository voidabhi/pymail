import smtplib
 
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems
    
username = raw_input("Enter Username!")
password = raw_input("Enter Password!")
to_addr = raw_input("Enter To Address")
cc_addr = raw_input("Enter CC Address")
subject = raw_input("Enter Subject!")
message = raw_input("Enter Message!")

    
sendemail(from_addr    = '', 
          to_addr_list = [to_addr],
          cc_addr_list = [cc_addr], 
          subject      = subject, 
          message      = message, 
          login        = username, 
          password     = password)   