def reverse(start,end,lst): #using two pointer approach 
    if(start<end): #check if start is less than end 
        if(lst[start]==lst[end]): #check if first and last character is same in the list 
            reverse(start+1,end-1,lst)#using recursion to iterate over the entire list 
        else:
            return False
    return True

   



lst="TAKE U FORWARD" #input 
start=0 
end=len(lst)-1
print(reverse(start,end,lst))
