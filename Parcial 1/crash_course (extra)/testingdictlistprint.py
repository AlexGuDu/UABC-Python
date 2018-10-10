# dictwithlists = {'a':[10, 20], 'b':[50, 60]}

dictN = {'a':[10, 20], 'b':[50, 60]}
iterresult = next(iter(dictN.values()))
print(iterresult[0])

# for key in dictwithlists.keys():
#     print(dictwithlists[key][0] + dictwithlists[key][1])
