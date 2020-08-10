import time          #time function required to visualize step by step in the speed specified by user

def bubble_sort(data, drawData, speed):
    for i in range(0, len(data)-1):
        for j in range(0, len(data)-i-1):
            if data[j]>data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['green' if x==j or x==j+1 else 'red' for x in range(len(data)-1)])  #bars currently considered are green
                time.sleep(speed)

    drawData(data, ['green' for x in range(len(data))])   # at the end all bars become green


