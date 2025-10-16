is_raining = True
is_windy = True

stay_inside = is_raining and is_windy

print("Stay inside:", stay_inside)

take_coat = is_raining or is_windy

print("Take coat:", take_coat)

print("Not windy :" + str(not is_windy))

take_umbrella = is_raining and not is_windy

print("Take umbrella:" +  str(take_umbrella))