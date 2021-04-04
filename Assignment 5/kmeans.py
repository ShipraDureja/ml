with open("Gauss2.csv", "r") as f:
    a = f.readlines()
    data = []
    for i in range(len(a)):
        b = a[i].split(",")
        data.append([float(b[1]),float(b[2][:-1])])

calculate = True

cluster_o1_old = []
cluster_o2_old = []
cluster_o3_old = []

c1 = [0, 5]
c2 = [0, 4]
c3 = [0, 3]

k = 0

while calculate:

    cluster_o1 =[]
    cluster_o2 = []
    cluster_o3 = []

    sse1 = 0
    sse2 = 0
    sse3 = 0


    for j in range(len(data)):
        d1 = ((data[j][0] - c1[0])**2 + (data[j][1]-c1[1])**2)**0.5
        d2 = ((data[j][0] - c2[0]) ** 2 + (data[j][1] - c2[1]) ** 2)**0.5
        d3 = ((data[j][0] - c3[0]) ** 2 + (data[j][1] - c3[1]) ** 2)**0.5

        if d1 <= d2 and d1 <= d3:
            cluster_o1.append(data[j])
            sse1 = sse1 + d1**2

        elif d2 <= d1 and d2 <= d3:
            cluster_o2.append(data[j])
            sse2 = sse2 + d2**2


        elif d3 <= d1 and d3 <= d2:
            cluster_o3.append(data[j])
            sse3 = sse3 + d3**2

    sse = sse1 + sse2 +sse3

    print(sse, c1[0],c1[1] , c2[0],c2[1], c3[0],c3[1])

    c1x = sum(l[0] for l in cluster_o1 )/len(cluster_o1)
    c1y = sum(l[1] for l in cluster_o1 )/len(cluster_o1)
    c1[0] , c1[1]= c1x,c1y


    c2x = sum(m[0] for m in cluster_o2) / len(cluster_o2)
    c2y = sum(m[1] for m in cluster_o2) / len(cluster_o2)

    c2[0], c2[1] = c2x, c2y

    c3x = sum(n[0] for n in cluster_o3) / len(cluster_o3)
    c3y = sum(n[1] for n in cluster_o3) / len(cluster_o3)

    c3[0], c3[1] = c3x, c3y

    if k == 0:
        pass
    elif k>0:
        if (cluster_o1_old ==cluster_o1) and (cluster_o2_old == cluster_o2) and (cluster_o3_old == cluster_o3):
            calculate = False

    k = k + 1
    cluster_o1_old = cluster_o1
    cluster_o2_old = cluster_o2
    cluster_o3_old = cluster_o3













