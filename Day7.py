# creating an empty set
st = set()

# creating a set with initial items
st = {'item1', 'item2', 'item3', 'item4'}

fruits = {'banana', 'orange', 'mango', 'lemon'}

st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits) 

# Adding items to set

st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')

# adding multiple items using update(it takes a list of argument)
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])

# example
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)

# removing an item from a set using remove()

st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')

# pop() method
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set

# clearing items in a set
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()

# example
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()

# deleting a set
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st

fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
