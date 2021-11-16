from inscUser import InscUser
from datetime import date
from datetime import datetime

today = date.today()
if today.day<=(9):
    strtr = "0{}.{}.{}".format(today.day,today.month,today.year)
else:
    strtr = "{}.{}.{}".format(today.day,today.month,today.year)
jour = datetime.now()


mardiheure1 ="12:15–13:45"#Pas touche
mardiheure2 ="21:00–22:30"#Pas touche

users = [
    {
        "login": "hakimdao",
        "pwd": "Se2E3abUg",
    },
    {
        "login": "NGOQUANG",
        "pwd": "x2bznimo",
    },
    {
        "login": "RAMIRAYA",
        "pwd": "YqyDaNELa",
    },
    {
        "login": "jaidigha",
        "pwd": "Zara-2stra2019",
    },
]

if (jour.strftime("%A")) == "Tuesday":
    for user in users:
        user["dates"] = [
            {
                "heure": mardiheure1,
                "dt": strtr
            },
            {
                "heure": mardiheure2,
                "dt": strtr
            },
        ]
elif (jour.strftime("%A")) == "Wednesday":
    users = [
        {
            "login": "hakimdao",
            "pwd": "Se2E3abUg",
            "dates": [
                {
                    "heure": "",
                    "dt": "",
                }
            ],
            "mercredi": True
        },
    ]
else:
    for user in users:
        user["dates"] = None


print(datetime.now().strftime("[%d/%m/%Y %H:%M:%S]") + " Running sports.unil.bot...")

for user in users:
    print("User " + user["login"] + "...")
    InscUser(user)

print(datetime.now().strftime("[%d/%m/%Y %H:%M:%S]") + " Successfully ran sports.unil.bot")
