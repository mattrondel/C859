#Welcome Message
def thanks():
        print(uname +", Thank you for using my calculator!")
#Ask User Name
#Store input as user name
uname=input("What is your name? ")
#Ask if Salaried
def ask_user():
        answer = input(uname +", Are you Salaried? (y/n) ")
        try:
                if answer.lower() == 'y':
                        return True
                elif answer.lower() =='n':
                        return False
                else:
                        print(f"Invalid response")
                        return ask_user()
        except Exception as error:
                print(f"Please answer y or n")
                print(error)
                return ask_user()
#Ask user if they want to put in a projected wage
def update():
        answerx = input(uname +", Do you want to input a projected wage? (y/n) ")
        try:
                if answerx.lower() == 'y':
                        return True
                elif answerx.lower() =='n':
                        return False
                else:
                        print(f"Invalid response")
                        return update()
        except Exception as error:
                print(f"Please answer y or n")
                print(error)
                return update()
#Ask user if they want to calculate weekly overtime
def calc():
        answery = input(uname +", Are you interested in finding out how much you could make per week with overtime? (y/n) ")
        try:
                if answery.lower() == 'y':
                        return True
                elif answery.lower() =='n':
                        return False
                else:
                        print(f"Invalid response")
                        return calc()
        except Exception as error:
                print(f"Please answer y or n")
                print(error)
                return calc()
#Ask user if they want to preform additional calulations , this will restart the loop until they answer no
def ans():
        answerz = input(uname + ", Do you want to perform another calculation? (y/n) ")
        try:
                if answerz.lower() == 'y':
                        return True
                elif answerz.lower() =='n':
                        return False
                else:
                        print(f"Invalid response")
                        return ans()
        except Exception as error:
                print(f"Please answer y or n")
                print(error)
                return ans()
#Ask user what they make per year
def currentsal():
    try:
        currentsalx=float(input("How much do you currently make per year? $")) #using float for partial hour
        return currentsalx
    except ValueError:
        print("Please enter a valid number")
        return currentsal()
#Ask user what they expect the new salary to be
def newsal():
    try:
        newsalx=float(input("What is the new salary? $"))
        return newsalx
    except ValueError:
        print("Please enter a valid number")
        return newsal()
#Ask user what their current wage is
def currentwa():
    try:
        currentx=float(input("What is your current wage? $"))
        return currentx
    except ValueError:
        print("Please enter a valid number")
        return currentwa()
#Ask user how many estimated hours they plan to work in a week
def worked():
    try:
        currentx=float(input("How many hours do you expect to work per week? "))
        return currentx
    except ValueError:
        print("Please enter a valid number")
        return worked()
#Ask user what their projected wage will be
def newwa():
    try:
        newx=float(input("What is your projected wage? $"))
        return newx
    except ValueError:
        print("Please enter a valid number")
        return newwa()
#Ask user what their projected wage will be
def hours():
    try:
        hoursx=float(input("How many hours do you project to work? Up to 40? ")) #using float for partial hour entry
        return hoursx
    except ValueError:
        print("Please enter a valid number")
        return hours()
def otx():
    try:
        oty=float(input("How many hours do you project to work over 40? "))
        return oty
    except ValueError:
        print("Please enter a valid number")
        return otx()
#Tax Rate Precentage
def tax():
    try:
        taxr=float(input("What is your local tax rate percentage? please input without the % sign"))
        return (taxr / 100) 
    except ValueError:
        print("Please enter a valid number")
        return tax()
#Local Area Tax Rate Calculation
def taxask():
    taxaskq = input(uname +", Would you like to input your current local tax rate? (y/n) ")
    try:
        if taxaskq.lower() == 'y':
            return tax()
        elif taxaskq.lower() =='n':
            return False
        else:
            print(f"Invalid response")
            return taxask()
    except Exception as error:
            print(f"Please answer y or n")
            print(error)
            return taxask()

