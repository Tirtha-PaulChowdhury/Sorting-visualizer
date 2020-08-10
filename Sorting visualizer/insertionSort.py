import  time

def insertion_sort(data, drawData, speedScale):
    for i in range(1, len(data)):
        value_to_sort = data[i]

        while data[i-1] > value_to_sort and i>0:
            data[i], data[i-1] = data[i-1] , data[i]
            i = i-1

            drawData(data, ['green' if x == i  else 'red' for x in range(len(data))])

        time.sleep(speedScale)

    drawData(data, ['green' for x in range(len(data))])