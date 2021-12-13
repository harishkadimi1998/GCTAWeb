from django.shortcuts import render,redirect
from django.db import connection




def fillddl(query,slectedValue):

    cursor = connection.cursor()
    connection.commit()
    cursor.execute(query)
    result = cursor.fetchall()
    strData = '<option value="">--Select--</option>'
    for ids in result:
        value = ids[0]
        display = ids[1]
        if slectedValue == value:
            strData += '<option value="'+value+'" selected>'+display+'</option>'
        else:
            strData += '<option value="'+value+'">'+display+'</option>'
    
    return strData