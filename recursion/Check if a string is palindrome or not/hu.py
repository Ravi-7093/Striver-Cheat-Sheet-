def reverse(start,end,lst):
    if(start<end):
        if(lst[start]==lst[end]):
            reverse(start+1,end-1,lst)
        else:
            return False
    return True

   



lst="TAKE U FORWARD"
start=0
end=len(lst)-1
print(reverse(start,end,lst))
