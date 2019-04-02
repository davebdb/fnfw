#!/usr/bin/awk -f
# simple AWK application to make the CSV readable in human terms for the traffic logs
# need to work on formatting a little more and some if/else and concat statements needed

BEGIN { FS="," }

#{print $1,"T",$2,"\t",$10,"\t",$13,":",$14,"==>",$18,":",$19," | ",$20}
{printf("%s T %s | %10s | %16s:%s ==> %16s:%s | %3s | %s %s ==> %s %s | %s  \n",$1,$2,$10,$13,$14,$18,$19,$20,$25,$26,$27,$28,$55)}

