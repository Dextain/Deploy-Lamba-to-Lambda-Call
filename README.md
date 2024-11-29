# Deploy-Lamba-to-Lambda-Call
How to call one lambda function from another lambda function
	1. Execution time; splitting a process between two lambda since a lambda max time is 15min, splitting it can speed up the process.
STEPS

	1. Create IAM ROLE
		a. Attach policies
			i. Cloudwatch log
			ii. Lambda full access
	2. Create Lambda function using python and attach the role
		a. Go to configuration and edit
		b. Change timeoue - 1min
	3. Create Lambda no.02 using same process
	4. Write lambda function in Lambda 1
  5. Write Lambda function in Lambda 2
  6. 	6. Deploy
  7. Return to Lambda 01
  8. 		a. Test 
		b. Use 'Hello World' Template
    c. Create and test!

![image](https://github.com/Dextain/Deploy-Lamba-to-Lambda-Call/assets/174049610/7147963b-b849-4ff2-b8d6-156f038de96a)

done

