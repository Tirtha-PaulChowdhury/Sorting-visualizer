import time

def selection_sort(data, drawData, speedScale):
    for i in range(len(data)-1):
        min_value = i
        for j in range(i+1, len(data)):
            if data[min_value]>data[j]:
                min_value = j

                drawData(data, ['green' if x == min_value else 'red' for x in
                            range(len(data) - 1)])  # min value and the value currently considered are green
            time.sleep(speedScale)

        if min_value != i:
            data[min_value], data[i] = data[i], data[min_value]



    drawData(data, ['green' for x in range(len(data))])

