print('Hello - It is time to Vote!')
name = input('What is your Name? ')
age = int(input('How old are you? '))
party = input('Which political party are you registered too? ')

# print("Hello,", name,'> Your political affiliation is', party)

voting_power = 25

if age >= 18:
  print(f'Congrats, {name}! You are old enough to Vote.')

  wants_to_vote = input("Would you like to Vote now? ").upper()
  if wants_to_vote == 'YES':
    print('Great! Your starting Voting-Power is:', voting_power)
    print('Lets go Vote!')

    voting_method = input('First and most importantly, do you want to Vote by Mail, Vote Early or Vote on Election Day (Mail/Early/Day)? ').upper()

    if voting_method == 'MAIL':
      ans = input(f'{name}, Be sure to complete your ballot and then SIGN the backside. Do you want to mail it or drop it off (Mail/Drop)? ').upper()

      if ans == 'MAIL':
        print(f'{name}, You mailed your ballot successfully but due to the USPS being under-funded by the Federal Government it may take longer than anticipated for your ballot to arrive & be counted. Voting-Power reduced by 5.')
        voting_power -= 5

      elif ans == 'DROP':
        print(f'{name}, You dropped your ballot off at the County Election Office or a Election Ballot Drop box! Congrats this the quickest and safest way to ensure your vote is counted! Voting-Power increased by 25!!')
        voting_power += 25

      else:
        print(f'{name}! You lost your ballot and are unable to Vote now which means you did not perform one of your responsibilities as an American. Shame!')
    
    elif voting_method == 'EARLY':
      ans = input(f'{name}, Confirm the first day you can Vote Early In-Person. Can you Vote today (Yes/No)?').upper()

      if ans == 'YES':
        print('Locate your Voting Location, take identification documents and head to the polls to Vote Early! Voting-Power increased by 25!')
        voting_power += 25
      
      else:
        print('Set a reminder in your calendar for the earliest date to Vote Early. Voting-Power increased by 5.')
        voting_power += 5

    elif voting_method == 'DAY':
      ans = input(f'Mark the date and location of your Polling Station in your calendar, {name}. Be sure to take ID with you. There may be long wait times to Vote. Would you like to Vote Early (Yes/No)?').upper()

      if ans == 'YES':
        print('Great! Locate your Voting Location, take identification documents and head to the polls to Vote Early! Voting-Power increased by 25!')
        voting_power += 25
      
      else:
        print(f'Sounds good, {name}. Fill out a EXAMPLE ballot and take it with you on Election Day to ensure a smooth process when voting.')
        voting_power += 5

    else:
      print(f"That is not a Voting option, {name}.")
  
  else:
    print(f'Ok, {name} but remember to Vote on Tuesday November 3rd, 2020!')

else:
  print(f'Sorry, you are not old enough to Vote, {name}.')