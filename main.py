print('Hello - It is time to Vote!')
name = input('What is your Name? ')
age = int(input('How old are you? '))
party = input('Which political party are you registered too? ')

# print("Hello,", name,'> Your political affiliation is', party)

voting_power = 25

if age >= 18:
  print('Congrats - You are old enough to Vote.')

  wants_to_vote = input("Would you like to Vote now? ").upper()
  if wants_to_vote == 'YES':
    print('Great! Your starting Voting-Power is:', voting_power)
    print('Lets go Vote!')

    
      print("Not a Voting option.")
  
  else:
    print('Ok but remember to Vote on Tuesday November 3rd, 2020!')

else:
  print('Sorry, you are not old enough to Vote.')