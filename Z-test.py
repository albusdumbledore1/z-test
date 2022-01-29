import pandas as pd 
import statistics as st 
import random as rand 
import plotly.figure_factory as ff 
import plotly.graph_objects as go

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()
mean = st.mean(data)

stdev = st.stdev(data)
print(mean,stdev)

print("@thv")
fig=ff.create_distplot([data],['Math_score'],show_hist = False)
#fig.show()

def randomsetofmean():
    dataset = []
    for i in range(0,100):
        random_index=rand.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    
    temp_mean = st.mean(dataset)
    return temp_mean

def sampling_mean():
    sampling_mean_list=[]
    for i in range(0,1000):
        temp_sampling_mean = randomsetofmean()
        sampling_mean_list.append(temp_sampling_mean)
    sample_mean = st.mean(sampling_mean_list)
    sample_stdev = st.stdev(sampling_mean_list)
    fig = ff.create_distplot([sampling_mean_list],["Math_score"],show_hist=False)
    fig.add_trace(go.Scatter(x=[sample_mean,sample_mean],y=[0,0.2],mode = "lines",name = "mean"))
    print("BTS")
    print(sample_mean,sample_stdev)
    stdev_1_start = sample_mean-sample_stdev
    stdev_1_end = sample_mean+sample_stdev
    stdev_2_start = sample_mean-(2*sample_stdev)
    stdev_2_end = sample_mean+(2*sample_stdev)
    stdev_3_start = sample_mean-(3*sample_stdev)
    stdev_3_end = sample_mean+(3*sample_stdev)
    print(stdev_1_start)
    print(stdev_1_end)
    print(stdev_2_start)
    print(stdev_2_end)
    print(stdev_3_start)
    print(stdev_3_end)


    fig.add_trace(go.Scatter(x=[stdev_1_start,stdev_1_start],y=[0,0.2],mode = "lines",name = "stdev_1_start"))
    fig.add_trace(go.Scatter(x=[stdev_1_end,stdev_1_end],y=[0,0.2],mode = "lines",name = "stdev_1_end"))

    fig.add_trace(go.Scatter(x=[stdev_2_start,stdev_2_start],y=[0,0.2],mode = "lines",name = "stdev_2_start"))
    fig.add_trace(go.Scatter(x=[stdev_2_end,stdev_2_end],y=[0,0.2],mode = "lines",name = "stdev_2_end"))

    fig.add_trace(go.Scatter(x=[stdev_3_start,stdev_3_start],y=[0,0.2],mode = "lines",name = "stdev_3_start"))
    fig.add_trace(go.Scatter(x=[stdev_3_end,stdev_3_end],y=[0,0.2],mode = "lines",name = "stdev_3_end"))

    df1 = pd.read_csv("data1.csv")
    data1 = df1["Math_score"].tolist()
    mean1 = st.mean(data1)
    print(mean1)
    fig.add_trace(go.Scatter(x=[mean1,mean1],y=[0,0.3],mode = "lines",name = "mean1"))
    zscore1 = (mean1 - sample_mean)/sample_stdev
    print(zscore1)

    df2 = pd.read_csv("data2.csv")
    data2 = df2["Math_score"].tolist()
    mean2 = st.mean(data2)
    print(mean2)
    fig.add_trace(go.Scatter(x=[mean2,mean2],y=[0,0.3],mode = "lines",name = "mean2"))
    zscore2 = (mean2 - sample_mean)/sample_stdev
    print(zscore2)


    df3 = pd.read_csv("data3.csv")
    data3 = df3["Math_score"].tolist()
    mean3 = st.mean(data3)
    print(mean3)
    fig.add_trace(go.Scatter(x=[mean3,mean3],y=[0,0.3],mode = "lines",name = "mean3"))
    zscore3 = (mean3 - sample_mean)/sample_stdev
    print(zscore3)



    




    
    
    
    fig.show()

sampling_mean()
