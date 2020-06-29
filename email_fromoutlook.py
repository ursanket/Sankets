#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import win32com.client as win32
def emailtoclient():
 outlook = win32.Dispatch('outlook.application')
 mail = outlook.CreateItem(0)
 mail.To = input("Recipient Email: ")
 mail.Subject = input("Subject: ")
 mail.Body = input("Enter your message:")
#mail.HTMLBody = '<h2>This is a test email</h2>' #this field is optional

# To attach a file to the email (optional):
#attachment  = "Path to the attachment"
#mail.Attachments.Add(attachment)

 mail.Send()
 print("mail sent!")


# In[ ]:


emailtoclient()


# In[ ]:




