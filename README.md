# Read.me
Task 1 (Data Points)

- for each file added by the user process should return 10 consecutive data points starting from a random timestamp

1) get the list of files
    - if no files are entered throw SE
    - add a table with the following header: FileName, Empty?, RowNr, ColumnNr, MultipleStocks
2) for each file check if:
    - there are 3 collumns (StockID, Timestamp, Price)
    - multiple StockID ?
    - date format is one of dd-MM-yyyy or dd/MM/yyyy (format all as dd-MM-yyyy)
    
3) for each OK file sort by timestamp