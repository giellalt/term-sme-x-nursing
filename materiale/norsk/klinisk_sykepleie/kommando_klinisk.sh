cat $GTLANGS/term-sme-x-nursing-private/materiale/norsk/klinisk_sykepleie/klinisk?.txt |\
hfst-tokenise -cg $GTLANGS/lang-nob/tools/tokenisers/tokeniser-disamb-gt-desc.pmhfst |\
vislcg3 -g $GTLANGS/lang-nob/src/cg3/disambiguator.cg3 |\
> klinisk.dis

