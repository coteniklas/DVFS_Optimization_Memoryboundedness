import os
import pandas as pd

benchmarks = ["./microbenchmark 0 ", "./microbenchmark 10","./microbenchmark 20","./microbenchmark 23","./microbenchmark 25","./microbenchmark 30" ,"./microbenchmark 35", "./microbenchmark 40","./microbenchmark 45", "./microbenchmark 50","./microbenchmark 55", "./microbenchmark 60", "./microbenchmark 70"]
threads= ["1","2","4"]
frequencies = [800000,2600000,4400000]
events = ["cycles","CYCLE_ACTIVITY:STALLS_TOTAL","LLC_MISSES","CYCLE_ACTIVITY:STALLS_L3_MISS,RESOURCE_STALLS:SB,CYCLE_ACTIVITY:STALLS_L1D_MISS"]
cycles=0
l3misses=0
membound=0
i = 0
if(os.path.exists("benchmark_results.txt")):
    os.remove("benchmark_results.txt")
output=open("benchmark_results.txt","w+")
for b in benchmarks:
    for t in threads:
        with open("results_"+b[17]+b[18]+"_"+t+"Thread") as openfile:
            output.write(""+b[17]+b[18]+"\n")
            print(""+b[17]+b[18])
            membound=0
            cycles=0
            l3misses=0
            for line in openfile:
                for part in line.split():
                    if "cycles" in part:
                        cycles=float(""+line.replace("cycles",""))
                        #print(""+line,end='')
                    if "CYCLE_ACTIVITY:STALLS_L3_MISS" in part:
                        l3misses=float(""+line.replace("CYCLE_ACTIVITY:STALLS_L3_MISS",""))
                        membound= str(l3misses/cycles)
                        #membound=membound.replace('.',',')
                        output.write(membound+"\n")
                        print(membound)
output.close()

fieldnames=[]
columns = []
with open ("benchmark_results.txt","r") as infile, open("output_bench.csv","w",newline='') as outfile:
    for b in benchmarks:
        fieldnames.append(""+b[17]+b[18])
        columns.append(""+b[17]+b[18])
    thewriter=csv.DictWriter(outfile, fieldnames=fieldnames)
    thewriter.writeheader()
    memlist = []
    for row in infile:
        if row.strip() in columns:
            memlist.append(next(infile).strip())
            memlist.append(next(infile).strip())
            memlist.append(next(infile).strip())
    for i in range(0,9):
        thewriter.writerow({""+columns[0] : ""+memlist[i],""+columns[1] : ""+memlist[i+9] , ""+columns[2] : ""+memlist[i+18], ""+columns[3] : ""+memlist[i+27], ""+columns[4] : ""+memlist[i+36], ""+columns[5] : ""+memlist[i+45], ""+columns[6] : ""+memlist[i+6*9],""+columns[7] : ""+memlist[i+7*9] , ""+columns[8] : ""+memlist[i+8*9], ""+columns[9] : ""+memlist[i+9*9], ""+columns[10] : ""+memlist[i+10*9], ""+columns[11] : ""+memlist[i+11*9],""+columns[12] : ""+memlist[i+12*9] })