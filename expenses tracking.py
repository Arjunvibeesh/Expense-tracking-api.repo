import bcrypt
import matplotlib.pyplot as plt
from datetime import date,datetime
import os
from supabase import create_client
url='https://chctrmjuvctogplzojln.supabase.co'
key='sb_publishable_ARnKg_kZoRM6rFXixwQojQ_4_Ka4BFG'
s= create_client(url,key)
print('\n\n''--Please login (press "f" to login)' "\n"'--if your new please sign up (press "j" to sign up)''\n'"--In order to exit press 'k'"'\n\n')
def main():    
    def addx():
        w=input("\n\t"'Enter what all expenses you have (for eg:- electricty ,grocery etc ) ')
        e=w.split(',')
        for i in range(1,len(e)+1):
            c=float(input("\t"'enter the expense for '+e[i-1]+':- '))
            p=input("\t"'any note regarding this???..(optional):-  ')
            t=input("\t"'enter the date (format="yyyy-mm-dd"):- ')
            d={'user_id':x,'amount':c,'date':t,'description':p,'category':e[i-1].lower().strip()}
            s.table('expenses').insert(d).execute()
        print('******* THE EXPENSE WAS SUCCESSFULLY ADDED...!!! *******')
    def hash_password(password):
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return hashed.decode()
    def check_password(password, hashed_password):
        return bcrypt.checkpw(password.encode(),hashed_password.encode())
    def viewcat(user_id, category):
        go=s.table("expenses").select("amount, description, date, category").eq("user_id", user_id).eq("category", category).execute()
        for e in go.data:
            print("\n\t"'For '+e['category'].capitalize()+"\n\t\t"'Amount:- Rs'+str(e['amount'])+"\n\t\t"'Date:- '+str(e['date'])+"\n\t\t"'Description:- '+e['description'])
    def viewdate(user_id, start, end):
        response = (s.table("expenses").select("amount, description, date, category").eq("user_id", user_id).gte("date", start).lte("date", end).execute())
        for e in response.data:
            print("\n\t"'For '+e['category'].capitalize()+"\n\t\t"'Amount:- Rs'+str(e['amount'])+"\n\t\t"'Date:- '+str(e['date'])+"\n\t\t"'Description:- '+e['description'])
    def view():
        response =s.table("expenses").select("amount, description, date, category").eq("user_id", x).order("date", desc=True).execute()
        if not response.data:
            print("\n******* No expenses found*******")
            return
        print("\n------- YOUR EXPENSES -------")
        for e in response.data:
            print("\n\t"'For '+e['category'].capitalize()+"\n\t\t"'Amount:- Rs'+str(e['amount'])+"\n\t\t"'Date:- '+str(e['date'])+"\n\t\t"'Description:- '+e['description'])
        while True:
            p=input("\n"'Press "c" if you want to display the specific category'"\n"'Press "d" if you want to display expenses within a range of dates'"\n"'Or press "e" to exit:-  ')
            if p.upper()=='C':
                cat=input("\n\t"'Enter that category:- ').lower()
                viewcat(x,cat)
            elif p.upper()=='D':
                start=input("\n"'Enter the starting date(yyyy-mm-dd):- ')
                end=input('Enter the ending date(yyy-mm-dd):- ')
                viewdate(x,start,end)
            elif p.upper()=='E':
                break
            else:
                print('Invalid choice......')
    def modify(user_id):
        cate = input("\nEnter the category which needs to be updated:- ").strip().lower()
        datem= input("Enter date of the expense to modify:- ").strip()
        check = (s.table("expenses").select("*").eq("date", datem).eq("user_id", user_id).execute())
        if not check.data:
            print("*******No expense found with this ID .....!!!*******")
            return
        amount = float(input("\n Enter the New amount:- "))
        desc = input("New description:- ")
        raw_date = input("New date (YYYY-MM-DD):- ")
        s.table("expenses").update({"category": cate,"amount": amount,"description": desc,"date": raw_date}).eq("category", cate).eq("date", datem).execute()
        print("******* EXPENSE UPDATED SUCCESSFULLY......!!!! *******")

    def delete(user_id):
        try:
            cate = input("\nEnter which category to delete: ").strip().lower()
            datem = input("Enter the date of expense (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(datem, "%Y-%m-%n").date().isoformat()
            except ValueError:
                print("\n Invalid date format. Use YYYY-MM-DD\n")
                return
            start = datem + "T00:00:00"
            end = datem + "T23:59:59"
            check = (s.table("expenses").select("*").eq("category", cate).eq("user_id", user_id).gte("date", start).lte("date", end).execute())
            if not check.data:
                check = (s.table("expenses").select("*").eq("category", cate).eq("user_id", user_id).eq("date", datem).execute())
            if not check.data:
                all_exp = (s.table("expenses").select("*").eq("category", cate).eq("user_id", user_id).execute())
                check.data = [exp for exp in all_exp.data if str(exp["date"]).startswith(datem)]
            if not check.data:
                print("\n******* NO MATCHING EXPENSE FOUND *******")
                return
            print("\n------- MATCHING EXPENSES TO DELETE -------")
            for i, exp in enumerate(check.data, 1):
                print(f"\n{i}. Category: {exp['category'].capitalize()}")
                print(f"   Amount: ₹{exp['amount']}")
                print(f"   Date: {exp['date']}")
                print(f"   Description: {exp['description']}")
            confirm = input("\nAre you sure you want to delete? (Y/N): ").upper()
            if confirm != "Y":
                print("\n******* DELETION CANCELLED *******")
                return
            result = (s.table("expenses").delete().eq("category", cate).eq("user_id", user_id).gte("date", start).lte("date", end).execute())
            if result.data:
                print(f"\n{len(result.data)} EXPENSE(S) DELETED SUCCESSFULLY")
                return
            deleted = 0
            for exp in check.data:
                s.table("expenses").delete() \
                    .eq("category", cate) \
                    .eq("user_id", user_id) \
                    .eq("date", str(exp["date"])) \
                    .eq("amount", exp["amount"]) \
                    .execute()
                deleted += 1

            if deleted:
                print(f"\n{deleted} EXPENSE(S) DELETED SUCCESSFULLY")
            else:
                print("\n FAILED TO DELETE EXPENSE(S)")

        except Exception as e:
            print("\n6 RUNTIME ERROR OCCURRED")
            print("Error:", e)


            
    def monran(year, month):
        start = date(year, month, 1)
        if month == 12:
            end = date(year + 1, 1, 1)
        else:
            end = date(year, month + 1, 1)
        return start, end
    def monsum(user_id):
        year = int(input("\nEnter year (YYYY): "))
        month = int(input("Enter month (1-12): "))
        start, end = monran(year, month)
        response = (s.table("expenses").select("amount, category, date").eq("user_id", user_id).gte("date", str(start)).lt("date", str(end)).execute())
        if not response.data:
            print("No expenses found for this month")
            return
        total = 0
        daily_total = {}
        category_total = {}
        for e in response.data:
            total += e["amount"]
            category_total[e["category"]] = category_total.get(e["category"], 0) + e["amount"]
            day = e["date"]
            daily_total[day] = daily_total.get(day, 0) + e["amount"]
        print(f"\n------- MONTHLY SUMMARY ({month}/{year}) -------")
        print(f"\tTotal Spent: ₹{total}")
        print(f"\tNumber of Expenses: {len(response.data)}")
        print("\n------- CATEGORY-WISE EXPENSES:-------")
        for cat, amt in category_total.items():
            print(f"\t{cat}: ₹{amt}")
        respons = (s.table("expenses").select("*").eq("user_id", user_id).order("amount", desc=True).limit(1).execute())
        e = respons.data[0]
        print("\n\n--- Highest Expense recorded ---")
        print(f"Amount      : ₹{e['amount']}")
        print(f"Category    : {e['category']}")
        print(f"Date        : {e['date']}")
        print(f"Description : {e['description']}")
        category_bar_chart(category_total)
        category_pie_chart(category_total)
        daily_line_chart(daily_total)
    def category_bar_chart(category_total):
        categories = list(category_total.keys())
        amounts = list(category_total.values())
        plt.figure()
        plt.bar(categories, amounts)
        plt.xlabel("Category")
        plt.ylabel("Amount Spent")
        plt.title("Category-wise Monthly Expense")
        plt.show()
    def category_pie_chart(category_total):
        plt.figure()
        plt.pie(category_total.values(),labels=category_total.keys(),autopct="%1.1f%%")
        plt.title("Expense Distribution by Category")
        plt.show()
    def daily_line_chart(daily_total):
        dates = list(daily_total.keys())
        amounts = list(daily_total.values())
        plt.figure()
        plt.plot(dates, amounts, marker="o")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.title("Daily Expense Trend")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    def ask_continue():
        q = input("Do you want to continue (yes or no): ").strip().lower()
        if q == "no":
            return False
        elif q == "yes":
            return True
        else:
            print("Invalid choice, returning to menu.")
            return True
    while True:
        n=input("\n\t\t"'Enter your choice (login(f) , sign up(j) or exit(k)):- ')
        if n.upper()=="F":
            print("\n\n"'******* YOU WISH TO LOGIN *******''\n')
            x=int(input("\t"'Enter your user id:- '))
            y=input("\t"'Enter your name:- ').strip()
            v=input("\t"'Enter the password:- ')
            r= s.table("users").select("*").eq("username", y).execute()
            if not r.data:
                print("\n\t\t"'++ Invalid credinitials.....'"\n\t\t"'Try again.... ++'"\n")
            else:
                stored_hash = r.data[0]["password"]
                if check_password(v, stored_hash):
                    print("\n"'******* LOGIN SUCCESSFULL....!!!! *******'"\n\n")
                else:
                    print('\n\t'"Invalid password......!!"'\n')
                    pass
                while True:
                    print('\nWhat would you like to perform....????'"\n")
                    print('1.) Add a new expense record\n2.) View stored expenses\n3.) Modify existing expenses\n4.) Delete an expense\n5.) Show monthly summary\n6.) Exit')
                
                    try:
                        a = int(input("\n"'Enter your choice:- '))
                    except ValueError:
                        print("Invalid input. Enter a number.")
                        continue
                    if a == 1:
                        addx()
                        if not ask_continue():
                            break
                    elif a == 2:
                        view()
                        if not ask_continue():
                            break
                    elif a == 3:
                        modify(x)
                        if not ask_continue():
                            break
                    elif a == 4:
                        delete(x)
                        if not ask_continue():
                            break
                    elif a == 5:
                        monsum(x)
                        if not ask_continue():
                            break
                    elif a == 6:
                        print('\n\t'"-------EXITING PROGRAM.....!!!-------"'\n')
                        break
                    else:
                        print('\n'"******* Invalid choice.....Choose between 1–6 *******"'\n')
        elif n.upper()=='J':
            print("\n"'******** YOU WISH TO SIGN UP *******''\n')
            a=int(input("\t"'Enter your id:- '))
            b=input("\t"'Enter you name:- ')
            j=input("\t"'Enter your password:- ')
            hashed_password = hash_password(j)
            d={'id':a,'username':b,'password':hashed_password}
            s.table('users').insert(d).execute()
            print("\n"'******* SUCCESSFULLY SIGNED UP......!!!! *******'"\n\n")
        elif n.upper()=='K':
            print("\n\n\t\t\t\t\t\t"'----------------- THANK YOU.....!!!! -----------------')
            break
        else:
            print("\n"'******* Invalid choice (Press "f" or "j" OR "k")*******'"\n")
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting safely....!!!")
    except Exception as e:
        print("\nSomething went wrong. Please try again.")
        with open("error.log", "a") as f:
            f.write(f"{datetime.now()} | {str(e)}\n")


