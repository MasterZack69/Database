from numpy import random as r
import pandas as p

Player_Data = {
             "Players" : ["Takla","Toxic","Chain","Obhi"],
             "Level" : [r.randint(100),r.randint(100), r.randint(100),r.randint(100)],
             "Favorite Weapon" : ["Chamakta Takla","Toxic Gas","Chota Chakku","Thappad"]
}

print("       WEX Mobile's Sasta Database")
print (" ")
Data = p.DataFrame(Player_Data)
print(Data)