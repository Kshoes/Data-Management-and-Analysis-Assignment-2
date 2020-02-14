# tabletools.py

class LabeledList:

    def __init__(self, data=None, index=None):
        self.data = data
        self.index = index
        if index == None:
            self.index = list(range(len(data)))

    def __str__(self):
        string = '""""""\n'
        for x, y in zip(self.index, self.data):
            string += f'{x:>5}   {y}\n'
        return string

    def __repr__(self):
        return self.__str__()
    
    def __getitem__(self, key_list):
        
        query_data = list()
        query_index = list()
        
        if isinstance(key_list, LabeledList):
#             print(key_list.data)
#             print(key_list.index)
#             return key_list.__getitem__(key_list.data)
            for x in key_list.data:
                if x in self.index:
                    count = self.index.count(x)
                    while count >= 1:
                        query_data.append(self.data[[i for i, n in enumerate(self.index) if n == x][self.index.count(x)-count]])
                        query_index.append(x)
                        count -= 1
            return LabeledList(query_data, query_index)
                    
            
        elif isinstance(key_list, list):
            
            if isinstance(key_list[0], bool):
                count = 0
                for x in key_list:
                    if x == True:
                        query_data.append(self.data[key_list.index(x)+count])
                        query_index.append(self.index[key_list.index(x)+count])
                        count += 1
                return LabeledList(query_data, query_index)
                
            else:
                for x in key_list:
                    if x in self.index:
                        count = self.index.count(x)
                        while count >= 1:
                            query_data.append(self.data[[i for i, n in enumerate(self.index) if n == x][self.index.count(x)-count]])
                            query_index.append(x)
                            count -= 1            
                return LabeledList(query_data, query_index)
        
        elif self.index.count(key_list) == 1:
            return self.data[self.index.index(key_list)]
        
        else:
            for x in self.index:
                if x == key_list and x not in query_index:
                    count = self.index.count(key_list)
                    while count >= 1:
                        query_data.append(self.data[[i for i, n in enumerate(self.index) if n == x][self.index.count(x)-count]])
                        query_index.append(x)
                        count -= 1
            return LabeledList(query_data, query_index)
    
    
    def __iter__(self):
        return iter(self.data)
                
    def __eq__(self, scalar):
        return LabeledList([n == scalar for n in self.data])
    
    def __ne__(self, scalar):
        return LabeledList([n != scalar for n in self.data])

    def __gt__(self, scalar):
        return LabeledList([n > scalar for n in self.data])
    
    def __lt__(self, scalar):
        return LabeledList([n < scalar for n in self.data])
    
    def map(self, f):
        return LabeledList([f(n) for n in self.data])
    
# end of LabeledList
    
class Table:
    def __init__(self, data, index=None, columns=None):
        self.values = data
        self.index = index
        self.columns = columns
        if index == None:
            self.index = list(range(len(data)))
        if columns == None:
            self.columns = list(range(len(data[0])))

    def __str__(self):
        string = '       '
        for x in self.columns:
            string += f'{x:>7}'
        string += '\n'
        for y in self.index:
            string += f'{y:>7}'
            for z in self.values[self.index.index(y)]:
                string += f'{z:>7}'
            string += '\n'
        return string

    def __repr__(self):
        return self.__str__()
    
    def __getitem__(self, col_list):
        
        query_data = list()
        query_index = list()
        query_columns = list()
        
        
        if isinstance(col_list, LabeledList):
            
            i,col = enumerate(self.columns)
            print(i)
            print(col)
            for x in col_list.data:
                if x in self.columns:
                    query_columns.append(x)
                    
                    for y in self.values:

                        if row == None:
                            row = list()
                        for z in y:
                            row.append()
                        query_data.append([])
                    
                    
                
            
        elif isinstance(col_list, list):
            
#             indices = list()
#             cols = list()
            
#             for i,col in enumerate(self.columns):
#                 indices.append(i)
#                 cols.append(col)
#                 print(i)
#                 print(col)
            for x in col_list:
        
                if x in self.columns:
                    count = col_list.count(x)
                    while count >= 1:
                        query_values.append(self.values[[i for i, n in enumerate(self.index) if n == x][self.index.count(x)-count]])
                        query_index.append(x)
                        count -= 1            
                return LabeledList(query_data, query_index)                
        
#                 if x in self.columns:
#                     query_columns.append(x)
                    
#                     for y in self.values:

#                         if row == None:
#                             row = list()
#                         for z in y:
#                             row.append()
#                         query_data.append([])
            
#             if isinstance(col_list[0], bool):
                
#             else:
    
    def head(self, n):
        new_index = list(range(n))
        return Table(self.values, new_index, self.columns)

    def tail(self, n):
        new_index = self.index[-n:]
        return Table(self.values, new_index, self.columns)
    
    def shape(self):
        return(len(self.index), len(self.columns))
    
# end of Table
    
def read_csv(fn):
    file = open(fn, encoding="utf8")
    
    table_values = list()
    table_index = list()
    
    header = file.readline()
    table_columns = [i for i in header.strip().split(",")]
    
    for line in file.readlines():
        curr_line = line.strip().split(",")
        table_index.append(curr_line.pop(0))
        single_value = list()
        for d in curr_line:
            single_value.append(d)
        table_values.append(single_value)
        
    file.close()
    
    return Table(table_values, table_index, table_columns)