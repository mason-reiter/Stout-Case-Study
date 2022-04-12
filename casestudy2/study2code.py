import csv
import matplotlib.pyplot as plt
import numpy as np


def import_file(save_to_file=False):
    with open('data/casestudy.csv', newline='') as input:
        reader = csv.reader(input)
        reader.__next__()
        output = []
        for row in reader:
            output += [row]
        print("Input file loaded with",len(output),"rows")
        return output

#Idea: Just print duplicate emails instead of returning so you get them all
def duplicate_emails(file):
    emails={}
    for row in file:
        if row[1] in emails and row[3]==emails[row[1]]:
            return ''+row[1]+' is a duplicate email'
        else:
            emails[row[1]]=row[3]
    return 'There are no duplicate emails'

def total_customers(file,current_year):
    total=0
    for row in file:
        year=int(row[3])
        if year==current_year:
            total+=1
    return total

def new_customers(file, current_year):
    prev_customers = {}
    current_customers = {}
    for row in file:
        email, revenue, year = (row[1], float(row[2]), int(row[3]))
        # print(type(year), current_year-1)
        if year == current_year - 1:
            prev_customers[email] = revenue
        elif year == current_year:
            current_customers[email] = revenue
    for email in prev_customers:
        current_customers.pop(email, None)
    return current_customers

def lost_customers(file,current_year):
    prev_customers={}
    kept_customers={}
    for row in file:
        email, revenue, year =(row[1], float(row[2]), int(row[3]))
        #print(type(year), current_year-1)
        if year==current_year-1:
            prev_customers[email]=revenue
        elif year==current_year and email in prev_customers:
            kept_customers[email]=revenue
    for email in kept_customers:
        prev_customers.pop(email,None)
    return prev_customers

    #print(len(prev_customers),len(kept_customers))
    #print("ajfzujupln@gmail.com" in prev_customers)

def total_revenue(file, current_year):
    total=0
    for row in file:
        revenue, year=(float(row[2]), int(row[3]))
        if year==current_year:
            total+=revenue
    return round(total,2)

def new_customer_revenue(file, current_year):
    prev_customers = {}
    total=0
    for row in file:
        email, revenue, year =(row[1], float(row[2]), int(row[3]))
        if year==current_year-1:
            prev_customers[email]=0
        elif year==current_year and email not in prev_customers:
            total+=revenue
    return round(total,2)

def existing_customer_revenue(file, current_year):
    prev_customers = {}
    total = 0
    for row in file:
        email, revenue, year = (row[1], float(row[2]), int(row[3]))
        if year == current_year - 1:
            prev_customers[email] = 0
        elif year == current_year and email in prev_customers:
            total += revenue
    return round(total, 2)

def existing_customer_growth(file,current_year):
    prev_customers={}
    kept_customers={}
    for row in file:
        email, revenue, year =(row[1], float(row[2]), int(row[3]))
        #print(type(year), current_year-1)
        if year==current_year-1:
            prev_customers[email]=revenue
        elif year==current_year and email in prev_customers:
            kept_customers[email]=revenue
    growth=0
    for email in kept_customers:
        growth+=prev_customers[email]-kept_customers[email]
    #print(len(prev_customers),len(kept_customers))
    #print("ajfzujupln@gmail.com" in prev_customers)
    return round(growth,2)

def revenue_lost_attrition(file, current_year):
    lc_dict=lost_customers(file,current_year)
    total=0
    for email in lc_dict:
        total+=lc_dict[email]
    return round(total,2)

def make_scatterplot_graph(file):
    revenues_list=[{}]
    init_year=int(file[0][3])
    dict_index=0
    for i in range(0,len(file)):
        row=file[i]
        revenue, year = (float(row[2]), int(row[3]))
        revenue=round(revenue,0)
        if year==init_year:
            if revenue in revenues_list[dict_index]:
                revenues_list[dict_index][revenue]+=1
            else:
                revenues_list[dict_index][revenue]= 1
        else:
            dict_index+=1
            init_year=year
            revenues_list+=[{revenue:1}]
    x=[]
    y=[]
    colors=[]
    for item in revenues_list[0]:
        x+=[item]
        y+=[revenues_list[0][item]]
        colors+=[(0,0,1)]
    for item in revenues_list[1]:
        x+=[item]
        y+=[revenues_list[1][item]]
        colors+=[(1,0,1)]
    for item in revenues_list[2]:
        x+=[item]
        y+=[revenues_list[2][item]]
        colors+=[(0,0.8,0.3)]

    import matplotlib.patches as mpatches
    plt.scatter(x,y,c=colors, s=10)
    pop_a = mpatches.Patch(color=(0,0,1), label='2015')
    pop_b = mpatches.Patch(color=(1,0,1), label='2016')
    pop_c = mpatches.Patch(color=(0,0.8,0.3), label='2017')

    plt.legend(handles=[pop_a, pop_b, pop_c], loc="upper right")
    plt.title("Number of Orders for each Net Revenue Per Year")
    plt.xlabel("Net Revenue (rounded to nearest integer)")
    plt.ylabel("Number of Orderg")
    plt.show()

def make_bar_graph(file):
    y=[]
    years=["2015","2016","2017"]
    for year in years:
        year=int(year)
        print(new_customer_revenue(file,year)/len(new_customers(file,year)))
        y+=[new_customer_revenue(file,year)/len(new_customers(file,year))]
    plt.bar(years,y)
    plt.xlabel("Year")
    plt.ylabel("Average New Customer Revenue")
    plt.title("Average New Customer Revenue per Year")
    plt.show()

if __name__ == "__main__":
    file = import_file()
    print(file[2])
    print(duplicate_emails(file))
    print([1,2,3,4])
    print((2*np.array([1,2,3,4])).tolist())
    year=2016
    '''
    print("You made", total_revenue(file,year),"bucks this year")
    print("You made", new_customer_revenue(file, year),"bucks from new customers this year")
    print("You made", existing_customer_growth(file,year),"bucks from existing customer growth this year")
    print("You lost", revenue_lost_attrition(file, year),"bucks from attrition this year")
    print("You had",  total_customers(file,year-1),"total customers last year")
    print("You have", total_customers(file, year),"total customers this year")
    print("You made", existing_customer_revenue(file,year),"from existing customers this year")
    print("You made", existing_customer_revenue(file, year-1), "from existing customers last year")
    print("You have", len(new_customers(file, year)),"new customers this year")
    print("You lost", len(lost_customers(file,year)),"customers from last year")
    '''
    #make_scatterplot_graph(file)
    make_bar_graph(file)

