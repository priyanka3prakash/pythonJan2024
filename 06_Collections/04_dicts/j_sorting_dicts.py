# sorted() list.sort()
# reversed() list.reverse

print(f"{sorted('abacus')      =}")
print(f"{sorted('322321')      =}")
print(f"{sorted([23,43,-2, 1]) =}")
print(f"{sorted([23,43,-2, 1], reverse=True) =}")


print()
frequency1 = {"a": 3, "b": 2, "c": 2, "d": 1}
print(f"{frequency1                 =}")
print(f"{sorted(frequency1)         =}")
print(f"{sorted(frequency1.keys())  =}")
print(f"{sorted(frequency1.values())=}")


print()
print(f"{sorted(frequency1.items()) =}")
# default - sort by 0th value in pair

print(f"{sorted(frequency1.items(), reverse=True) =}")

print()
print(f"{sorted(frequency1.items()) =}")
print(f"{sorted(frequency1.items(), key=lambda tpl: tpl[0]) =}") # by key
print(f"{sorted(frequency1.items(), key=lambda tpl: tpl[0], reverse=True) =}") # by key


print()
print(f"{sorted(frequency1.items(), key=lambda x:x[1]) =}")  # sort by value
print(
    f"{sorted(frequency1.items(), key=lambda x:x[1], reverse=True) =}"
)  # sort by value
print()



frequency_result = dict(sorted(frequency1.items(), key=lambda x: x[1], reverse=True))
print(frequency_result)
print(frequency_result.keys())
print("Top 3 chars in frequency are", list(frequency_result.keys())[:3])



# In character frequency analyses, try to get top 5 occurring characters
print(sorted(frequency1.items(), key=lambda x: x[1])[-5:])


"""
Assignment
==========
choose a large sentence greater than 150 words and perform the following
1) character frequency analyses
    a) case sensitive
        {
            'P': 1,
            'y': 2,
            't : 5
            ....
        }
    b) case insensitive
        {
            'p': 2,
            'y': 2,
            't : 5
            .....
        }
        HINT: str.lower()
2) word frequency analyses
    a) case sensitive
    b) case insensitive
    HINT: str.split()

3) cleansed_words frequency analyses
        HINT: string module -> string.punctuation
    a) case sensitive
    b) case insensitive

    Are you coming?  --> ['Are', 'you', 'coming']

"""