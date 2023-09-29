def anonymous_filter(s):
    anonymous_filter = filter(lambda x: x.lower() == 'я', list(s))
    return len(anonymous_filter) >= 23
    
   
    
#s = 'Я - последняя буква в алфавите!'
s = 'яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!'
print(anonymous_filter(s))

#print(anonymous_filter('Я - последняя буква в алфавите!'))




