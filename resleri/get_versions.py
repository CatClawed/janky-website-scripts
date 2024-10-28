from os import listdir

gl_fileassets = '/home/chloe/.local/share/Steam/steamapps/common/AtelierReslerianaGL/AtelierResleriana_Data/ABCache/content_catalogs/'
jp_fileassets = '/home/chloe/.local/share/Steam/steamapps/common/AtelierResleriana/AtelierResleriana_Data/ABCache/content_catalogs/'

gl_masterdata = '/home/chloe/.local/share/Steam/steamapps/compatdata/2594920/pfx/drive_c/users/steamuser/AppData/LocalLow/KOEI TECMO GAMES CO_, LTD_/Atelier Resleriana_ Forgotten Alchemy and the Polar Night Liberator/Library'
jp_masterdata = '/home/chloe/.local/share/Steam/steamapps/compatdata/2586520/pfx/drive_c/users/steamuser/AppData/LocalLow/KOEI TECMO GAMES CO_, LTD_/レスレリアーナのアトリエ ～忘れられた錬金術と極夜の解放者～/Library'

with open(gl_masterdata, mode='rb') as f:
    content = f.read()
    pos = content.rfind(b'resleriana.com/master_data/en/') + len('resleriana.com/master_data/en/')
    print('GL Masterdata', content[pos:pos+27].decode('ascii'))

print('GL Fileasset ', listdir(gl_fileassets)[0][:-13])


with open(jp_masterdata, mode='rb') as f:
    content = f.read()
    pos = content.rfind(b'resleriana.jp/master_data/') + len('resleriana.jp/master_data/')
    print('JP Masterdata', content[pos:pos+27].decode('ascii'))

print('JP Fileasset ', listdir(jp_fileassets)[0][:-13])
