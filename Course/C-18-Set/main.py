########## Set
dapur = {"fork","spoon","knife"}
piring = {"mangkok","piring","gelas","knife"}
dapur.add("gombal")
dapur.remove("spoon")
dapur.clear()
dapur.update(piring)
dinner_table = dapur.union(piring)
for i in dinner_table:
    print(i)
print(piring.difference(dapur))
print(dapur.intersection(piring))