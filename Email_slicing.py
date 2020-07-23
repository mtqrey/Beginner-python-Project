# Get user email address
email = input("What is your email address?: ")

user_name = email[0:email.index('@')]



domain_name = email[email.index("@")+1:]


output = "Your username is '{}' and your domain name is '{}'".format(user_name,domain_name)

# Display output message
print(output)