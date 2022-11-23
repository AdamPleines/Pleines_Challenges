
# simple for function
for i in range(1, 16):
    # % -> remainder of division by
    print(i)
    if i % 15 == 0:
        print('fizz buzz')
    # continue/nothing is required instead of return due to the ongoing 'for'
    # classic elif -> elseif
    elif i % 3 == 0:
            print('fizz')

    elif i % 5 == 0:
            print('buzz')
#  the print can be added to the for function to display/test all values through 100
#    print(i)

# Book "Deep work - path to success"
# code in MVC, professional UI, have a database, create/read/update/delete, solve a *business* problem
# security login authentication (use external app like auth0 to provide critiques in interview)
# take bootstrap template, slap it on the project, and push it to market\
# build it with .net c# and nvc