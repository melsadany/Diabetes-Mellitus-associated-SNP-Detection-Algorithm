import sqlite3 
sqlite3.connect('INSULIN_SNPs.db')
conn = sqlite3.connect('INSULIN_SNPs.db')
c = conn.cursor()
c.execute('''Create table Seqinfo
([Seq_ID] INTEGER, [Clinical_pathogenicity] TEXT, [Original_Base] TEXT, [New_Base] TEXT, [Position] INTEGER)''')

Seqinfo= (
    (1, 'likely-pathogenic', 'T', 'C', 278),
    (2, 'likely-pathogenic', 'A', 'G', 125),
    (3, 'pathogenic', 'C', 'A', 3),
    (4, 'pathogenic', 'C', 'T', 3),
    (5, 'pathogenic', 'T', 'C', 59),
    (6, 'pathogenic', 'G', 'A', 147),
    (7, 'pathogenic', 'G', 'C', 147),
    (8, 'pathogenic', 'C', 'A', 274),
    (9, 'pathogenic', 'G', 'C', 100),
    (10, 'pathogenic', 'G', 'A', 16),
    (11, 'pathogenic', 'G', 'C', 16),
    (12, 'likely-pathogenic', 'T', 'C', 308),
    (13, 'pathogenic', 'C', 'T', 163),
    (14, 'pathogenic', 'C', 'T', 137),
    (15, 'pathogenic', 'T', 'C', 323),
    (16, 'pathogenic', 'C', 'G', 287),
    (17, 'pathogenic', 'C', 'T', 287),
    (18, 'pathogenic', 'C', 'A', 268),
    (19, 'pathogenic', 'G', 'A', 265),
    (20, 'pathogenic', 'A', 'G', 143),
    (21, 'pathogenic', 'A', 'C', 143),
    (22, 'pathogenic', 'C', 'A', 140),
    (23, 'pathogenic', 'A', 'C', 172),
    (24, 'pathogenic', 'C', 'G', 94),
    (25, 'pathogenic', 'C', 'T', 94),
    (26, 'likely-pathogenic', 'G', 'A', 71),
    (27, 'likely-pathogenic', 'G', 'T', 71),
    (28, 'pathogenic', 'C', 'A', 266),
    (29, 'pathogenic', 'C', 'G', 266),
    (30, 'pathogenic', 'C', 'T', 266),
    )
c.executemany('INSERT INTO Seqinfo VALUES(?,?,?,?,?);',Seqinfo);
conn.commit()
