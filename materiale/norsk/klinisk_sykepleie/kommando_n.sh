cat klinisk.dis |\
grep -v '^[":]'|\
grep '" N '|\
cut -d'"' -f2|\
grep -v alphabet|\
grep -v image|\
grep -v '^..$'|\
uniq|\
grep -v '[A-ZÆØÅ0-9,:;()]'|\
grep -v '^.$'|\
grep -v '^$'|\
lookup $GTLANGS/dict-nob-sme/bin/nobsme-all.fst|\
grep "+?" |\
cut -f1 |\
sort |\
uniq |\
lookup $GTLANGS/dict-nob-fin/bin/nobfin-all.fst|\
grep "+?" |\
cut -f1 |\
sed 's/$/\tN\t/' > klinisk_n_missing.csv    


