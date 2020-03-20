import csv

total_votes = 0
candidates = []

khan_votes = 0
correy_votes = 0
li_votes = 0
o_tooley_votes = 0

with open("election_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        candidates.append(row[2])
        total_votes = total_votes + 1
        
        if row[2] == 'Khan':
            khan_votes = khan_votes + 1
        elif row[2] == 'Correy':
            correy_votes = correy_votes + 1
        elif row[2] == 'Li':
            li_votes = li_votes + 1
        else:
            o_tooley_votes = o_tooley_votes + 1

candidates = list(dict.fromkeys(candidates))

khan_prcnt = "{:.3%}".format(khan_votes/total_votes)
correy_prcnt = "{:.3%}".format(correy_votes/total_votes)
li_prcnt = "{:.3%}".format(li_votes/total_votes)
o_tooley_prcnt = "{:.3%}".format(o_tooley_votes/total_votes)

totals = [khan_votes, correy_votes, li_votes, o_tooley_votes]
winner = str(candidates[totals.index(max(totals))])

print("Election Results")
print("-------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------")

print(f'{candidates[0]}: {khan_prcnt} ({khan_votes})')
print(f'{candidates[1]}: {correy_prcnt} ({correy_votes})')
print(f'{candidates[2]}: {li_prcnt} ({li_votes})')
print(f'{candidates[3]}: {o_tooley_prcnt} ({o_tooley_votes})')

print("-------------------------")
print(f'Winner: {winner}')
print("-------------------------")

with open("Election_Results.txt", "w") as f:
 
    print("Election Results", file=f)
    print("-------------------------", file=f)
    print(f'Total Votes: {total_votes}', file=f)
    print("-------------------------", file=f)

    print(f'{candidates[0]}: {khan_prcnt} ({khan_votes})', file=f)
    print(f'{candidates[1]}: {correy_prcnt} ({correy_votes})', file=f)
    print(f'{candidates[2]}: {li_prcnt} ({li_votes})', file=f)
    print(f'{candidates[3]}: {o_tooley_prcnt} ({o_tooley_votes})', file=f)

    print("-------------------------", file=f)
    print(f'Winner: {winner}', file=f)
    print("-------------------------", file=f)
