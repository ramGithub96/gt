from sys import stdin

def defBill(consum,ratio):
    n=int(consum/(sum(ratio)))
    basicBillAmount=(ratio[0]*n)+(ratio[1]*n*1.5)
    return int(basicBillAmount)

def guestConsumption(guests):
    addconsum=guests*300
    finalBillAmount=0
    if(addconsum>0 and addconsum<=500):
        finalBillAmount+=(addconsum*2)
    elif(addconsum>500 and addconsum<=1500):
        finalBillAmount=finalBillAmount+1000+((addconsum-500)*3)
    elif(addconsum>1500 and addconsum<=3000):
        finalBillAmount+=(4000+((addconsum-1500)*5))
    else:
        finalBillAmount+=8500+((addconsum-3000)*8)

    return finalBillAmount,addconsum

if __name__ == "__main__":

  lines=stdin.read().splitlines()
  consumption=0 
  finalBillAmount=0
  guests=0
  bill=0
  for i in lines:
    query=i.split()
    j=query[0]
    if(j=="ALLOT_WATER"):
       if(query[1],query[2]):      
            bhk=int(query[1])
            ratio=list(map(int,query[2].split(":")))
            if(bhk==2):
                consumption=900
                finalBillAmount=(defBill(consumption,ratio))
            elif(bhk==3):
                consumption=1500
                finalBillAmount=(defBill(consumption,ratio))
            else:
                print("WRONG INPUT")

    elif(j=="ADD_GUESTS" ):
        if(len(query)==2):
            guests+=int(query[1])
        else:
            print("Please enter number of guests")
    elif(j=="BILL"):
        if(guests):
            addBill,addconsum=guestConsumption(guests)
            finalBillAmount+=addBill
            consumption+=addconsum
            print(consumption,finalBillAmount)
        else:
            print(consumption,finalBillAmount)
    else:
        print("ENTER PROPER QUERY")
