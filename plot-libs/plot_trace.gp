reset

#--------------------

filename=""
if ("$#" eq sprintf("%d",1)) filename="$0"
if (exist("fname")) filename=fname

#--------------------

set grid

set linestyle 1  linetype 1 linewidth 2 pointtype 5 linecolor rgb "#ff0000"

set term pngcairo enhanced color font "Arial,16"

#--------------------

set output "out/trace.png"

set xlabel "Time"
set ylabel "Trace"

plot filename u 1:2 w lp ls 1 noti
