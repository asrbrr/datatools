'''
csvh module - CSV helper

This module is intended to help review and somewhat mungle CSV files.
Typically, this would be done before a pd.read_csv(), as a conevenience
tool to identify NA values, know data types etc

'''


def num_rows(filepath):
    '''
    Returns number of rows in the CSV files
    Arguments:
    ---------
     - f : file-like object
    Returns: 
    --------
     - lines : integer, number of rows in files (including empty rows!)
    '''

    lines = 0
    with open (filepath, 'r') as f:
        for line in f:
            lines += 1
    return lines


def snif_delimiter(filepath):
    '''
    Returns the infered delimiter of the CSV file.

    Arguments:
    ---------
     - filepath : file-like object
    Returns: 
    --------
     - delimiter : string

    '''
    import csv
    with open(filepath , 'r') as f:
        dialect = csv.Sniffer().sniff(f.read(9999))
    return(dialect.delimiter)


def show_head(filepath, nrows=5, nchars=70):
    '''
    Prints the first N rows, and the first M characters of each row, for 
    visual inspection.

    Arguments
    ---------
     - filepath : file-like object
     - nrows : optional, integer, number of rows to show. Default=5
     - nchars : optinal, integer, number of characters of each row to show.
            Use None or -1 to show all the line
    Returns
    -------
     - list of nrows head  rows
     '''

    head = []
    with open(filepath , 'r') as f:           
        for i, line in enumerate(f):
            if i == nrows:
                break
            values = line[:nchars]
            head.append(values) 
    return head


def show_tail(filepath, nrows=5, nchars=70):
    '''
    Prints the last N rows, and the first M characters of each row, for 
    visual inspection.

    Arguments
    ---------
     - filepath : file-like object
     - nrows : optional, integer, number of rows to show. Default=5
     - nchars : optinal, integer, number of characters of each row to show.
            Use None or -1 to show all the line
    Returns
    -------
     - list of nrows tail  rows
     '''

    tail = []
    totalrows = numrows(filepath)
    with open(filepath, 'r') as f:           
        for i, line in enumerate(f):
            if i < totalrows - nrows:
                continue
            values = line[:nchars]
            tail.append(values) 
    return tail


def show_random(filepath, nrows=5, nchars=70):
    '''
    Prints a bunch of random rows, in case head and tail contained misleading
    values.

    Arguments
    ---------
     - filepath : file-like object
     - nrows : optional, integer, number of rows to show. Default=5
     - nchars : optinal, integer, number of characters of each row to show.
            Use None or -1 to show all the line
    Returns
    -------
     - list of nrows random rows rows
     '''

    import random
    totalrows = numrows(filepath)
    randrows = [random.randint(1,totalrows) for _ in range(nrows)]
    values = []
    with open(filepath, 'r') as f:           
        for i,line in enumerate(f):
            if i in randrows:
                value = line[:nchars]
                values.append(value)
    return values


def find_nans(filepath, hasheaders = True, hasindexcol=True):
    '''
    Passes through the columns 'the old way' (iterating)
    and enumerates non-numeric fields to be used as NaN identifiers
    
    Arguments:
    ----------
     - path : file object to be analysed. Assumes CSV format-
     - hasheaders : optional, default=True. Whether to skip first line
     - hasindexcol : optional, default=True. Whether to skip first col
    
    Returns: 
     - nan_list : set with nan values found
    '''
    import csv
    exceptions = set()

    with open(filepath) as f:
        csvr = csv.reader(f)
        for line in csvr:
            if hasheaders:
                hasheaders = False
                continue
            for item in line[hasindexcol:]:
                try:
                    float(item)
                except:
                    exceptions.add(item)
        return exceptions






