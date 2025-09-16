thisdict={"brand ":"ford",
"model":"mustang",
"year":1964}
    
x=thisdict["model"]
print (x)


x = thisdict.get ("model")
print (x)

z = thisdict.keys()
print (z)

thisdict["colour"]="red"
thisdict["engine"]="2000"
print(z)