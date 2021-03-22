year = input("Enter the Ferrari 250 GTO year:")
year = int(year)

if year < 1962:
    print ("Unfortunately, No Ferrari 250 GTO existed then!")
elif year <= 1964:
#canʻt concatenation numbers. Must turn them into a string.
    print ("\nThe price of a Ferrari 250 GTO in " + str(year) + " was $18,500")
elif year <= 1968:
    print ("\nThe price of a Ferrari 250 GTO in " + str(year) + " was $6,000")
elif year <= 1971:
    print ("The price of a Ferrari 250 GTO in " + str(year) + " was $12,000")
elif year <= 1975:
    print ("The price of a Ferrari 250 GTO in " + str(year) + " was $48,000")
elif year <= 1980:
    print ("The price of a Ferrari 250 GT in " + str(year) + " was $200,000")
elif year <= 1985:
    print ("The price of a Ferrari 250 GT in " + str(year) + " was $650,000")
elif year <= 2012:
    print ("The price of a Ferrari 250 GT in " + str(year) + " was $35,000,000")
elif year <= 2014:
    print ("The price of a Ferrari 250 GT in " + str(year) + " was $52,000,000")
else:
    print ("No data for a Ferrari 250 GT data is available for that year.")
