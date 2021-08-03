# Auto Request Assigner Bot

_This project has been developed as a solution for the problem statement 2 of Laiye RPA Hackathon 2021._


# Problem Statement: 

_"The new generation of customers demand faster responses and better customer service in the retails industry. How can they leverage RPA to help with retailers for delivering good customer services ?"_


# Current Manual Process: 

_This solution revolves around the customer support department in our case we have considered the IT department of a prestigious firm. They receive requests from their customer base every day for various type of queries and issues related to Networking, Desktop hardware and software issues._ 

_These requests can come in form of any language by the customers as they have set up their business globally. The current manual process involves customers to send emails to the IT department head regarding their issues which the IT department head sends across his team depending on the language of the customer._

_The team consists of subject matter experts who have been trained in different languages and they in turn analyze the catergoy of the issue and raise an incident in Service Now and enter the same details in Salesforce for having the record of tickets._


# Solution Statement:

 _As per our solution, the AutoRequestAssigner mailbox will be created where the incoming emails will be stored. A bot will be scheduled at different intervals of time throughout the day which will fetch the incoming emails and detect the language in which the customer has sent the email._ 

_Upon successful detection of the language, the bot will translate the email into default configurable language (which is english in our case) and will then invoke the custom Machine Language classifier model hosted on cloud to determine the type of the incident._ 

_Bot will assign the incident to the IT department team queue and will post a comment with the translated email body. Bot will then enter the same details in Salesforce CRM application and send a request confirmation reply to the customer with the incident number._

_At the end of process, an automated voice call will be sent to the IT department head to notify him about all the incidents raised by the Bot so that he can allocate the tickets among his workforce based on their availability._
## Team Details

__Team Name:__ _Team Automators_

__Team Members:__
- Devneet Mohanty 
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://devneet.github.io) 

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/devneetmohanty07/)

- Chaitanya Kulkarni
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/chaitanya007/)

## Technologies Used

* Laiye RPA
* Python
* Java
* .NET
* Azure LUIS

## Services Integrated

* Salesforce CRM
* Service Now
* Twilio
* Google Translate

## Reference Documents

* As-Is Process Workflow (.vsdx and .pdf): 
  - _"Submission Documents\Process Flows.vsdx"_
  - _"Submission Documents\Process Flows.pdf"_ 


* To-Be Process Workflow (.vsdx and .pdf):
  - _"Submission Documents\Process Flows.vsdx"_
  - _"Submission Documents\Process Flows.pdf"_ 


* Screenshots Of Solution:
  - _"Submission Documents\Solution Screenshots Documents.docx"_


* Presentation Of Solution:
  - _"Submission Documents\AutoRequestAssignerBot.pptx"_

* Demo Video Of Solution:
  - _"Demo Video\AutoRequestAssignerBotInAction.wmv"_