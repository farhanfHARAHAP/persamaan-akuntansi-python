# Model

class Persamaan:

  def __init__(self):
    # Fundamental (uneditable)
    self._asset = 0
    self._liability = 0
    self._equity = 0

    #  (editable)
    self.asset_cash = 0
    self.asset_equipment = 0
    self.liability_cash = 0
    self.liability_equipment = 0
    self.equity_income = 0
    self.equity_outcome = 0

  def update(self):
    self._asset = self.asset_cash + self.asset_equipment
    self._liability = self.liability_cash + self.liability_equipment
    self._equity = self.equity_income - self.equity_outcome

  def show(self, desc='No description.', date='0/0/0'):
    self.update()
    map = {
        'a1': self.asset_cash,
        'a2': self.asset_equipment,
        'l3': self.liability_cash,
        'l4': self.liability_equipment,
        'e5': self.equity_income,
        'e6': self.equity_outcome,

        's1': self._asset,
        's2': self._liability,
        's3': self._equity
    }
    print(f'''
DATE: {date}
DESC : {desc}

A (cash {map['a1']:,} + equipment {map['a2']:,}) = L (cash {map['l3']:,} + equipment {map['l4']:,}) + E (income {map['e5']:,} - outcome {map['e6']:,})

ASSET (A) {map['s1']:,} = LIABILITY (L) {map['s2']:,} + EQUITY (E) {map['s3']:,}

    ''')
	

# View

def menu_awal():
  print('''
== MENU ==
Aplikasi ini membantu anda memahami persamaan akutansi dasar dengan mensimulasikannya.
Ayo coba sekarang~~

Berikut kegiatan yang biasa dilakukan dalam bisnis (pilih satu):
  1. Menambah modal untuk usaha.
  2. Menambah barang untuk usaha.
  3. Hutang: Bentuk pinjaman uang.
  4. Hutang: Bentuk barang yang dibayar nanti.
  5. Membeli barang untuk usaha dengan modal.
  6. Membayar hutang / gaji pegawai.
  7. Membayar hutang barang.

  ''')
  opt = int(input('*Pilih: '))

  print('''
Untuk mensimulasikan kegiatan, mesin perlu nominal.
  ''')

  val = int(input('*Nilai nominal: '))

  return {'opt':opt, 'val':val}


# Controller

pers = Persamaan()
day, month, year = 0, 5, 23

while True:
  day = 0 if day == 30 else day
  day += 1
  month += 1 if day == 30 else month

  ops = menu_awal()

  if ops['opt'] == 1: # 1. Menambah modal untuk usaha.
    pers.equity_income += ops['val']
    pers.asset_cash += ops['val']
    pers.show(desc=f"{ops['val']:,} Menambah modal untuk usaha.", date=f"{day}/{month}/2023")
  elif ops['opt'] == 2: # 2. Menambah barang untuk usaha.
    pers.equity_income += ops['val']
    pers.asset_equipment += ops['val']
    pers.show(desc=f"{ops['val']:,} Menambah barang untuk usaha.", date=f"{day}/{month}/2023")
  elif ops['opt'] == 3: # 3. Hutang: Bentuk pinjaman uang.
    pers.liability_cash += ops['val']
    pers.asset_cash += ops['val']
    pers.show(desc=f"{ops['val']:,} Hutang: Bentuk pinjaman uang.", date=f"{day}/{month}/2023")
  elif ops['opt'] == 4: # 4. Hutang: Bentuk barang yang dibayar nanti.
    pers.liability_equipment += ops['val']
    pers.asset_equipment += ops['val']
    pers.show(desc=f"{ops['val']:,} Hutang: Bentuk barang yang dibayar nanti.", date=f"{day}/{month}/2023")
  elif ops['opt'] == 5: # 5. Membeli barang untuk usaha dengan modal.
    pers.asset_cash -= ops['val']
    pers.asset_equipment += ops['val']
    pers.show(desc=f"{ops['val']:,} Membeli barang untuk usaha dengan modal.", date=f"{day}/{month}/2023")
  elif ops['opt'] == 6: # 6. Membayar hutang modal / gaji pegawai.
    pers.asset_cash -= ops['val']
    pers.liability_cash -= ops['val']
    pers.show(desc=f"{ops['val']:,} Membeli barang untuk usaha dengan modal.", date=f"{day}/{month}/2023")
  elif ops['opt'] == 7: # 7. Membayar hutang barang.
    pers.asset_cash -= ops['val']
    pers.liability_equipment -= ops['val']
    pers.show(desc=f"{ops['val']:,} Membayar hutang barang.", date=f"{day}/{month}/2023")
  else:
    print('\nERROR: PERHATIKAN INPUT YANG BENAR!\n')