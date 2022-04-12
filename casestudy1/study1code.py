import csv
import numpy as np
import matplotlib.pyplot as plt


def import_file(save_to_file=False):
    with open('data/loans_full_schema.csv', newline='') as input:
        reader = csv.reader(input)
        reader.__next__()
        output = []
        for row in reader:
            output += [row]
        return output


def import_labels(file='data/loans_full_schema.csv'):
    with open(file, newline='') as input:
        reader = csv.reader(input)
        return reader.__next__()
        # return output


def most_common_job(file):
    num_titles = {}
    for row in file:
        if row[0] in num_titles:
            num_titles[row[0]] += 1
        else:
            num_titles[row[0]] = 1
    max_num = 0
    title = "lmao nojobs"
    for job_title in num_titles:
        if num_titles[job_title] > max_num and job_title != '':
            max_num = num_titles[job_title]
            title = job_title
    return title, max_num


def make_feature_set(file):
    x = []
    y = []
    emp_title = {}
    state = {}
    loan_purpose={}

    for row in file:
        # emp_title
        if row[0] not in emp_title:
            emp_title[row[0]] = len(emp_title)
        row[0] = emp_title[row[0]]
        # emp_length
        if row[1] == "NA":
            row[1] = 0
        row[1] = int(row[1])
        # state
        if row[2] not in state:
            state[row[2]] = len(state)
        row[2] = state[row[2]]
        # homeownership
        if row[3] == "MORTGAGE":
            row[3] = 0
        elif row[3] == "OWN":
            row[3] = 1
        else:
            row[3] = 2
        # annual_income
        if row[4]=="NA":
            row[4]=0
        row[4] = float(row[4])
        # verified_income
        if row[5] == "Verified":
            row[5] = 0
        elif row[5] == "Not Verified":
            row[5] = 1
        else:
            row[5] = 2
        # annual_income_joint
        if row[7] == "NA":
            row[7] = 0
        row[7] = float(row[7])
        # verification_income_joint
        if row[8] == "Verified":
            row[8] = 0
        elif row[8] == "Not Verified":
            row[8] = 1
        elif row[8] == "Source Verified":
            row[8] = 2
        else:
            row[8] = 3
        # debt_to_income_joint
        if row[9] == "NA":
            row[9] = 0
        row[9] = float(row[9])
        #delinq_2y
        row[10]=float(row[10])
        #months_since_last_delinq
        if row[11] == "NA":
            row[11] = 200.0
        row[11]=float(row[11])
        #earliest_credit_line
        row[12]=float(row[12])
        #inquiries_last_12m
        row[13]=float(row[13])
        #total_credit_lines
        row[14] = float(row[14])
        # open_credit_lines
        row[15] = float(row[15])
        # total_credit_limit
        row[16] = float(row[16])
        # total_credit_utilized
        row[17] = float(row[17])
        # num_collections_last_12m
        row[18] = float(row[18])
        # num_historical_failed_to_pay
        row[19] = float(row[19])
        # months_since_90d_late
        if row[20]=="NA":
            row[20]=200.0
        row[20]=float(row[20])
        # current_accounts_delinq
            #row[21]
        # total_collection_amount_ever
        row[22]=float(row[22])
        # current_installment_accounts
        row[23]=float(row[23])
        # accounts_opened_24m
        row[24] = float(row[24])
        # months_since_last_credit_inquiry
        if row[25]=="NA":
            row[25]=200.0
        row[25]=float(row[25])
        # num_satisfactory_accounts
        row[26] = float(row[26])
        # num_accounts_120d_past_due
            #row[27]
        # num_accounts_30d_past_due
            #row[28]
        # num_active_debit_accounts
        row[29] = float(row[29])
        # total_debit_limit
        row[30] = float(row[30])
        # num_total_cc_accounts
        row[31] = float(row[31])
        # num_open_cc_accounts
        row[32] = float(row[32])
        # num_cc_carrying_balance
        row[33] = float(row[33])
        # num_mort_accounts
        row[34] = float(row[34])
        # account_never_delinq_percent
        row[35]=float(row[35])
        # tax_liens
        row[36]=float(row[36])
        # public_record_bankrupt
        row[37]=float(row[37])
        # loan_purpose
        if row[38] not in loan_purpose:
            loan_purpose[row[38]]=len(loan_purpose)
        row[38]=loan_purpose[row[38]]
        # application_type
        if row[39]=="individual":
            row[39]=0
        else:
            row[39]=1
        # loan_amount
        row[40]=float(row[40])
        # term
        row[41]=float(row[41])
        # interest_rate
        # installment
        # grade
        # sub_grade
        # issue_month
        # loan_status
        # initial_listing_status
        # disbursement_method
        # balance
        # paid_total
        # paid_principal
        # paid_interest
        # paid_late_fees
        '''
        REMEMBER TO REMOVE COLUMNS BY ONLY ADDING PART OF THE ROW
        '''
        x += [row[0:21]+row[22:27]+row[29:42]]
        y += [float(row[42])]
    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j] == "NA":
                x[i][j] = 0
            x[i][j] = float(x[i][j])
    return (x,y)

