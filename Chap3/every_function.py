rivers = ['Zambezi','Luapula','Chambeshi','Kafue']

rivers.append('Kabompo')
print(rivers)

rivers.insert(0, 'Luangwa')

popped_river = rivers.pop()

rivers.remove('Zambezi')

rivers.sort()

rivers.sort(reverse=True)

sorted_rivers = sorted(rivers, reverse=True)
print(sorted_rivers)