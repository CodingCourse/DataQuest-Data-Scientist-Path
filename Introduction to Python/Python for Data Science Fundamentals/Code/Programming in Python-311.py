## 2. Python Syntax ##

print(30+10+40+20)
print(4-8)
print(-5+13)
print(-3-(-3))
print(+5-(+3))

## 3. Computer Programs ##

print(34-(-5))
print(-34)
print(+34)
print(34)


## 4. Arithmetical Operations ##

print(16*10)
print(16/10)
print(16**10)
print(4**3+13)
print(6*7-2**3)
print((12**2)**2-2**(1+2**3))

## 5. Variables ##

result1 = (5 + 20) * 2
result2 = 10**2
print(result1)
print(result2)
print(result1+10)
print(result2*4**2)
print(result1+result2)
print((result1+result2)/result1)

## 7. Updating Variables ##

variable_1 = 20
variable_2 = 20
variable_3 = 100
variable_2 += 10
variable_2 -= variable_1
variable_3 = variable_1
print(variable_1,variable_2,variable_3)

## 8. Integers and Floats ##

variable_1 = 10
variable_2 = 2.5
variable_1 += 6.5
variable_2 *= 2
variable_1 /= variable_2
variable_2 **=variable_2
print(variable_1,variable_2)

## 9. Conversion Between Types ##

variable_a = 10
variable_b = 2.8
variable_a += variable_b
print(variable_a)
print(round(variable_b))
print(variable_b)
variable_b=round(variable_b)
print(variable_b)

## 10. Strings ##

app_name = 'Pandora - Music & Radio'
average_rating = '4.0'
total_ratings = '1724546'
price = 'free'
description = 'Pandora - Music & Radio is free and has a 4.0 rating.'
print(app_name,description)

## 11. Escaping Special Characters ##

motto = 'Facebook\'s new motto is "move fast with stable infra".'
print(motto)

## 12. String Operations ##

facebook = "Facebook's rating is"
fb_rating = '3.5'
instagram = "Instagram's rating is"
insta_rating = '4.5'
fb = facebook + ' ' + fb_rating + '.'
insta = instagram + ' ' + insta_rating + '.'
fb_insta = fb + ' ' + insta
print(fb,insta,fb_insta,sep="\n")