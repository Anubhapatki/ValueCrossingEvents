class CrossingEvents:

    def __init__(self, signal, value):
        self.signal = signal
        self.value = value



    def get_number_of_value_crossings(self):
        value_index = (i for i, v in enumerate(self.signal) if v == self.value )


        value_crossing_values = list()
        for index in value_index:
            print (index)
            for i in range(1,len(self.signal)):

                if self.signal[index-i] != self.value:
                    previous_value = self.signal[index-i]
                    print ("previous{}".format(previous_value))
                    break
            for i in range(1, len(self.signal)):
                if self.signal[index+i] != self.value:
                    next_value = self.signal[index+i]
                    print("next{}".format(next_value))
                    break
            if (previous_value < self.value and next_value > self.value) or (previous_value > self.value and next_value < self.value):
                value_crossing_values.append((previous_value,next_value))



        print (set(value_crossing_values))
        print (len(set(value_crossing_values)))
        return (len(set(value_crossing_values)))






"""
if __name__=="__main__":
    signal = [1,2,3,3,4,5,5,6,3, 2,1]
    value = 5
    print (value)

    sum = CrossingEventsEvents(signal, value).get_number_of_value_crossings()
"""