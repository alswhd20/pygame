

def split(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]   #처음3개를 넣는다. ([1, 2, 3]분할)->  [4.5.6]
         arrs.append(pice)
         arr= arr[size:] #나머지값학인 ([4, 5, 6, 7, 8, 9]) -> 7 8
     arrs.append(arr) 
     return arrs

x=[1, 2, 3, 4, 5, 6, 7, 8]
category=split(x, 3)
print(category)

for idx, val in enumerate(category):
    print( str(idx) +"==="+ str(val))

