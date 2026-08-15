#Given an integer array, return True if any value appears at least twice.
def dupplicate(marks):
    seen=set()
    for mark in marks:
        if mark in seen:
            return True
        seen.add(mark)
    return False
print(dupplicate([23,45,67,98,90,54,29,73,83,64,23]))
print(dupplicate([45,67,98,90,54,29,73,83,64,23]))

#alternatively use the lens


 
    


    
