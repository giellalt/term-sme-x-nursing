cat $GTLANGS/term-sme-x-nursing-private/materiale/norsk/klinisk_sykepleie/klinisk?.txt |\
hfst-tokenise -cg $GTLANGS/lang-nob/tools/tokenisers/tokeniser-disamb-gt-desc.pmhfst |\
vislcg3 -g $GTLANGS/lang-nob/src/cg3/disambiguator.cg3 |\
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
lookup $GTHOME/words/dicts/nobsme/bin/nobsme-all.fst|\
grep "+?"|\
cut -f1|\
sort|\
uniq -c|\
sort -nr|\
cut -c6-|\
lookup $GTHOME/words/dicts/nobfin/bin/nobfin-all.fst|\
grep "+?"|\
cut -f1 > klinisk_a_missing.freq


