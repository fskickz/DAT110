def skuddaar(aar):

    if aar % 4 == 0:
        if aar % 100 == 0 and aar % 400 != 0:
            return False
        else:
            return True
    else:
        return False

print(skuddaar(2040))
