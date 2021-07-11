# -*- coding: UTF-8 -*- 
pod_name=['name1','name2','name3','name4']
cnt=4
all_dict={'name1':[],'name2':[],'name3':[],'name4':[],'all':[]}
if __name__=="__main__":
    with open("test.txt","r") as f:
        count=1
        for key in all_dict.keys():
            for i in range(4):
                listtemp=[0]*4
                all_dict[key].append({"test":listtemp})
        print(all_dict)
        group=[]
        No=1
        pod_count={'name1':[0,0],'name2':[0,0],'name3':[0,0],'name4':[0,0]}
        
        for line in f.readlines():
            print(line)
            if line[1] == No:
                group.append(line)
                if No == 1:
                    pod_count[line.strip('\n').split()[-2]][0]+=1
            else:
                for itemline in group:
                    pname=itemline.strip('\n').split()[-2]
                    pod_count[pname][1]+=1
                    if pod_count[pname][1] < pod_count[pname][0]:
                        


                




   

            all_dict["all"]

    print(all_dict)
    print("hello world!")