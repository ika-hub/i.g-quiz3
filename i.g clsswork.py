#ი.გ qz3
import requests
import json
import sqlite3


#არტისტის ან ჯგუფის შესახებ ინგფორმაცია
artist = input("შიყვანეთ მომღერალი ან ჯგუფი")
url = "https://api.deezer.com/search"
payload = {"q" : "eminem"} #input-ს არ მაკეთებინებს და ამიტომ კონკრეტული ჩავწერე
r = requests.get(url, payload)
res = json.loads(r.text)
# print(json.dumps(res, indent=4))
print("მომღერლის შესახებ: ", res['data'])

###

s_payload = {'track/{"track_id"}'}
track_id = input("შეიყვანეთ რიცხვი")
s = requests.post('https://api.deezer.com/post', data=s_payload)
print(s.text)


#Json ფაილის შენახვა
with open("data.json", 'w') as f:
    json.dump(res, f, indent=4)


# # სტატუს კოდი და ჰედერი
print(f'სტატუს კოდი: {r.status_code}\n')
print(f'ინფორმაციის ტიპი: {r.headers}\n')
result = json.loads(r.text)
print(json.dumps(result, indent=4))



# ცხრილის გაკეთება
conn = sqlite3.connect('artist.sqlite')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE artist
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 rank INTEGER,
                 title VARCHAR(50),    
                 duration INTEGER
                 )
''')
conn.commit()

