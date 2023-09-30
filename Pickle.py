##import pickle
##x=[i for i in range(1,200,1)]
##with open("data.pkl","wb") as file:
##    pickle.dump(x,file)
import pickle
with open("D:\\data.pkl","rb") as  file:
    x=pickle.load(file)

print(x)
