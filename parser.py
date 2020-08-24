# -*- coding: utf-8 -*-
from __future__ import print_function
from tokens import *
import ply.yacc as yacc

def p_error(p):
    print("error")

def p_expression_dictionary(p):
    '''dictionary : key_or_value LPAREN dictionary RPAREN
                  | key_or_value LPAREN RPAREN
                  | key_or_value LPAREN dictionary
                  | key_value_pair dictionary
                  | dictionary dictionary
                  | key_value_pair
    '''
    if len(p)==5:
        p[0]={
            p[1]:p[3]
        }
    elif len(p)==4:
        if p.slice[3].type=="RPAREN":
            p[0]={}
        else:
            p[0]={
                p[1]:p[3]
            }
    elif len(p)==3:
        p[0]=dict(p[1].items()+p[2].items())
    else:
        p[0]=p[1]

def p_expression_key_value_pair(p):
    '''key_value_pair : key_or_value key_or_value'''
    p[0] = {
        p[1]:p[2]
    }

def p_expression_key(p):
    '''key_or_value : ID
           | STRING
           | INT
           | FLOAT
    '''
    target=p.slice[1]
    if target.type=="STRING":
        p[1]= p[1].replace("\"","")
    elif target.type=="INT":
        p[1]= int(p[1])
    elif target.type=="FLOAT":
        if p[1].count(".")==1:
            p[1]= float(p[1])
    p[0] = p[1]

lexer = lex.lex()
parser = yacc.yacc()

def parse_to_json(text):
    result = parser.parse(text, lexer=lexer)
    return result

def main():
    text = open("addoninfo.txt").read()
    data = parse_to_json(text)
    temp = ""

if __name__ == "__main__":
    main()