while True: #loop start
    salary=ask_user()
    if salary==True:
        currentsalary=currentsal()
        newsalary=newsal()
        taxaskr=taxask()      
        grossdifference=(newsalary - currentsalary)
        weekly=round((newsalary/52),2)
        weekly=round((newsalary/52),2)
        weeklydif=round((grossdifference/52),2)
        biweekly=round((newsalary/26),2)
        biweekly=round((newsalary/26),2)
        biweeklydiff=round((grossdifference/26),2)
        difference=((newsalary / 2080)-(currentsalary / 2080)) 
        differencerounded=(round(difference,2))
        def sal_print():
                print(f"Your Current Hourly rage is$",currentsalary / 2080)
                print(f"Your Hourly pay difference is $",differencerounded) #output to user
                print(f"Your Estimated Weekly Pay Difference is $",weeklydif)
                print(f"Your Estimated Weekly Pay is $",weekly)
                print(f"Your Estimated Bi-Weekly Pay Difference is $",biweeklydiff)
                print(f"Your Estimated Bi Weekly Pay is $",biweekly)
                print(f"Your Estimated Gross pay Difference is $",grossdifference)
                print(f"Your Estimated Net Pay is $",(newsalary*(1 - taxaskr)))
        sal_print()
        ansy=ans()
        if(ansy==True): 
                continue
        else:
                thanks()
                break   
    else:
                currentwage=currentwa()
                houworked=worked()
                taxaskr=taxask()
                updatex=update()
                if updatex == True:
                        newwage=newwa()
                        grosswage=(((newwage * houworked) * 52) - ((currentwage * houworked) * 52))
                        grosswage=(((newwage * houworked) * 52) - ((currentwage * houworked) * 52))
                        wagediff=(newwage - currentwage)
                        wagediffround=(round(wagediff,2))
                        groround=(newwage * 2080)
                        biweround=(newwage * 80)
                        groround=(newwage * 2080)
                        biweround=(newwage * 80)
                        #print statements
                        def sal_print():
                                print("Your pay difference is $",wagediffround)
                                print("Your new Bi-Weekly Income is $",(round(biweround,2)))
                                print("Your new Gross Annual Income is $",(round(groround,2)))
                        def sal_print():
                                print("Your pay difference is $",wagediffround)
                                print("Your new Bi-Weekly Income is $",(round(biweround,2)))
                                print("Your new Gross Annual Income is $",(round(groround,2)))
                        calcx=calc()
                        if calcx == True:
                                hours=houworked
                                ot=otx()
                                otRate=newwage*1.5
                                pay=round(((newwage * hours)+(ot * otRate)),2) #calculations
                                binet=((pay * 2)*(1 - taxaskr)*2)
                                netan=((pay * 52) * (1 - taxaskr))
                                def sal_print():                                
                                        print("Your projected pay is $",pay,"for",hours+ot,"hours") #output to user
                                        print("Your projected Bi-Weekly pay is $",(pay * 2))
                                        print("Your projected Bi-Weekly Net is $",(round(binet,2)))
                                        print("Your projected Annual Gross is $",(pay * 52), "based off of working all 52 weeks")
                                        print("Your projected Annual Net is $",(round(netan,2)))
                        else:()
                else:
                        anround=(((currentwage * houworked)*52) * (1 - taxaskr))
                        bipayround=((currentwage * houworked)*2)
                        netround=(bipayround *(1 - taxaskr))
                        angro= ((currentwage * houworked)* 52)
                        def sal_print(): 
                                print("Your projected pay is $",(currentwage * houworked),"for",houworked,"hours") #output to user
                                print("Your Estimated Bi-Weekly pay is $",(round(bipayround,2)))
                                print("Your projected Bi-Weekly Net is $",(round(netround,2)))
                                print("Your Estimated Annual Gross is $",(round(angro,2)))   
                                print("Your Estimated Annual Net is $",(round(anround,2)))
                        calcx=calc()
                        if calcx == True:
                                hours=houworked
                                ot=otx()
                                otRate=currentwage*1.5
                                pay=((currentwage * hours)+(ot * otRate)) #calculations
                                netan=((pay * 52) * (1 - taxaskr))
                                binet=((pay * 2) * (1 - taxaskr))
                                def sal_print():                              
                                        print("Your projected pay is $",pay, "for",hours+ot, "hours") #output to user
                                        print("Your projected Bi-Weekly pay is $",(pay * 2))
                                        print("Your projected Bi-Weekly Net is $",(round(binet,2)))
                                        print("Your projected Annual Gross is $",(pay * 52), "based off of working all 52 weeks")
                                        print("Your projected Annual Net is $",(round(netan,2)))
                        else:()
                sal_print()
                ansx=ans()
            #check answer for continuation or exit
                if ansx == True: 
                        continue
                else:
                        thanks()
                        #Quit Calc
                        break
