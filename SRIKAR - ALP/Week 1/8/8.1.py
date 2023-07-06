'''
In these tasks you will be given one or more examples of code.

- Look at each example , study it carefully.
- Write a prediction of what it will do when it runs. Your prediction should be added to the code as comments. You should use the key terms list, item and index in your predictions.
- Run the code, compare what happens to your prediction.
- Add comments to note down and differences between your prediction and what actually happened.

'''

# Example Code 1

Sentence = ["Always", "look", "on", "the", "bright", "side", "of",]# The sentence will have no spaces and the output is Alwayslookonthebrightsideof
print(Sentence)# it will show thd output above
print(Sentence[1])# it will only say always since it is the second word since code always starts at 0 and then goes to 1
Sentence.append("life") #It will take out life in the sentence
Sentence[4] = "sunny" # it will only say sunny
print(Sentence[4]) #It will say sunny
print(Sentence[0] + " " + Sentence[3]) #It will say always the
print(Sentence) # it will repeat the original sentence