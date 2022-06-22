from flask import Flask, render_template
import random



app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    list1 = []
    for i in range(15):
        data_generated = get_details()
        list1.append(data_generated)
    return render_template("index.html", data = list1[::-1])

def absolute_sum(val):
        val = str(val)
        while len(val)!=1:
            val = list(val)
            val = [int(i) for i in val]
            val = sum(val)
            val = str(val)
        return int(val)

def generate_valid_card():
        flag=0
        while flag==0:
            cc_number = f"{random.randint(0000,9999):04} {random.randint(0000,9999):04} {random.randint(0000,9999):04} {random.randint(0000,9999):04}"
            card_number = cc_number.replace(" ","")
            part1 = list(card_number[-1::-2])
            part2 = list(card_number[-2::-2])
            part1 = [int(i) for i in part1]
            part2 = [2*int(i) for i in part2]
            part2 = [absolute_sum(i) for i in part2]
            sum_val = sum(part1)+sum(part2)
            if sum_val%10==0:
                flag=1
            else:
                pass
        return cc_number


def get_details():
        f_names = ["Suresh", "Ramesh", "Boman", "Rahul", "Devdut", "Somya", "Shakira", "Mahesh", "Ram", "Kartik", "Gaurav"]
        l_names = ["Singh", "Bano", "Singhania", "Patel", "Raghuvanshi", "Shankar", "Pandit", "Malone", "Mohan", "Selevam"]
        name = random.choice(f_names)+" "+random.choice(l_names)
        email = name.lower().replace(" ","_")+"@email.com"
        contact = f"{random.randint(000,999):03}-{random.randint(000,999):03}-{random.randint(0000,9999):04}"
        credit_card = generate_valid_card()
        data_dict = {
            "name": name,
            "email": email,
            "contact": contact,
            "card_number": credit_card
        }

        return data_dict
    



if __name__ == "__main__":
    app.run()
    
