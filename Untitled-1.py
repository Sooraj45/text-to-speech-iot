input=True
while input:
    prompt1=input('Can I make this stupid thing work?').lower()

    if prompt1 == 'yes':
       raw_input('Hooray, I can!')
       input=False
       break
    elif prompt1 == 'no':
       raw_input('Well I did anyway!')
       input=False
       break
    else:
       raw_input('Huh?') #an answer that wouldn't be yes or no



