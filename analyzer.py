import csv

contributors = {}
total_commits = 0

with open("data/sample_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        author = row["author"]
        commits = int(row["commits"])

        contributors[author] = contributors.get(author, 0) + commits
        total_commits += commits

print("Community Metrics Report")
print("-------------------------")
print("Total Contributors:", len(contributors))
print("Total Commits:", total_commits)
print(
    "Average Commits per Contributor:",
    round(total_commits / len(contributors), 2)
)
