#The volume of a sphere with radius r is 4/3 pi r^3. What is the volume of a sphere with radius 5?
# Hint: 392.7 is wrong!


radius = 5
volume = (4.0/3.0) * 3.14 * (radius ** 3)
print('volume of sphere with radius 5 : ',volume)
print('-----------------------------------------')

#Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. 
#Shipping costs $3 for the first copy and 75 cents for each additional copy. 
#What is the total wholesale cost for 60 copies?

price = 24.95
discount = 40.0/100.0
shipping = 3.0
shipping_extra = 0.75

discount_price = price * discount 
total_cost = (price-discount_price)*60 + shipping + (shipping_extra * 59)
print('Total wholesale cost of 60 copies ',total_cost)
print('-----------------------------------------')

#If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), 
#then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time 
#do I get home for breakfast?

start_time_hr = 6 + 52/60.0
easy_pace_hr = (8 + 15/60.0) / 60.0
tempo_pace_hr = (7 + 12/60.0) / 60.0

running_time_hr= 2 * easy_pace_hr + 3 * tempo_pace_hr
breakfast_hr = start_time_hr + running_time_hr
breakfast_min = (breakfast_hr-int(breakfast_hr)) * 60.0
breakfast_sec = (breakfast_min- int(breakfast_min)) * 60.0

print('breakfast_hr : ',breakfast_hr)
print('breakfast_min :', breakfast_min)
print('breakfast_sec :', breakfast_sec)
print('-----------------------------------------')


