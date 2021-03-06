#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

#take the input
num = int(input())

#analyse the input
while num <= 2 or not num <= 10:    
    num = int(input())

scores = input()    #input the scores with space bar in b/w
score_list = scores.split()  #store the scores into a list, remember: the values are still strings

#initialize the highest and runner ups
high = None
runner = None

#loop to check and assign the values
for i in range(num):
    if high is None:
        high = int(score_list[i])
        continue
    elif runner is None:
        if int(score_list[i]) < high:
            runner = int(score_list[i])    
    if int(score_list[i]) > high:
        runner = high
        high = int(score_list[i])
    try: #as comparing int to a None type object results into traceback, we use try, except
        if int(score_list[i]) > runner:
                if int(score_list[i]) < high:
                    runner = int(score_list[i])
    except:
        continue
print(runner)