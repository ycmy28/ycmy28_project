# Chrun predition on Telco

```{attention}
This page is still on development on deploying.
```

## Dataset Description
The dataset consists of data customer churn of Telco which focused on customer retention program. The main goal of this project is to predict behavior to retain customer.

this dataset originated from ucL : https://www.kaggle.com/blastchar/telco-customer-churn

### Attribute Information:
Each row represents a customer, each column contains customer’s attributes described on the column Metadata.
Column Descriptions:
- Customers who left within the last month – the column is called Churn.

- Services that each customer has signed up for – phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies.

- Customer account information – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges.

- Demographic info about customers – gender, age range, and if they have partners and dependents.

1. customerID : A unique ID that identifies each customer.
2. gender : The customer’s gender: Male, Female.
3. SeniorCitizen: indicates if the customer is 65 or older: Yes, No
4. Partner : Indicates if the customer is married: Yes, No
5. Dependents : Indicates if the customer lives with any dependents: Yes, No. Dependents could be children, parents, grandparents, etc.
6. Tenure: Indicates the total amount of months that the customer has been with the company.
7. PhoneService : Indicates if the customer subscribes to home phone service with the company: Yes, No
8. MultipleLines : Indicates if the customer subscribes to multiple telephone lines with the company: Yes, No
9. InternetService : Indicates if the customer subscribes to Internet service with the company: No, DSL, Fiber Optic, Cable.
10. OnlineSecurity : Indicates if the customer subscribes to an additional online security service provided by the company: Yes, No
 
11. OnlineBackup : Indicates if the customer subscribes to an additional online backup service provided by the company: Yes, No.

12. DeviceProtection  Indicates if the customer subscribes to an additional device protection plan for their Internet equipment provided by the company: Yes, No

13. TechSupport        Indicates if the customer subscribes to an additional technical support plan from the company with reduced wait times: Yes, No

14. Streaming TV: Indicates if the customer uses their Internet service to stream television programing from a third party provider: Yes, No. The company does not charge an additional fee for this service.

15. Streaming Movies: Indicates if the customer uses their Internet service to stream movies from a third party provider: Yes, No. The company does not charge an additional fee for this service.
16. Contract: Indicates the customer’s current contract type: Month-to-Month, One Year, Two Year.

17. Paperless Billing: Indicates if the customer has chosen paperless billing: Yes, No

18. Payment Method: Indicates how the customer pays their bill: Bank Withdrawal, Credit Card, Mailed Check

19. Monthly Charge: Indicates the customer’s current total monthly charge for all their services from the company.

20. Total Charges: Indicates the customer’s total charges, calculated to the end of the quarter specified above.

21. Churn : customer status Yes = the customer left the company this quarter. No = the customer remained with the company. Directly related to Churn Value.
