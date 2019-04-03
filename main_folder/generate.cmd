python %1\tm.py --dfd | dot -Tpng -o %1\dfd.png
python %1\tm.py --seq | java -Djava.awt.headless=true -jar plantuml.jar -tpng -pipe > %1\seq.png
python %1\tm.py --report template.md | pandoc -f markdown -t html > %1\report.html