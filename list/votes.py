
#read all votes into a list
#find all cities  in list
#find all people in list
#for each person find its vote in whole cities list and stor it in compond list
#finde out who voted! 

filename='people.csv'


def find_all_comma(st):
    b=[]
    b=[st.find(',')]
    b.append(st.find(',',b[0]+1))
    b.append(st.find(',',b[1]+1))
    return(b)

def read_votes(filename):
    vote_file=open(filename,'r')
    aline=vote_file.readline()
    votes=[]
    while aline!='':
        aline=vote_file.readline()
        comma=find_all_comma(aline)
        vote=[]
        vote.append((aline[:comma[0]]))
        vote.append(aline[comma[0]+1:comma[1]])
        vote.append((aline[comma[1]+1:comma[2]]))
        vote.append(aline[comma[2]+1:][:-1])
        votes.append(vote)  
    vote_file.close()
    return votes


def find_cities(votes):
    cities=[]
    for vote in votes:
        if not vote[3] in cities:
            cities.append(vote[3])
    return cities

def find_cities(votes):
    cities=[]
    for vote in votes:
        if not vote[3] in cities:
            cities.append(vote[3])
    return cities


def find_individual(votes):
    individuals=[]
    for vote in votes:
        if not vote[1] in individuals:
            individuals.append(vote[1])
    return individuals


votes=read_votes(filename)
cities=find_cities(votes)
individuals=find_individual(votes)
individuals.index('Mohammad')
