a="BiswajitPatnaik"

print(a.upper())#uppercase
print(a.lower())#lowercase
print(a.title())#convertstring into titlecase
#a[0]="B"#we cannot assign data type to individual letter of inputed string
print(a.swapcase())#converts all uppercase to lowercase and vice-versa
print(a.strip("B"))#it removes both leading and trailing characters
print(a.startswith("B",0,1))#checks the starting character and returns boolean
print(a.rstrip("aik"))#removes trailing characters
print(a.rpartition("P"))#PARTITION THE STRING BASED ON THE INPUT
print(a.rindex("P"))#find the substring inside the string
print(a.rindex("sw",0,4))#returns the highest index of the substring inside the string if the substring is found. Otherwise, it raises ValueError
print(a.split("i"))#splits strings based on input charcter,the input character is removed
#formating string literals
print("{}".format("age 29"))
print('This is {1} {0}'.format('me','mine'))
#formating floating no
result=45.86376
print('value of x is {}'.format(result))
print("value of x precise is {x:1.3f}".format(x=result))#to format float we need to assign another variable to the existing variable inside print
#fstring format
print(f"My name is {a}")
print(f"My name is {a!r}")#here "!r" helps to quote the string in the printout stmnt
print(f'value of x is {result:1.3f}')#compare line 21 to line 25

 Output-
>>BISWAJITPATNAIK
>>biswajitpatnaik
>>Biswajitpatnaik
>>bISWAJITpATNAIK
>>iswajitPatnaik
>>True
>>BiswajitPatn
>>('Biswajit', 'P', 'atnaik')
>>8
>>2
>>['B', 'swaj', 'tPatna', 'k']
>>age 29
>>This is mine me
>>value of x is 45.86376
>>value of x precise is 45.864
>>My name is BiswajitPatnaik
>>My name is 'BiswajitPatnaik'
>>value of x is 45.864
