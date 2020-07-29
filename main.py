import smtplib 
  
# Creates SMTP session with Gmail using its specific port 587
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# Start TLS for security 
s.starttls() 
  
# Authentication to your Gmail Account
s.login("nishkarshraj000@gmail.com","[pass]") 
  
# Send Message
message = "Hello, World!"
  
# Send Mail 
s.sendmail("<<sender>>", "<<receiver>>", message) 
  
# Terminate SMTP Session 
s.quit() 

