class CrossingEvents:

    def __init__(self, signal, value):
        self.signal = signal
        self.value = value



    def get_number_of_value_crossings(self):
        value_index = (i for i, v in enumerate(self.signal) if v == self.value)


        value_crossing_values = list()
        for i, index in enumerate(value_index):
            print (len(self.signal))

            if index == 0 or index == len(self.signal)-1 or index - next(value_index) == 1 :
                continue

            for i in range(1,len(self.signal)):
                if self.signal[index-i] != self.value:
                    previous_value = self.signal[index-i]
                    #print ("previous{}".format(previous_value))
                    break
            for i in range(1, len(self.signal)):
                if self.signal[index+i] != self.value:
                    next_value = self.signal[index+i]
                    #print("next{}".format(next_value))
                    break
            if (previous_value < self.value and next_value > self.value) or (previous_value > self.value and next_value < self.value):
                value_crossing_values.append((previous_value,next_value))

        print ("sum{}".format(len((value_crossing_values))))
        return (len((value_crossing_values)))

