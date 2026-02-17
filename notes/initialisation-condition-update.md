In order to create a successful loop, 3 distinct steps need to be present:

- Initialisation
- Condition
- Update

## Initialisation

This refers to setting the values of the variable used for the condition in the loop. They are also often called iteration or iterator variables. It's performed before the first loop begins.

## Condition

This defines how long the loop is executed for. It's set out at the start of the loop. 

## Update

The variables within the condition are *updated* so that each iteration brings the loop closer to being completed.

```python
# ask for a number
number = int(intput("Please type in a number: ")) # this is the Initialisation

# repeat while the number is less than 10
while number < 10: # this is the condition

# print out and increment number
  print(number)
  number += 1 # updating variable

print("Execution finished.")
```
