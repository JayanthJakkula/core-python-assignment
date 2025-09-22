#calculate positive feedback percent
def feedback_calculate(feed):
    count=0
    for i in feed:
        if i==4 or i==5:
            count+=1
    return (count/len(feed))*100

ratings=list(map(int,input("enter ratings(1-5) : ").split(",")))
print(f"Positive Feedback: {feedback_calculate(ratings)}%")