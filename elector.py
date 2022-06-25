# ----- Section 1 -----

#-- create an empty candidate list
candidates = []

#-- create an empty votes list
votes = []

#-- contestant index position
candidate_position = [1, 2, 3, 4, 5]

#-- creating a ballot box for each of the candidate
ballot_box1 = []
ballot_box2 = []
ballot_box3 = []
ballot_box4 = []
ballot_box5 = []

#-- while loop to fill up the candidate list with contestant
while (True):
#-- accept the name of the contestant
    contestant = input('Enter the name of the contestant: \n ')
    
#-- change the name case of the the contestant
    contestantName = contestant.title()
    
#-- put the contestant name in the candidate list 
    candidates.append(contestantName)
    
#-- count the number of contestant in the list
    count_contestant = len(candidates)

#-- prompt user to add more contestant to the list
    add_contestant = input('Do you want to add another contestant? Type y or n: \n ')

#-- if the contestant is less than 2, then force the user to add another contestant
    """ the error code, check check"""
    if (add_contestant.upper() == 'N'):
        if (count_contestant < 2):
            print('\n *** Minimum of 2 contestants')
            contestant2 = input('Please Enter the name of another contestant: \n ')
            candidates.append(contestant2.title())

#-- let the user decised if they want more contestant in the list
        if(count_contestant < 5):
                candidates.append('nil')
                if (count_contestant < 5):
                    candidates.append('nil')
                    if (count_contestant < 5):
                        candidates.append('nil')
        
#-- display the number of contestant in the list
        print('\n*** The contestant are: ')
        break
  
#-- if the list equals 5 contestant, then the list is full     
    if (count_contestant == 5):
        print('\nCandidates list is full')
        
#-- display the number of candidate in the list
        print('\n*** The contestant are: ')
        for i in candidates:
            print('- ', i)
        break    
    
#-- append nil to candidates, if contestant is not up to 5
    #elif (count_contestant < 5):
        #while(count_contestant < 5):
        #    candidates.append('nil')
        #    if (count_contestant == 5):
        #        break
        #candidates.append('nil')
        #candidates.append('nil')
        #candidates.append('nil')
        #candidates

        


# ----- Section 2 -----
#-- Display the candidate and their Vote number to the user
def dispCandidate():
    ''' Display the candidates '''
    print('\n *** Enter the number associated with the candidate you want to vote for!')
    print(candidate_position[0],':', candidates[0])
    print(candidate_position[1],':', candidates[1])
    print(candidate_position[2],':', candidates[2])
    print(candidate_position[3],':', candidates[3])
    print(candidate_position[4],':', candidates[4])

dispCandidate() #-- calling the disp candidate
    
    
#-- Get the user to vote for each candidate of their choice
while (True):            
    user_vote = int(input('Who do you want to vote for? Type 1, 2, 3, 4 or 5: \n'))

#-- Checking which candidate the user voted for    
    if (user_vote == 1):
        ballot_box1.append(1)
        print('You voted for: ', candidates[0])
        dispCandidate() #-- calling the disp candidate
        
    elif (user_vote == 2):
        ballot_box2.append(2)
        print('You voted for: ', candidates[1])
        dispCandidate() #-- calling the disp candidate
        
    elif (user_vote == 3):
        ballot_box3.append(3)
        print('You voted for: ', candidates[2])
        dispCandidate() #-- calling the disp candidate
        
    elif (user_vote == 4):
        ballot_box4.append(4)
        print('You voted for: ', candidates[3])
        dispCandidate() #-- calling the disp candidate
        
    elif (user_vote == 5):
        ballot_box5.append(5)
        print('You voted for: ', candidates[4])
        dispCandidate() #-- calling the disp candidate
        
    else:
        print('\n No Candidate using this ballot box')
        
    
#-- asking the user if they still want to continue voting    
    response = input('\n Do you still want to continue voting?: Type Y or N \n')
    if (response.upper() == 'N'):
        print('\n *** Vote Completed ***')
        break

#-- putting the total no of votes in the box variable
box0 = len(ballot_box1)
box1 = len(ballot_box2)
box2 = len(ballot_box3)
box3 = len(ballot_box4)
box4 = len(ballot_box5)

#-- assigning the votes counts to the candidate
print("\n", candidates[0], 'got:', box0, 'votes')
print("\n", candidates[1], 'got:', box1, 'votes')
print("\n", candidates[2], 'got:', box2, 'votes')
print("\n", candidates[3], 'got:', box3, 'votes')
print("\n", candidates[4], 'got:', box4, 'votes')


#-- deciding who won using the content of the box
if (box0 > box1 or box0 > box2 or box0 > box3 or box0 > box4):
    result = str(candidates[0] + ' is the winner')
elif (box1 > box0 or box1 > box2 or box1 > box3 or box1 > box4):
    result = str(candidates[1] + ' is the winner')
elif (box2 > box0 or box2 > box1 or box2 > box3 or box2 > box4):
    result = str(candidates[2] + ' is the winner')
elif (box3 > box0 or box3 > box1 or box3 > box2 or box3 > box4):
    result = str(candidates[3] + ' is the winner')
elif (box4 > box0 or box4 > box1 or box4 > box2 or box4 > box3):
    result = str(candidates[4] + ' is the winner')
else: 
    result = 'No winner for this session'
    

#-- Displaying the winner of the electoral process
print('\n Having the highest number of votes therefore {}'.format(result))


















