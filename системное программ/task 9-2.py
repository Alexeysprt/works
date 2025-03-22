class AdditionTable:
    def __init__(self):
        self.rows = 9  
        self.cols = 9  
    def print_table(self):
        
        row = 1
        while row <= self.rows:  
            col = 1
            line = ""
            while col <= self.cols:  
                result = row + col 
                line += f"{col} + {row} = {result} "
                col += 1  
            print(line.strip())  
            row += 1  

table = AdditionTable()
table.print_table()