from flask import Flask, render_template, request, redirect
import random
app = Flask(__name__)



@app.route('/', methods=['GET'])
def dropdown():
    sizes = ['3x3', '4x4', '5x5']
    return render_template('form.html', sizes=sizes)

@app.route('/card', methods=['POST'])
def card():
    list = ["Jack Crawford", "Molly Graham", "Abigail Hobbs", "Frederick Chilton", "Freddie Lounds", "Bella Crawford", "Beverly Katz", "Bedelia Du Maurier", "Brian Zeller", "Jimmy Price", "Reba McClane", "Francis Dolarhyde", "Chiyoh", "Rinaldo Pazzi", "Georgia Madchen", "Garett Jacob Hobbs", "Alana Bloom", "Margot Verger", "Cordell Doemling", "Abel Gideon", "Mason Verger", "Kade Prurnell", "Tobias Budge", "Eliot Buddish", "Donald Sutcliffe", "Franklyn Froideveaux", "Mrs. Komeda", "Miriam Lass", "Matthew Brown", "Anthony Dimmond"]

    card = []
    dropdownval = request.form['size']

    if dropdownval == '3x3':
        numbers = random.sample(range(30), 9)
        for num in numbers:
            card.append(list[num])
        if request.form.get('free_space'):
            card[4] = "Hannibal Lecter Free Space"
        else:
            pass

    elif dropdownval == '4x4':
        numbers = random.sample(range(30), 16)
        for num in numbers:
            card.append(list[num])
        if request.form.get('free_space'):
            card[5] = "Hannibal Lecter Free Space"
        else:
            pass

    elif dropdownval == '5x5':
        numbers = random.sample(range(30), 25)
        for num in numbers:
            card.append(list[num])
        if request.form.get('free_space'):
            card[12] = "Hannibal Lecter Free Space"
        else:
            pass


    return render_template("card.html", card=card, length=len(card))


if __name__ == "__main__":
    app.run()

