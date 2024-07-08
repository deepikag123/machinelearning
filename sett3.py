s1={0,1,2,3,4}
s2={5,6,7,8}
s3={1,9,2}
print("set:",s1)
a=s1.union(s2)
print("union:",a)
b=s1.intersection(s3)
print("intersection:",b)
c=s1.symmetric_difference(s3)
print("symmetric_difference:",c)
d=s3.difference(s2)
print("difference:",d)
e=s2.issuperset(s3)
print("issuperset:",e)