def linear_regression(x,y):
    return np.linalg.lstsq(x,y)[0]

def make_neural_network(x,y):
    y2=[]
    for i in y:
        y2+=[[i]]
    x=np.array(x)
    y=np.array(y2)
    model=Sequential
    model.add(Input(shape=39))
    model.add(Dense(60))
    model.add(Dense(1))
    model.compile(loss="mean squared error", optimizer="sgd", metrics=["accuracy"])
    model.summary()


def make_graph1(file):
    x = [0, 1, 2]
    y_1 = []
    y_2 = []
    y_3 = []
    for row in file:
        verified_income = row[5]
        interest_rate = float(row[42])
        # print(interest_rate)
        if verified_income == "Not Verified":
            y_1 += [interest_rate]
        elif verified_income == "Verified":
            y_2 += [interest_rate]
        else:
            y_3 += [interest_rate]
    y = [np.mean(y_1), np.mean(y_2), np.mean(y_3)]
    plt.bar(x, y, tick_label=["Not Verified", "Verified", "Source Verified"])
    plt.ylabel("Average Interest Rate")
    plt.title("Income Verification Status vs Average Interest Rate")
    plt.show()


def make_graph2(file):
    x = []
    y = []
    for row in file:
        sub_grade = row[45]
        interest_rate = float(row[42])
        num_grade = 100 + 10 * (65 - ord(sub_grade[0])) + 2 * (1 - int(sub_grade[1]))
        if num_grade <= 68 and interest_rate < 10:
            print(sub_grade, interest_rate)
        x += [num_grade]
        y += [interest_rate]
    plt.scatter(x, y)
    plt.xlabel("Numerical Loan Subgrade")
    plt.ylabel("Interest Rate")
    plt.title("Interest Rate vs Subgrade")
    plt.show()


def make_graph3(file):
    x = [0, 0]
    for row in file:
        current_accounts_delinq = int(row[21])
        if current_accounts_delinq == 0:
            x[0] += 1
        else:
            x[1] += 1
    plt.pie(x, labels=["0", "1"], autopct='%1.2f%%')
    plt.title("Number of Current Delinquent Accounts")
    plt.show()


def make_graph4(file):
    # find another variable that moderately coincides with interest rate
    # idea: annual_income_joint to see if working with moderately difficult data is worth it
    x0 = 0
    num_x0 = 0
    x = []
    y = []
    for row in file:
        annual_income_joint = row[7]
        interest_rate = float(row[42])
        if annual_income_joint == "NA":
            x0 = (x0 * num_x0 + interest_rate) / (num_x0 + 1)
            num_x0 += 1
        else:
            x += [float(annual_income_joint)]
            y += [interest_rate]
    plt.scatter([0], [x0], color=(1, 0, 0), label="Avg. interest rate without joint income")
    plt.scatter([0], [np.mean(y)], color=(0, 0.8, 0), label="Avg. interest rate with joint income")
    print(len(y))
    plt.scatter(x, y, s=8)
    plt.xlabel("Joint annual income")
    plt.ylabel("Interest rate")
    plt.title("Joint Annual Income vs Interest Rate")
    plt.legend()
    plt.show()


def make_graph5(file):
    x_dict = {}
    x = []
    y = []
    for row in file:
        loan_purpose = row[38]
        interest_rate = float(row[42])
        if loan_purpose in x_dict:
            x_dict[loan_purpose] += [interest_rate]
        else:
            x_dict[loan_purpose] = [interest_rate]
    for loan_purpose in x_dict:
        x += [loan_purpose.replace("_", "\n")]
        y += [np.mean(x_dict[loan_purpose])]

    plt.bar(x, y)
    plt.ylabel("Interest rate")
    plt.title("Loan purpose vs interest rate")
    plt.show()


def make_results_1(feature_set,y,model):
    x=[]
    y1=[]
    for row in feature_set:
        y1+=[row @ model]
        x+=[row[6]]
    plt.scatter(x,y,color=(0,0.8,0), label="Actual")
    plt.scatter(x,y1,color=(0.8,0,0), label="Predicted")
    plt.title("Model interest rate vs actual interest rate")
    plt.xlabel("Debt to income ratio")
    plt.ylabel("Interest Rate")
    plt.legend()
    plt.show()






if __name__ == "__main__":
    file = import_file()
    labels = import_labels()
    print(file[2])
    print(most_common_job(file))
    # make_graph1(file)
    # make_graph2(file)
    # make_graph3(file)
    # make_graph4(file)
    # make_graph5(file)
    x,y = make_feature_set(file)
    #print(x[0],len(x[0]),y[0])
    #print(len(x),len(x[0]),len(np.transpose(y)))
    #model1=linear_regression(x,y)
    print(len(y), len(x[0]))
    make_neural_network(x,y)
    '''
    model2=make_neural_network(x,y)
    model2.predict(x[0])
    '''
    plt.plot(error)
    plt.show()
    #make_results_1(x,y,model1)
