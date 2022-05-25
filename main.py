# This exercise is about printing the name as specified on the below logic based on character counts
# 1. if character counts < 3 charaters - show - "name is very short"
# 2. if character counts > 60 charaters - show - "name is very long"
# 3. or else show - name is validated


full_name = "Subramanaya"

if len(full_name) < 3:
    print("name is too short")

elif len(full_name) > 60:
    print("name is very long")

else:
    print("name is validated")


