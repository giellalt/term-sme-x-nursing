cat klinisk.dis |\
grep -v '^[":]'|\
grep '" A '|\
cut -d'"' -f2|\
grep -v alphabet|\
grep -v image|\
grep -v '^..$'|\
uniq|\
grep -v '[A-ZÆØÅ0-9,:;()]'|\
grep -v '^.$'|\
grep -v '^$'|\
lookup $GTLANGS/dict-nob-sme/bin/nobsme-all.fst|\
grep "+?"|\
cut -f1|\
sort|\
uniq -c|\
sort -nr|\
cut -c6-|\
lookup $GTLANGS/dict-nob-fin/bin/nobfin-all.fst|\
grep "+?"|\
sed 's/$/\tA\t/' |\
cut -f1 > klinisk_a_missing.freq


