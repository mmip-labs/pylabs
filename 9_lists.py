

children = ['ivanov_2000','aetrov_2005','sidorov_2002','Wkov_2008']

def by_year(name):
    print(name.split('_')[-1])
    return name.split('_')[-1]

#s_children = sorted(children,key=by_year)

s_children = sorted(children,key=len)

print(s_children)

