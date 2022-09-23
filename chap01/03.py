# “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
ss = s.split(' ')
ans = []
for w in ss:
    ww = w.strip(',.')
    ans.append(len(ww))
print(ans)