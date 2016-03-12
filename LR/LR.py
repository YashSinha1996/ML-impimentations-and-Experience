#Check exp_learn for how to set rate and iterations
def h_theta(x,thetas,para_no):
	h=0
	for (power,theta) in enumerate(thetas):
		h+=theta*(x**power)
		#print(power)
	return h

#Change according to your data
def data_reader(data1):
	data=[]
	header=list(data1[0])
	for x in data1[1:]:
		data.append(x)
	return (header,data)

from numpy import *
from matplotlib.pyplot import *
import csv
#File must be in the same cwd
file_name=input("Enter the file name to read data from: ")
file_name=file_name+".csv"	
para_no=int(input("Enter the largest power of variable to plot: "))
data1=csv.reader(open(file_name))
(header,data)=data_reader(data1)
x_s=[int(x[0])  for x in data[:]]
y_s=[int(x[1])  for x in data[:]]
print(y_s)
print(x_s)
thetas=[1 for x in range(para_no+1)]
rate=0.0005	#alpha
k=1/len(y_s)
iterations=2000000
for a in range(iterations):
	sum_total=[0.0 for j in thetas]
	for i,y in enumerate(y_s):
		h=h_theta(x_s[i],thetas,para_no)
		for j,theta in enumerate(thetas):
			sum_total[j]+=(y_s[i]-h)*(x_s[i]**j)*k
	thetas=[theta+(rate*sum_total[j]) for j,theta in enumerate(thetas)]
print (thetas)
x_c=linspace(0,12,300)
y_c=h_theta(x_c,thetas,para_no)
figure()
plot(x_c,y_c)
plot(y_s)
grid(True)
show()
h_s=[h_theta(x,thetas,para_no) for x in x_s]
diff=[abs(x-y) for x,y in zip(y_s,h_s)]
print(diff,sum(diff))
#print(h_theta(x_s[2],thetas,para_no),y_s[2],abs(y_s[2]-h_theta(x_s[2],thetas,para_no)))
