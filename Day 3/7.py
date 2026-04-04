# 1. rstrip()==> remove space from right side
# 2. lstrip()===> remove space from left side
# 3. strip()===> remove space from both side

programming = input("Enter programming Name : ")
p_name = programming.rstrip()
if p_name =='Python':
    print(p_name)
elif p_name == 'Java':
    print(p_name)
elif p_name == 'Cpp':
    print(p_name)
else:
    print("wrong programming name")

