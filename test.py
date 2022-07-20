'''[
    {
        "label": "Primary Surgeon",
        "backgroundColor": "#398AB9",
        "data": [14, 3, 1, 7, 5, 1, 11, 3, 4, 2, 1, 1, 0, 0, 1, 1, 0, 0, 3, 0, 0],
    },
    {
        "label": "First Assist",
        "backgroundColor": "#D8D2CB",
        "data": [29, 14, 3, 5, 3, 6, 3, 2, 6, 7, 3, 3, 3, 3, 3, 3, 3, 1, 0, 1, 0],
    },
    {
        "label": "Secondary Assist",
        "backgroundColor": "#1A374D",
        "data": [13, 36, 28, 18, 11, 10, 3, 8, 0, 0, 4, 2, 2, 2, 0, 0, 0, 2, 0, 1, 1],
    },
]
'''




data = {

    "Secondary Assist": {
        "Trauma": 25,
        "Arthroplasty": 107,
        "Pediatrics": 1,
        "Sports": 6,
        "Foot and Ankle": 2,
    },
    "First Assist": {
        "Trauma": 27,
        "Upper Extremity": 6,
        "Arthroplasty": 58,
        "Pediatrics": 6,
        "Sports": 3,
        "General": 1,
    },
    "Primary Surgeon": {
        "Arthroplasty": 33,
        "Trauma": 20,
        "Pediatrics": 4,
        "General": 1,
    },
}
get_data = []
for key, value in data.items():
    dat = {
        "Trauma": value.get("Trauma",0),
        "Arthroplasty": value.get("Arthroplasty",0),
        "Pediatrics": value.get("Pediatrics",0),
        "Sports": value.get("Sports",0),
        "Foot and Ankle": value.get("Foot and Ankle",0),
        "Upper Extremity": value.get("Upper Extremity",0),
        "General": value.get("General",0),
    }
    get_data.append(dat)
    
get_data = [
    {
        "label": "Secondary Assist",
        "Trauma": 25,
        "Arthroplasty": 107,
        "Pediatrics": 1,
        "Sports": 6,
        "Foot and Ankle": 2,
        "Upper Extremity": 0,
        "General": 0,
    },
    {
        "label": "First Assist",
        "Trauma": 27,
        "Arthroplasty": 58,
        "Pediatrics": 6,
        "Sports": 3,
        "Foot and Ankle": 0,
        "Upper Extremity": 6,
        "General": 1,
    },
    {
        "label": "Primary Surgeon",
        "Trauma": 20,
        "Arthroplasty": 33,
        "Pediatrics": 4,
        "Sports": 0,
        "Foot and Ankle": 0,
        "Upper Extremity": 0,
        "General": 1,
    },
]
grt_Data = []

for i in get_data:
    d ={
            "label": i.get("label"),
            "data": [i.get("Trauma"), i.get("Arthroplasty"), i.get("Pediatrics"), i.get("Sports"), i.get("Foot and Ankle"), i.get("Upper Extremity"), i.get("General")],
        }
    grt_Data.append(d)

print(grt_Data)


# output = []

# labels = data[0].keys()

# for l in labels:
#     count = []
#     for d in data:
#         count.append(d[l])
    
#     output.append({
#         "label": l,
#         "backgroundColor": "#398AB9",
#         "data": count
#     })
    
# print(output)



    
    
    
 

  



