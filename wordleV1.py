
worda = 'apple'
print ('the word length is',len(worda))

attempt = 0
while attempt < 5:
    j=0
    clc= []
    wlc=[]
    print('guess the answer:')
    answer = input()

    if len(answer) != len(worda):
        print('the answer has to be', len(worda),'letters')
        attempt += 1;
        continue

    while j < len(worda):
        if answer[j] == worda[j]:
            clc.append(answer[j])
            j += 1

        elif answer[j] != worda[j]:
            print ('you guessed',len(clc), 'letters from the word, but it is in wrong order, letters are', sorted(clc))
            if answer[j] not in worda:
                wlc.append(answer[j])
                if len(wlc) > 0:
                    print(wlc,'letter is not needed in the word')
            break   
    attempt += 1
    print('you used',attempt,'out of 5 attempts')
    if answer == worda:
        print('you guessed it right, the answer is', worda)
        break

if answer != worda:
    print('you ran out of attempts, the word is', worda)