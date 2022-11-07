# code to track Covid-19 using python
while True:

    # importing Covid module
    from covid import Covid
    print("Covid Tracker")
    cv=Covid()


    act=cv.get_total_active_cases()
    rec=cv.get_total_recovered()
    death=cv.get_total_deaths()
    con=cv.get_total_confirmed_cases()


    print('----------Menu---------')
    print('1.Global Count')
    print('2.Active Cases')
    print('3.Confrimed Cases')
    print('4.Recovered Cases')
    print('5.Total Deaths')
    print('6.Get Covid update by country Name')
    print(" ")

    Choice=input('Enter your choice Number: ')

    # if-else statement used
    if Choice=='1':
        print('Active Cases:',act, '\nConfrimed Cases:',con, '\nRecovered Cases:',rec, '\nTotal Deaths:',death)
    elif Choice=='2':
        print('Active cases:',act)
    elif Choice=='3':
        print('Confirmed Cases:',con)
    elif Choice=='4':
        print('Recivered cases',rec)
    elif Choice=='5':
        print("Total Deaths:",death)
    elif Choice=='6':
        str=i=input('Enter Country Name: ')
        cname=cv.get_status_by_country_name(i)
        print(cname)
    else:
        print('Invalid Option')

    print('---------------------')
    play_again = input("Check again? (y/n): ")
    print(' ')
    if play_again.lower() != "y":
        break

    # End of Program
