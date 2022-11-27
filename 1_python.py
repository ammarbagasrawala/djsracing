Drivers_Names = ["lEwiS_HaMiLton","MaX_vERsTapPen","SebASTIaN_vEtTeL","ChaRLeS_lEcLeRc"]

"""
● Use the enumerate() and append() functions to create two lists (named 'indices' and
‘drivers’) containing all the indices of the items in the first list and the items in the
second list from the given list.
● Use the lower() and replace() functions to remove the capitalization from all items in
'characters' and to replace any underscore, if present in an item, with a double hyphen.
"""
indices=[]
name=[]
for count,element in enumerate(Drivers_Names):
    indices.append(count)
    name.append(element.lower().replace("_","--"))

""" Write a lambda function using the len() function to return the length of a given input
sequence. Create a new list called 'temp' by using this lambda function on 'drivers' with
the help of the map() function.
sequence. Create a new list called 'temp' by using this lambda function on 'drivers' with
the help of the map() function. """

length= lambda val : len(val)
temp=list(map(length,name))
print(f"name list: {name}")
print(f"temp list (length of names): {temp}")
print(f"indices before sum of temp and incdices list {indices}")
old_indices=indices
indices=list(map(sum,zip(indices,temp)))

print(f"indices after sum of temp and incdices list {indices}")

indices.sort(reverse=True)
print(f"indices in reverse order sorted {indices}")
F1_drivers=dict(zip(old_indices,name))
print(F1_drivers)

# 2
nextgame=[]
creepy_doll = ['red_light', 'green_light', 'red_light', 'you_got_shot', 'green_light', 'you_got_shot',
'you_got_shot', 'green_light', 'you_ got_shot', 'red_light', 'green_light', 'red_light', 'you_got_shot',
'green_light','red_light', 'red_light', 'green_light', 'you_got_shot','red_light', 'you_got_shot']
for green in creepy_doll:
    if green == 'green_light':
        nextgame.append(green)

print(nextgame)